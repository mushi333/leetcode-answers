class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert to str
        str_x = str(x)
        
        # Start from both the left and right side
        for i in range(len(str_x)):
            left_val = str_x[i]
            right_val = str_x[len(str_x) - (1 + i)]

            # if left and right side incremented I value is the same, return true
            if i == len(str_x) - (1 + i):
                return True

            # If both sides have the same value and the difference of 1 for i, return true
            if abs(len(str_x) - (1 + i)) - abs(i) == 1 and left_val == right_val:
                return True
            
            # Check to see if left val is the same as right val, if it is not, return false
            if left_val != right_val:
                return False

            # Increment i so that left val goes right and right val goes left


if __name__ == '__main__':
    new_sol = Solution()
    print(new_sol.isPalindrome(112211))
    exit() 