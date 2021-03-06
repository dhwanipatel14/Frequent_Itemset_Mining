import argparse
from datetime import datetime
from textwrap import indent


class Pcy:
    def __init__(self, inputFile, dataChunk=40, support=1) :
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
                yield frozenset(bucket)                      # Making sure that the bucket only have unique items and bucket can not be modified(immutable)
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

   
    def firstPass(self):  

    #   I used frozenset to represent a pair {i, j} instead of list or set since in hashmap can not have mutable key
        data = self.readData()
        count = {}
        buckets = {}
        for bucket in data:
            bucket = list(bucket)
            for item in bucket:
                singleton = frozenset([item])
                count[singleton] = count.get(singleton,0) + 1

            bucketsLen = len(bucket)
            for i in range(bucketsLen - 1):
                for j in range(i+1,bucketsLen):
                    index = hashFunction(int(bucket[i]),int(bucket[j]))
                    buckets[index] = buckets.get(index, 0) + 1
        
        frequentItems = self.frequentItemCount(count)
        # print("frequentItems : ", frequentItems)
        # print("buckets: ", buckets)
        return frequentItems, buckets
        
    def frequentItemCount(self, item_count):

        frequentItems = []

        for item, count in item_count.items() :
            if count >= self.support:
                item = list(item)
                frequentItems.append(item[0])
        # print("FREQUENT: ", frequentItems)
        return frequentItems

    def secondPass(self, frequentItems, map):
        data = self.readData()

        count = {}

        for bucket in data:
            bucket = list(bucket)
            length = len(bucket)
            for i in range(length - 1):
                if bucket[i] in frequentItems : 
                    for j in range(i+1, length):
                        if bucket[j] in frequentItems:
                            if map[hashFunction(int(bucket[i]),int(bucket[j]))%5432] == 1:
                                pair = frozenset([bucket[i], bucket[j]])
                                count[pair] = count.get(pair, 0) + 1
        
        # print("ALLPairs: ", count)
        return count

    def frequentPairs(self, allPairs):
            frequentItems = {}
            for pair, count in allPairs.items():
                if count >= self.support:
                    frequentItems[pair] = count
            #print("\n\n\nFrequentPairs: ", frequentItems)
            return frequentItems

    def runPcy(self):
        start_time = datetime.now()

        frequentItems , buckets = self.firstPass()
        mapValues(buckets, self.support)
        candidatePairs = self.secondPass(frequentItems, buckets)
        frequentItemSet = self.frequentPairs(candidatePairs)

        end_time = datetime.now()                             # Total time required for execution

        time_diff = (end_time - start_time)
        execution_time = time_diff.total_seconds() * 1000
        
        total_candidate_pairs = len(candidatePairs)
        total_frequent_pair = len(frequentItemSet)
        print("Total candidate pairs: ", total_candidate_pairs)
        print("Total frequent pairs: ", total_frequent_pair)
        print("Total false positives: ", total_candidate_pairs - total_frequent_pair)
        print("runtime: ", round(execution_time, 2))
        print("-----------------------------------------------------") 

        return execution_time


def mapValues(hashTable, support):
    for key, value in hashTable.items():
        if value < support:
            hashTable[key] = 0
        else:
            hashTable[key] = 1

def hashFunction( num1, num2):
    return (num1*num2) % 5434

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process the data')
    parser.add_argument('-f', dest='inputFile', default=None, help='Name of the file containing the data')
    parser.add_argument('-d', dest='dataChunk', default=100, help='% of data/buckets you would want to run apriory on(default=100%)')
    parser.add_argument('-t', dest='supportThreshold', default=10, help='Support Threshold in terms of percentage(default=10%)')

    args = parser.parse_args()
    inputFile = args.inputFile
    dataChunk = float(args.dataChunk)
    support = float(args.supportThreshold)

    
    input_file = input("Enter the data file name: ")
    
    pcy = Pcy(input_file, dataChunk, support)
    pcy.runPcy()

    # chunks = [10, 50, 100]
    # threshold = [1, 5, 10]
    # exe_time = []

    # for i in threshold:
    #     for j in chunks:
    #         pcy = Pcy("retail.txt", j, i)
    #         exe_time.append(pcy.runPcy())
    # # print(exe_time)
