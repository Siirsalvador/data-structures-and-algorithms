class Solution:
    def is_power_of_two(self, num: int) -> bool:
        """
        Takes in a positive integer and returns
        true if it is a power of two, else false.
        :param num: Integer to test.
        :return: True if the number is a power of two, false otherwise.
        """
        return not bool(num & (num - 1))
