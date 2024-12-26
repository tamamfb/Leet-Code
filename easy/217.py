from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set()

        for bil in nums:
            if bil in a:
                return True
            else:
                a.add(bil)
        return False