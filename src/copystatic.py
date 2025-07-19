import os
import shutil

from markdown_blocks import markdown_to_html_node, extract_title


def copy_files_recursive(src, dest):
    if not os.path.isdir(dest):
        os.mkdir(dest)

    for filename in os.listdir(src):
        from_path = os.path.join(src, filename)
        dest_path = os.path.join(dest, filename)
        if os.path.isfile(from_path):
            shutil.copyfile(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        from_str = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template_str = f.read()
    html = markdown_to_html_node(from_str).to_html()
    title = extract_title(from_str)
    template_str = template_str.replace("{{ Title }}", title).replace("{{ Content }}", html)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(template_str)

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str):
    for entry in os.listdir(dir_path_content):
        if entry.endswith(".md"):
            generate_page(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, entry))
        else:
            copy_files_recursive(os.path.join(dir_path_content, entry), os.path.join(dest_dir_path, entry))
