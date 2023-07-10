class FileWriter:
    def set_filepath_and_writer(self, filepath, writer):
        self.filepath = filepath
        self.writer = writer
    
    def open(self):
        self.file = open(self.filepath, "w", encoding="utf8")
    
    def write(self):
        self.file.write(self.writer.toString())
        
    def close(self):
        self.file.flush()
        self.file.close()
        
    def WriteAll(self):
        self.open()
        try:
            self.write()
        finally:
            self.close()