import os

def export_all_file_contents(root_dir, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as file_content:
                        relative_path = os.path.relpath(file_path, root_dir)
                        f.write(f"\n### File: {relative_path} ###\n")
                        f.write(file_content.read())
                        f.write("\n" + "-"*80 + "\n")  # separator between files
                except Exception as e:
                    f.write(f"\n### File: {relative_path} ###\n")
                    f.write(f"[Error reading file: {e}]\n")
                    f.write("\n" + "-"*80 + "\n")

# Set root directory and output file
root_directory = "."  # current directory
output_txt = "all_file_contents.txt"

export_all_file_contents(root_directory, output_txt)
print(f"📄 All file contents saved to: {output_txt}")
