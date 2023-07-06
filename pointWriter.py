class PointWriter:
    def __init__(self, writer):
        self.writer = writer

    def write(self, x, y, z):
        self.writer.write(f'{x},{y},{z}')