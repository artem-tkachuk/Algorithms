#!/bin/python3

import math
import os
import random
import re
import sys


from copy import deepcopy
#
# Complete the 'getItems' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts 2D_STRING_ARRAY entries as parameter.
#
class MinHeap:
    def __init__(self):
        self.__heap = []
    
    """ INTERNAL API """    
    def __siftUp(self, index):
        if 0 < index < self.getSize():
            parentIndex = (index - 1) // 2  # floor division
            
            # if price of parent > price of current OR prices are equal and name is greater
            while index > 0 and (self.__heap[parentIndex][1] > self.__heap[index][1] or 
                (self.__heap[parentIndex][1] == self.__heap[index][1] and 
                    self.__heap[parentIndex][0] > self.__heap[index][0])):
                
                self.swap(parentIndex, index, self.__heap)
                index = parentIndex
                parentIndex = (index - 1) // 2  # floor division
                    
    
    def __siftDown(self, index):
        if index >= 0:
            n = self.getSize()
            c1_idx = 2 * index + 1
            
            while c1_idx < n:
                c2_idx = c1_idx + 1 # child2_idx = 2 * index + 2
                
                min_child_idx = c1_idx \
                    if (c2_idx >= n or 
                        (self.__heap[c1_idx][1] < self.__heap[c2_idx][1] or 
                            (self.__heap[c1_idx][1] == self.__heap[c2_idx][1] and self.__heap[c1_idx][0] < self.__heap[c2_idx][0]))) \
                    else c2_idx
                
                
                # if price <= min child or prices are equal and name < min child name
                if (self.__heap[index][1] <= self.__heap[min_child_idx][1]) or \
                    (self.__heap[index][1] == self.__heap[min_child_idx][1] and self.__heap[index][0] <= self.__heap[min_child_idx][0]): 
                    break
                else:
                    self.swap(index, min_child_idx, self.__heap)
                    index = min_child_idx
                    c1_idx = 2 * index + 1
                
                
    
    """ EXTERNAL API """
    def insert(self, entry):
        self.__heap.append(entry)
        self.__siftUp(self.getSize() - 1)
    
    def removeRoot(self):
        # will always be able to do a swap since guarantted that k <= size of db
        self.swap(0, self.getSize() - 1, self.__heap)
        removed_elem = self.__heap.pop()
        self.__siftDown(0)
        return removed_elem
    
    def peek(self):
        return self.__heap[0]
    
    def getSize(self):
        return len(self.__heap)
    
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

        
def getItems(entries):
    # Write your code here
    outputs = []
    heap = MinHeap()
    k = 0
    
    for entry in entries:
        # It is guaranteed that at least one item 
        # is added to the database before user views for the first time
        if entry[0] == "VIEW":
            temp_heap_holder = []
            # Remove k cheapest elements from the top of the heap
            for _ in range(k):
               current_cheapest = heap.removeRoot()
               temp_heap_holder.append(current_cheapest)  
            # append the actual item name to array of outputs
            item, price = heap.peek()   
            outputs.append(item)
            # Return the removed elements because we want the entire database
            for entry in temp_heap_holder:
                heap.insert(entry)
            # Increment to respect the k-th item property
            k += 1
            
        else:  # entry[0] == "INSERT"
            itemname, price = entry[1], int(entry[2])
            heap.insert((itemname, price))
            
    # return all the results for running VIEW
    return outputs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    entries_rows = int(input().strip())
    entries_columns = int(input().strip())

    entries = []

    for _ in range(entries_rows):
        entries.append(input().rstrip().split())

    result = getItems(entries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
