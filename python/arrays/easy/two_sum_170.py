class TwoSum:
    def __init__(self):
        self.arr = []
    def add(self, number: int) -> None:
        self.arr.append(number)
    def find(self, value: int) -> bool:
        seen = set()
        for num in self.arr:
            if value - num in seen:
                return True
            seen.add(num)
        return False

if __name__ == "__main__":
	two = TwoSum()
	two.add(2)
	print(two.find(2))


'''
NOTES:

Solution
Create a set and loop through the arr running valueOfINterest - arr[i] and see if that is in seen. O(1) because a set is a no duplicates hashmap checking for the EXISTANCE of the value in question
'''
