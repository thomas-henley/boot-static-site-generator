import unittest

from htmlnode import HTMLNode
from src.textnode import TextType, TextNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "Welcome to the site", props={"style": "font-family: sans-serif;"})
        expected = '<p> Welcome to the site\n<style> \"font-family: sans-serif;\"\n'
        self.assertEqual(str(node), expected)

    def test_props_to_html(self):
        prop_arg = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        node = HTMLNode(
            "p",
            "Welcome to the site",
            props = prop_arg,
        )
        expected =  ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)