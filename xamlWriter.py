from io import StringIO

class XamlWriter:
    def __init__(self):
        self.outfile = StringIO()
    
    def toString(self):
        return self.outfile.getvalue()

    def write(self, str):
        self.outfile.write(str)