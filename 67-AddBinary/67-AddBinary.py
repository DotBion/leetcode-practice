# Last updated: 7/29/2025, 5:48:37 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        return str(bin(int(a,2)+int(b,2)))[2:]