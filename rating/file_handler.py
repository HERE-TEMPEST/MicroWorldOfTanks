class FileHandler:
    def __init__(self, reader, writer):
        self.writer = writer
        self.reader = reader
        self.source = ""

    def update_resource(self, source):
      self.source = source
    
    def read_from_source(self):
      return self.reader.read_from_source(self.source)

    def update_source(self, path, data):
      self.writer.update_source(path, data)