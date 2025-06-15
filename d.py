import os

def list_directory_structure(root_dir, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            depth = dirpath.replace(root_dir, "").count(os.sep)
            indent = "  " * depth
            f.write(f"{indent}📁 {os.path.basename(dirpath)}\n")
            sub_indent = "  " * (depth + 1)
            for file in filenames:
                f.write(f"{sub_indent}📄 {file}\n")

# You are already in cbse_math_solver/
root_directory = "."  # current folder
output_txt = "directory_structure.txt"

list_directory_structure(root_directory, output_txt)
print(f"✅ Directory structure saved to {output_txt}")
