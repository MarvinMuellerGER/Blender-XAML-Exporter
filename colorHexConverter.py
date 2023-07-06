class ColorHexConverter:
    def __init__(self):
        self.predefined_colors = {
            (1.0, 1.0, 1.0): 'White',
            (0.0, 0.0, 0.0): 'Black',
            (1.0, 0.0, 0.0): 'Red',
            (0.0, 1.0, 0.0): 'Green',
            (0.0, 0.0, 1.0): 'Blue',
        }

    def getColorHex(self, color):
        if tuple(color) in self.predefined_colors:
            return self.predefined_colors[tuple(color)]
        else:
            return '#%02X%02X%02X' % (int(color[0]*255), int(color[1]*255), int(color[2]*255))