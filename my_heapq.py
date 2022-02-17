import heapq


class word:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq


nums = []

heapq.heappush(nums, word("1", 3))
heapq.heappush(nums, word("2", 1))
heapq.heappush(nums, word("3", -3))

for i in range(len(nums)):
    print(heapq.heappop(nums).freq)
