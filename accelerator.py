# coding: utf-8

# Author: Mingzhe Du (mingzhe@nus.edu.sg)
# Date: 2025-09-22

import os
import zlib
import dotenv
import zipfile
import argparse
import zopfli.zlib
from tqdm import tqdm
from google import genai
from google.genai import types
from multiprocessing import Pool

dotenv.load_dotenv()

# Gemini Interface
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

content_template = """
Rewrite the code to be extremely shortest while maintaining the identical functionality:

{original_code}
"""

def gemini_interface(original_code):
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=-1),
            system_instruction="You are a Python code golf expert."
        ),
        contents=content_template.format(original_code=original_code)
    )
    # extract the code from the response
    try:
        raw_code = response.text.split("```python")[1].split("```")[0].strip()
    except Exception as e:
        print(f"Error: {e}")
        raw_code = response.text
    return raw_code

def zip_src(src_code):
    compressed_options = []
    for compress in [zopfli.zlib.compress, lambda data: zlib.compress(data, 9)]:
        for trailing in [b"", b"\n"]:
            src = src_code + trailing
            # We prefer that compressed source not end in a quotation mark
            while (compressed := compress(src))[-1] == ord('"'):
                src += b"#"

            def sanitize(b_in):
                """Clean up problematic bytes in compressed b-string"""
                b_out = bytearray()
                for b in b_in:
                    if b == 0:
                        b_out += b"\\x00"
                    elif b == ord("\r"):
                        b_out += b"\\r"
                    elif b == ord("\\"):
                        b_out += b"\\\\"
                    else:
                        b_out.append(b)
                return b"" + b_out

            compressed = sanitize(compressed)
            delim = b'"'
            if ord("\n") in compressed:
                delim = b'"""'
            elif ord('"') in compressed:
                delim = b"'"
            compressed_options.append(
                b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes("
                + delim
                + compressed
                + delim
                + b',"L1")))'
            )
    return min(compressed_options, key=lambda x: len(x))

def compress_code(input_dir, output_dir, task_index):
    original_code = open(f"{input_dir}/task{task_index:03d}.py", "rb").read()
    zipped_original_code = zip_src(original_code)
    
    try:
        accelerator_code = gemini_interface(original_code.decode("utf-8")).encode("utf-8")
        zipped_accelerator_code = zip_src(accelerator_code)
    except Exception as e:
        print(f"Error: {e}")
        accelerator_code = original_code
        zipped_accelerator_code = zip_src(accelerator_code)
    
    code_list = [original_code, accelerator_code, zipped_original_code, zipped_accelerator_code]
    best_code = min(code_list, key=lambda x: len(x))
    
    open(f"{output_dir}/task{task_index:03d}.py", "wb").write(best_code)
    
    score = max(1, 2500-len(best_code))
    save = len(original_code) - len(best_code)
    return score, save

def compress_code_wrapper(args):
    return compress_code(*args)

def main(input_dir, output_dir, task_index_list):
    total_score, total_save = 0, 0
    os.makedirs(output_dir, exist_ok=True)
    
    # processing pool
    with Pool(processes=8) as pool:
        args_iter = ((input_dir, output_dir, task_index) for task_index in task_index_list)
        for score, save in tqdm(pool.imap(compress_code_wrapper, args_iter), total=len(task_index_list)):
            total_score += score
            total_save += save
    
    print(f"Total Score: {total_score}")
    print(f"Total Save: {total_save}")

if __name__ == "__main__":
    input_dir = "./kaggle/submission_v1"
    output_dir = "./kaggle/submission_v2"
    
    args = argparse.ArgumentParser()
    args.add_argument("--task_index_list", type=str, default=None)
    args = args.parse_args()
    
    if args.task_index_list is not None:
        task_index_list = list(map(int, args.task_index_list.split(",")))
    else:
        task_index_list = list(range(1, 401))
        
    main(input_dir, output_dir, task_index_list)