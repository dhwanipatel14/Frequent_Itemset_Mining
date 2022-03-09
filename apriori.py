import argparse
from asyncore import read
import datetime

class Apriori:
    def __init__(self, inputFile = None,dataChunk =100, support = 10 ):
        self.inputFile = inputFile
        self.dataChunk = dataChunk
        self.support = support

    def fileLength(self):
        with open(self.inputFile) as file:
            for i, _ in enumerate(file):
                pass
        
        return i + 1

    #getter
    def support(self):
        return self._support
    
    #setter
    def support(self, s):
        self._support = int((s*self.dataChunk)//100)

    
    def dataChunk(self):
        return self._dataChunk
    
    def dataChunk(self, data):
        buckets = self.fileLength()
        self._dataChunk = int((data*buckets)//100)

    def runApriori(self):
        start_time = datetime.datetime.now()    
        item_count = self.itemCount()                                    # Pass one to find the frequent count
        frequent_items = self.frequentItemCount(item_count)             # List of items which are frequent which we then use in second pass
        candidate_pair_count = self.getAllPairs(frequent_items)  # Second pass to find candidate pair
        frequent_item_set = self.frequentPairs(candidate_pair_count)   # frequent pairs 
        
        end_time = datetime.datetime.now()                                    # Stop Calculating time

        time_diff = (end_time - start_time)
        execution_time = time_diff.total_seconds() * 1000                     # Total time required for execution 
        
        total_candidate_pairs = len(candidate_pair_count)
        total_frequent_pair = len(frequent_item_set)
        print("Total candidate pairs: ", total_candidate_pairs)
        print("Total frequent pairs: ", total_frequent_pair)
        print("Total false positives: ", total_candidate_pairs - total_frequent_pair)
        print("runtime: ", round(execution_time, 2))
        print("-----------------------------------------------------")

    def readData(self):
        
        with open(self.inputFile, "r", newline="") as f:
            for i in range(1, self.dataChunk + 1):
                bucket = f.readline
                bucket = bucket.strip().split()
                print(bucket)
                if i == 10:
                    break
            yield frozenset(bucket)

    def itemCount(self):
        data = self.readData()
        count ={}
        for bucket in data:
            for item in bucket:
                first_item = frozenset([item])
                count[first_item] = count.get(first_item,0) + 1
        
        return count
    
    def frequentItemCount(self, items_count):

        frequentItems = []

        for item, count in items_count.items() :
            if count >= self.support:
                item = list(item)
                frequentItems.append(item[0])
        
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
                          pair = frozenset([bucket[i]], bucket[j])
                          count[pair] = count.get(pair, 0) + 1
        

        return count

    
    def frequentPairs(self, allPairs):
        frequentItems = {}
        for pair, count in allPairs.items():
            if count >= self.support_threshold:
                frequentItems[pair] = count
        
        return frequentItems

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process the data')
    parser.add_argument('-f', dest='data_file', default=None, help='Name of the file containing the data')
    parser.add_argument('-d', dest='dataChunk', default=100, help='% of data/buckets you would want to run apriory on(default=100%)')
    parser.add_argument('-t', dest='support', default=10, help='Support Threshold in terms of percentage(default=10%)')

    args = parser.parse_args()
    inputFile = args.data_file
    dataChunk = float(args.dataChunk)
    support = float(args.support)

    if inputFile is None:
        inputFile = input("Enter the data file name: ")

    apriori = Apriori(inputFile, dataChunk, support)
    apriori.runApriori()



    
