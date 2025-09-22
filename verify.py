import sys
import shutil
from tqdm import tqdm
sys.path.append("./kaggle/input/google-code-golf-2025/code_golf_utils")
from code_golf_utils import *

total_passed = 0
total_score = 0
failed_tasks = []

submission_dir = "kaggle/submission"

for i in tqdm(range(1, 401)):
    try:
        passed = verify_program_lite(i, f"{submission_dir}/task{i:03d}.py", load_examples(i))
    except Exception as e:
        passed = False
        
    if passed:        
        total_passed += 1
        total_score += max(1, 2500-os.path.getsize(f"{submission_dir}/task{i:03d}.py"))
    else:
        print(f"Task {i} failed")
        failed_tasks.append(i)
    #     shutil.copy(f"kaggle/submission_vanilla/task{i:03d}.py", f"{submission_dir}/task{i:03d}.py")
    #     total_score += max(1, 2500-os.path.getsize(f"{submission_dir}/task{i:03d}.py"))

print(f"Total passed: {total_passed}")
print(f"Total score: {total_score}")
print(f"Failed tasks: {failed_tasks}")