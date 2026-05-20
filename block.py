class Block:
    def __init__(self, x, y, scale, color):
        self.scale = scale
        self.color = color
        self.x, self.y = (x // scale) * scale, (y // scale) * scale