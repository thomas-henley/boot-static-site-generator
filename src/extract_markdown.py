import re

def extract_markdown_images(text: str) -> list[tuple]:
        res = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
        return res

def extract_markdown_links(text: str) -> list[tuple]:
        res = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
        return res