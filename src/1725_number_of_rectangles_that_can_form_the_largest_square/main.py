class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        len_arr = [min(rectangle) for rectangle in rectangles]
        print(len_arr) # [5, 3, 5, 5]
        return len_arr.count(max(len_arr))