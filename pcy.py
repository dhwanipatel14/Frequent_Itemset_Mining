
from textwrap import indent


class pcy:
    def __init__(self, inputFile, dataChunk, support) :
        self.inputFile = inputFile
        self.dataChunk = dataChunk
        self.support = support
    

    def fileLength(self):
        with open(self.inputFile) as file:
            for i, _ in enumerate(file):
                pass
        #print("File length: {}", i)
        return i + 1

    def readData(self):
        with open(self.inputFile, "r", newline="") as f:
            for i in range(1, self.dataChunk + 1):
                bucket = f.readline()
                bucket = bucket.strip().split()
                yield frozenset(bucket)
    
     #getter
    @property
    def support(self):
        return self._support
    
    #setter
    @support.setter
    def support(self, s):
        self._support = int((s*self.dataChunk)//100)

    @property
    def dataChunk(self):
        return self._dataChunk

    @dataChunk.setter
    def dataChunk(self, data):
        buckets = self.fileLength()
        self._dataChunk = int((data*buckets)//100)

   

    def first_pass(self):
        data = self.readData()
        count = {}
        buckets = {}
        for bucket in data:
            for item in bucket:
                singleton = frozenset([item])
                count[singleton] = count.get(singleton,0) + 1
        #print("Count : ", count)

            bucketsLen = len(bucket)
            for i in range(bucketsLen - 1):
                for j in range(i+1,bucketsLen):
                    index = (int(bucket[i]), int(bucket[j]))
                    buckets[index] = buckets.get(index, 0) + 1
        
        frequentItems = self.frequentItemCount(count)

        return frequentItems, buckets
        
    
    def frequentItemCount(self, item_count):

        frequentItems = []

        for item, count in item_count.items() :
            if count >= self.support:
                item = list(item)
                frequentItems.append(item[0])
        #print("FREQUENT: ", frequentItems)
        return frequentItems

    def hashFunction(num1, num2):
        return (num1*num2) % 5434

    


        


