class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        num_str = str(x)
        half_len = len(num_str) // 2
        half_str = num_str[:half_len]
        reversed_tail = num_str[-half_len:][::-1]
        return reversed_tail == half_str

list_true = [0, 1, 2, 3, 11, 22, 33, 121, 131, 535, 555, 777, 4444, 1111, 1221, 4224]
list_false = [12, 21, 34, 43, 112, 221, 4222, 1114, -123, -442, -1, -2]

if __name__ == "__main__":
    s = Solution()
    print('Traverse list_true')
    for i in list_true:
        result = s.isPalindrome(i)
        if not result:
            print(i, result)

    print('Traverse list_false')
    for i in list_false:
        result = s.isPalindrome(i)
        if result:
            print(i, result)
    
    
    
