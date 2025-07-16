import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.example.com")
        expected = "TextNode(This is a text node, TextType.BOLD, www.example.com)"
        self.assertEqual(repr(node), expected)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.example.com")
        self.assertEqual(node, node2)

    def test_eq_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.sample.com")
        self.assertNotEqual(node, node2)

if __name__ == '__main__':
    unittest.main()
