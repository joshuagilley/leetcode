class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # stack solution
        stack = []
        for char in s:
            stack.append(char)

        for char in reversed(t):
            if (len(stack) > 0 and stack[len(stack) - 1] == char):
                stack.pop()

        return len(stack) == 0

if __name__ == "__main__":
	sol = Solution()
	result = sol.isSubsequence("hlo", "hello")
	print(result)

'''
NOTES:
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


My solution here was to use stacks. 
	• Push characters of subsequence to stack
	• Reverse compare string and pop from stack when finding valid value
	• The result:
		○ If the stack is empty, it is in order, and every value was accounted for
		○ If it is NOT empty, the it is not a valid subsequence

O(n)
Beats 100% runtime in leetcode
'''
