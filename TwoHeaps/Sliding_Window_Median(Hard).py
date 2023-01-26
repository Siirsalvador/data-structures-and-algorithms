import heapq
from heapq import *


class SlidingWindowMedian:

    def find_sliding_window_median(self, nums, k):
        result = [0.0 for i in range(len(nums) - k + 1)]
        self.cur_size = 0
        self.min_heap = []
        self.max_heap = []
        for i in range(len(nums)):
            if not self.max_heap or -self.max_heap[0] >= nums[i]:
                heappush(self.max_heap, -nums[i])
            else:
                heappush(self.min_heap, nums[i])
            self.cur_size += 1

            self.rebalance_heaps()

            if self.cur_size >= k:
                if len(self.max_heap) == len(self.min_heap):
                    result[i - k + 1] = -self.max_heap[0] / 2.0 + self.min_heap[0] / 2.0
                else:
                    result[i - k + 1] = -self.max_heap[0] / 1.0

                elementToBeRemoved = nums[i - k + 1]
                if elementToBeRemoved <= -self.max_heap[0]:
                    self.remove(self.max_heap, -elementToBeRemoved)
                else:
                    self.remove(self.min_heap, elementToBeRemoved)

                self.rebalance_heaps()

        return result

    @staticmethod
    def remove(heap, element):
        ind = heap.index(element)
        heap[ind] = heap[-1]
        del heap[-1]

        if ind < len(heap):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)

    def rebalance_heaps(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))


def main():
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
