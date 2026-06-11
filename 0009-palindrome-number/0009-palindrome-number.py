class Solution(object):
    def isPalindrome(self, x):
        if(x<0):
            return False
        
        reverse = 0    # store reverse value
        xcopy  = x     # make copy of original value

        while(x>0):
            reverse = (reverse * 10 ) + (x % 10)            # reverse 
            x//=10                                          # remove last element

        return reverse == xcopy
        