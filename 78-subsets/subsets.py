class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        def bt(remaining, bag) :
            
            if not remaining :
                res.append(bag[:])
                return 
            first = remaining[0]
            remaining = remaining[1:]
            bag.append(first)
            bt(remaining, bag)
            bag.pop()
            bt(remaining, bag)
        bt(nums,[])
        return res