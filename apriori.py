import this

class Apriori_algo:
    def __init__(self, inputFile = None,dataChunk =100, support = 10 ):
        self.inputSize = inputFile
        self.dataChunk = dataChunk
        self.support = support

    def fileLength(self):
        with open(self.inputFile) as file:
            for i in enumerate(file):
                pass
        
        return i + 1

    #getter
    def support(self):
        return self.support
    
    #setter
    def support(self, s):
        this.support = int((s*self.dataChunk)//100)

    
    def dataChunk(self):
        return self.dataChunk
    
    def dataChunk(self, data):
        buckets = self.fileLength()
        self.dataChunk = int((data*buckets)//100)
    
    def readData(self):
        with open(self.inputFile, "r", newline="") as f:
            bucket = f.readline
            bucket = bucket.strip().split()

    

    
