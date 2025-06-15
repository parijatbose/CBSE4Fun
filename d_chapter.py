# File: cbse_math_solver/chapter_structure_extractor.py

import os

def write_line(f, indent_level, prefix, name):
    indent = "  " * indent_level
    f.write(f"{indent}{prefix} {name}\n")

def scan_directory(base_path, f, filter_keyword=None, indent_level=0):
    for dirpath, dirnames, filenames in os.walk(base_path):
        rel_dir = os.path.relpath(dirpath, base_path)
        if "__pycache__" in rel_dir or rel_dir.startswith("."):
            continue
        if filter_keyword and filter_keyword not in dirpath.lower():
            continue
        depth = rel_dir.count(os.sep) if rel_dir != "." else 0
        write_line(f, indent_level + depth, "📁", os.path.basename(dirpath))
        for file in sorted(filenames):
            if file.endswith((".py", ".json", ".txt", ".md", ".pdf")):
                write_line(f, indent_level + depth + 1, "📄", file)

def find_matching_chapter_folder(base_path, keyword):
    """
    Find the full folder name under 'chapters/' that matches the chapter keyword (e.g., chapter12)
    """
    chapters_path = os.path.join(base_path, "chapters")
    for name in os.listdir(chapters_path):
        if keyword in name.lower() and os.path.isdir(os.path.join(chapters_path, name)):
            return name
    return None

def generate_chapter_structure(chapter_num: str):
    root_dir = "."
    chapter_keyword = f"chapter{chapter_num}"

    output_file = f"{chapter_keyword}_structure.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# Structure for {chapter_keyword}\n\n")

        # 1. Root files
        f.write("📁 Root Files in cbse_math_solver\n")
        for item in sorted(os.listdir(root_dir)):
            if os.path.isfile(item) and item.endswith((".py", ".txt", ".md", ".env")):
                write_line(f, 1, "📄", item)
        f.write("\n")

        # 2. topic_handlers
        topic_dir = os.path.join(root_dir, "topic_handlers")
        f.write("📁 topic_handlers (filtered)\n")
        scan_directory(topic_dir, f, filter_keyword=chapter_keyword)

        # 3. utils
        utils_dir = os.path.join(root_dir, "utils")
        f.write("\n📁 utils (filtered)\n")
        scan_directory(utils_dir, f, filter_keyword=chapter_keyword)

        # 4. chapters
        matched_folder = find_matching_chapter_folder(root_dir, chapter_keyword)
        if matched_folder:
            chapter_dir = os.path.join(root_dir, "chapters", matched_folder)
            f.write(f"\n📁 chapters/{matched_folder}\n")
            scan_directory(chapter_dir, f)
        else:
            f.write(f"\n⚠️ Folder chapters/*{chapter_keyword}* not found\n")

    print(f"✅ Structure saved to: {output_file}")


# === MAIN ===
if __name__ == "__main__":
    chapter_input = input("Enter chapter number (e.g., 12 for chapter12_surface_areas_and_volumes): ").strip()
    if not chapter_input.isdigit():
        print("❌ Invalid chapter number")
    else:
        generate_chapter_structure(chapter_input)
