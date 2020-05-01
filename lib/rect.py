class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x2 = x + width
        self.y2 = y + height

    @property
    def center(self):
        return self.x + round(self.width / 2), self.y + round(self.height / 2)

    def include(self, other):
        return self.x < other.x and self.y < other.y and self.x2 > other.x2 and self.y2 > other.y2

    def __lt__(self, other):
        """Using "reading order" in a coordinate system where 0,0 is bottom left"""
        try:
            x0, y0 = self.center
            x1, y1 = other.center
            return ((y0 * 10) + x0) < ((y1 * 10) + x1)
        except AttributeError:
            return NotImplemented

    def __repr__(self):
        return 'Rec: ' + str(self.x) + ':' + str(self.y)
