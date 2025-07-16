class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError()

    def props_to_html(self) -> str:
        prop_str = ''
        if self.props:
            for k,v in self.props.items():
                prop_str += f' {k}=\"{v}\"'
        return prop_str

    def __repr__(self):
        string = ''
        string += f'<{self.tag}> {self.value}\n'
        if self.children:
            for child in self.children:
                string += f'<{child.tag}> {child.value}\n'
        if self.props:
            for k,v in self.props.items():
                string += f'<{k}> "{v}"\n'
        return string

class LeafNode(HTMLNode):
    def __init__(self, tag: str or None, value: str, props: dict = None):
        super().__init__(tag, value, children = None, props = props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value

        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("Missing tag in ParentNode")
        if not self.children:
            raise ValueError("Missing children in ParentNode")

        res = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            res += child.to_html()
        res += f'</{self.tag}>'

        return res
