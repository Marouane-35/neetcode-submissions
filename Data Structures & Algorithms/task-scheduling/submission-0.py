from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_f = max(freq.values())
        max_count = sum(1 for count in freq.values() if count == max_f)
        
        return max(len(tasks), (max_f - 1) * (n + 1) + max_count)