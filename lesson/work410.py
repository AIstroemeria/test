class FileObject:
    def __init__(self,name,mod = 'r'):
        self.name = name
        self.f = open(self.name,mod)

    def __del__(self):
        self.f.close()
