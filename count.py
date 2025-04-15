import os

def count_lines_in_py_files(directory):
    total_lines = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    total_lines += sum(1 for _ in f)
    return total_lines

# Replace this with the path to your "Project Code" directory
project_code_path = r"c:\Users\amcgl\Documents\W2025\Senior Project\Project Code"
total_lines = count_lines_in_py_files(project_code_path)
print(f"Total number of lines in all .py files: {total_lines}")