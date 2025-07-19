import os
import shutil
import sys

from copystatic import copy_files_recursive, generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_docs = "./docs"

def main():
    basepath = sys.argv[1] or "/"

    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    copy_files_recursive(dir_path_static, dir_path_docs)

    generate_pages_recursive("./content", "template.html", dir_path_docs, basepath)


main()
