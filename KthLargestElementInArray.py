# Kth Largest Element in an Array
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #implement a priority queue
        min_heap = []
        for num in nums:
            #insert each element into the min heap
            heapq.heappush(min_heap, num)
            #reached the kth largest element, root=min
            if len(min_heap) > k:
                #delete min until root is kth largest
                heapq.heappop(min_heap)
        return min_heap[0]
        