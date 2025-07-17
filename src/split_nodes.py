# split_nodes.py
import re

from src.extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        if node.text.count(delimiter) % 2 != 0:
            raise SyntaxError(f'Invalid markdown')

        strings = node.text.split(delimiter)
        for i, string in enumerate(strings):
            if i % 2 == 0:
                new_nodes.append(TextNode(string, TextType.TEXT))
            else:
                new_nodes.append(TextNode(string, text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        for image in images:
            first, second = text.split(f"![{image[0]}]({image[1]})")
            if first:
                new_nodes.append(TextNode(first, TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            text = second
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        for link in links:
            first, second = text.split(f"[{link[0]}]({link[1]})")
            if first:
                new_nodes.append(TextNode(first, TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            text = second
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text: str):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
