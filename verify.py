import sys
import shutil
import argparse
from tqdm import tqdm
sys.path.append("./kaggle/input/google-code-golf-2025/code_golf_utils")
from code_golf_utils import *

total_passed = 0
total_score = 0
failed_tasks = []

args = argparse.ArgumentParser()
args.add_argument("--dir", type=str, default="kaggle/submission")
args.add_argument("--full", action='store_true')
args.add_argument("--task_index", type=int, default=None)
args = args.parse_args()

print(f"[+] Current submission directory: {args.dir}")
print(f"[-] Current task index: {args.task_index}") if args.task_index is not None else print(f"[-] Running all tasks {'(full)' if args.full else '(lite)'}")
test_index_list = [args.task_index] if args.task_index is not None else list(range(1, 401))

if not args.full and args.task_index is None:
    # Time-consuming tasks
    test_index_list.remove(18)
    test_index_list.remove(23)
    test_index_list.remove(157)
    test_index_list.remove(158)
    test_index_list.remove(173)

for i in tqdm(test_index_list):
    try:
        passed = verify_program_lite(i, f"{args.dir}/task{i:03d}.py", load_examples(i))
    except Exception as e:
        passed = False
        
    if passed:        
        total_passed += 1
        total_score += max(1, 2500-os.path.getsize(f"{args.dir}/task{i:03d}.py"))
    else:
        print(f"Task {i} Failed...")
        # shutil.copy(f"kaggle/original/task{i:03d}.py", f"{args.dir}/task{i:03d}.py")
        failed_tasks.append(i)
    
print(f"Total passed: {total_passed}")
print(f"Total score: {total_score}")
print(f"Failed tasks: {failed_tasks}")