import argparse
from asyncore import read
import datetime

class Apriori:
    def __init__(self, inputFile, dataChunk, support ):
        self.inputFile = inputFile
        self.dataChunk = dataChunk
        self.support = support

    def fileLength(self):
        with open(self.inputFile) as file:
            for i, _ in enumerate(file):
                pass
        print("File length: {}", i)
        return i + 1

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

    def runApriori(self):
        start_time = datetime.datetime.now()    
        item_count = self.itemCount()                                    
        frequent_items = self.frequentItemCount(item_count)             # List of items which are frequent which we then use in second pass
        pairs_count = self.getAllPairs(frequent_items)  # Second pass to find candidate pair
        frequent_item_set = self.frequentPairs(pairs_count)   # frequent pairs 
        
        end_time = datetime.datetime.now()                                    # Stop Calculating time

        time_diff = (end_time - start_time)
        execution_time = time_diff.total_seconds() * 1000                     # Total time required for execution 
        
        total_candidate_pairs = len(pairs_count)
        total_frequent_pair = len(frequent_item_set)
        print("-----------------------------------------------------")
        print("Total items", len(item_count))
        print("Total candidate pairs: ", total_candidate_pairs)
        print("Total frequent pairs: ", total_frequent_pair)
        print("Total false positives: ", total_candidate_pairs - total_frequent_pair)
        print("runtime: ", round(execution_time, 2))
        print("-----------------------------------------------------")


    def itemCount(self):
        data = self.readData()
        count = {}
        for bucket in data:
            for item in bucket:
                first_item = frozenset([item])
                count[first_item] = count.get(first_item,0) + 1
        #print("Count : ", count)
        return count
    
    def frequentItemCount(self, item_count):

        frequentItems = []

        for item, count in item_count.items() :
            if count >= self.support:
                item = list(item)
                frequentItems.append(item[0])
        #print("FREQUENT: ", frequentItems)
        return frequentItems
    
    def getAllPairs(self, frequentItems):
        data = self.readData()

        count = {}

        for bucket in data:
            bucket = list(bucket)
            length = len(bucket)
            for i in range(length - 1):
                if bucket[i] in frequentItems : 
                    for j in range(i+1, length):
                        if bucket[j] in frequentItems:
                          pair = frozenset([bucket[i], bucket[j]])
                          count[pair] = count.get(pair, 0) + 1
        
        #print("ALLPairs: ", count)
        return count

    
    def frequentPairs(self, allPairs):
        frequentItems = {}
        for pair, count in allPairs.items():
            if count >= self.support:
                frequentItems[pair] = count
        #print("FrequentPairs: ", frequentItems)
        return frequentItems

    def readData(self):
        with open(self.inputFile, "r", newline="") as f:
            for i in range(1, self.dataChunk + 1):
                bucket = f.readline()
                bucket = bucket.strip().split()
                yield frozenset(bucket)

if __name__ == '__main__':
   
    inputFile = input("Enter the data file name: ")
    val = 1
    dataChunk = 10
    support = 10
    apriori = Apriori(inputFile, dataChunk, support)
    apriori.runApriori()



    
