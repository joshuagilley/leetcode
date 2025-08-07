class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #return bin(int(a, 2) + int(b, 2))[2:]
        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))): # range of longer string
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB =  ord(b[i]) - ord("0") if i < len(b) else 0
            total = digitA + digitB + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2
        if carry: 
            res = "1" + res
        return res

if __name__ == "__main__":
    sol = Solution()
    result = sol.addBinary("1010", "1011")
    print(result)  # Output should be "10101"

'''
NOTES:
	* Best Solution: Solution two but using a list and reversing at the end
	* In solution 2, we are appending a character to the front of a string
	* But in python, strings are immutable. So every time you add a character, python
has to create a new string, copy over characters and reassign the result
	*  Doing this in the loop can result in O(n^2) time complexity
Use a list instead
'''
