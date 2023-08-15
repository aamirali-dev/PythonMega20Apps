from enum import Flag, auto


# | (OR) Union or Combination
# & (AND) Intersection
# ~ (NOT) everything except
# ^ (XOR) in one or the other but not both


class Style(Flag):
    ITALIC = auto()
    BOLD = auto()
    UNDERLINE = auto()
    SUPERSCRIPT = auto()
    SUBSCRIPT = auto()


class TextStyleSet:
    def __init__(self, *styles):
        self._text_styles = Style(0)

        for style in styles:
            self._text_styles |= style

    def __repr__(self):
        return f'{type(self).__name__}({self._text_styles})'

    def __add__(self, other):
        if isinstance(other, Style):
            self._text_styles |= other
            return self
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Style):
            self._text_styles & (~other)
            return self
        return NotImplemented

    def __contains__(self, item):
        if isinstance(item, Style):
            return self._text_styles & item
