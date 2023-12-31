# 3) Write a Python class to get all possible unique subsets from a set of distinct integers Input : [4, 5, 6] Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]] 

class SubsetGenerator:
    def __init__(self, nums):
        self.nums = nums
        self.subsets = []

    def generate_subsets(self):
        self._generate([], 0)
        return self.subsets

    def _generate(self, current_subset, index):
        self.subsets.append(current_subset[:])

        for i in range(index, len(self.nums)):
            current_subset.append(self.nums[i])
            self._generate(current_subset, i + 1)
            current_subset.pop()

if __name__ == "__main__":
    input_nums = [4, 5, 6]
    subset_generator = SubsetGenerator(input_nums)
    result = subset_generator.generate_subsets()
    print(result)


