import sys
sys.path.append("./kaggle/input/google-code-golf-2025/code_golf_utils")
from code_golf_utils import *

# Submission Compression
import zlib
import zipfile
import zopfli.zlib
from tqdm import tqdm
from zipfile import ZipFile

#https://www.kaggle.com/code/cheeseexports/big-zippa
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

def compress_submission(output_dir):
    # compress the folder into a zip file
    with zipfile.ZipFile(f"submission.zip", "w") as zipf:
        for file in os.listdir(output_dir):
            zipf.write(f"{output_dir}/{file}", file)
    print(f"Compressed {output_dir} -> [submission.zip]")
    
files = {}
total_save=0
input_dir = "./kaggle/submission_v1"
output_dir = "./kaggle/submission"
os.makedirs(output_dir, exist_ok=True)

# delete the existing submission.zip
if os.path.exists("submission.zip"):
    os.remove("submission.zip")
    print("[+] Deleted existing submission.zip")
    
print(f"[+] {input_dir} -> {output_dir}")

total_save = 0
total_score = 0

score_dict = {}

for task_index in tqdm(range(1, 401)):
    original_src = open(f'{input_dir}/task' + str(task_index).zfill(3) + '.py','rb').read().strip()
    zipped_src = zip_src(original_src)
    improvement = len(original_src) - len(zipped_src)
    
    score = 0
    if improvement > 0:
        total_save += improvement
        open(f'{output_dir}/task' + str(task_index).zfill(3) + '.py','wb').write(zipped_src)
        score = max(1, 2500-len(zipped_src))
    else:
        open(f'{output_dir}/task' + str(task_index).zfill(3) + '.py','wb').write(original_src)
        score = max(1, 2500-len(original_src))
    score_dict[task_index] = score
    total_score += score
    
print("[-] Total Save: ", total_save)
print("[-] Total Score: ", total_score)
print("================================================")

# Top-10 tasks
top_10_tasks = sorted(score_dict.items(), key=lambda x: x[1])[:10]
print("Top-10 Tasks:")
for task_index, score in top_10_tasks:
    print(f"[-] Task {task_index}: {score}")

print("[+] Compressing new submission.zip file...")
compress_submission(output_dir)