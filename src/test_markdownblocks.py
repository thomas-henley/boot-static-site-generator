import unittest

from blocks import *

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        md1 = "# heading 1"
        md6 = "###### heading 6"
        md7 = "####### heading 7"
        p1 = "this is a paragraph"
        p2 = "#this is another paragraph"
        self.assertEqual(BlockType.HEADING, block_to_block_type(md1))
        self.assertEqual(BlockType.HEADING, block_to_block_type(md6))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(md7))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(p1))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(p2))

    def test_block_to_block_type_code(self):
        c1 = "```This is a oneline code block```"
        c2 = "```This is a multi-line\ncode block.```"
        c3 = "```\nThis code block\nhas the ticks on their own lines\n```"
        p1 = "```This codeblock is unterminated"
        p2 = "``This codeblock doesn't have enough ticks``"
        self.assertEqual(BlockType.CODE, block_to_block_type(c1))
        self.assertEqual(BlockType.CODE, block_to_block_type(c2))
        self.assertEqual(BlockType.CODE, block_to_block_type(c3))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(p1))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(p2))

    def test_block_to_block_type_quote(self):
        q1 = ">This is a quote"
        q2 = "> This is another quote"
        q3 = "> This is\n> a multiline\n>quote"
        p1 = "> This is\nan invalid quote"
        self.assertEqual(BlockType.QUOTE, block_to_block_type(q1))
        self.assertEqual(BlockType.QUOTE, block_to_block_type(q2))
        self.assertEqual(BlockType.QUOTE, block_to_block_type(q3))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(p1))

    def test_block_to_block_type_unordered(self):
        u1 = "- this is a UL"
        u2 = "- this is a UL\n- with 2 lines"
        p1 = "-this is not a UL"
        p2 = "- this is not\n-a UL"
        p3 = "- this is not\na UL"
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(u1))
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(u2))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(p1))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(p2))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(p3))

    def test_block_to_block_type_ordered(self):
        o1 = "1. this is a OL\n2. this is the second line"
        o2 = "1. this is a OL"
        p1 = "1.this is not a OL"
        p2 = "1. this is a valid line\n2.this is not"
        p3 = "1. this is a valid line\nthis is not"
        p4 = "1. this is a valid line\n1. this is not"
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(o1))
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(o2))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(p1))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(p2))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(p3))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(p4))


