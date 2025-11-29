# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        

        def check(font):
            if fontInfo.getHeight(font) > h:
                return False
            width = 0
            for ch in text:
                width += fontInfo.getWidth(font, ch)
                if width > w:
                    return False
            return True
        
        n = len(fonts)
        low = 0
        high = n - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if check(fonts[mid]):
                ans = fonts[mid]
                low = mid + 1
            else:
                high = mid - 1
        return ans

