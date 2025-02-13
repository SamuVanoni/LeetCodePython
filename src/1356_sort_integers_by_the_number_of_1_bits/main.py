class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Define a custom comparison key function for sorting
        def custom_sort_key(num):
            bit_count = bin(num).count('1')
            # First order the amount of numbers '1's in binaries, then the original number
            return (bit_count, num)

        # Sort the input list using the custom comparison key function
        arr.sort(key=custom_sort_key)

        return arr