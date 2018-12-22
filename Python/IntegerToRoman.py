"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


class Solution:
    roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        str_index = 0
        result = ''
        while num > 0:
            digit_result = ''
            digit = num % 10
            if digit == 4:
                digit_result += self.roman[str_index] + self.roman[str_index+1]
            elif digit == 9:
                digit_result += self.roman[str_index] + self.roman[str_index+2]
            else:
                if digit >= 5:
                    digit_result += self.roman[str_index+1]
                    digit -= 5
                digit_result += self.roman[str_index] * digit
            str_index += 2
            result = digit_result + result
            num //= 10
            
        return result;

s = Solution()

test_case = [(1, 'I'),
             (2, 'II'),
             (3, 'III'),
             (4, 'IV'),
             (5, 'V'),
             (6, 'VI'),
             (7, 'VII'),
             (8, 'VIII'),
             (9, 'IX'),
             (10, 'X'),
             (12, 'XII'),
             (27, 'XXVII'),
             (58, 'LVIII'),
             (1994, 'MCMXCIV'),
             (3999, 'MMMCMXCIX')]

for c in test_case:
    answer = s.intToRoman(c[0])
    if answer != c[1]:
        print(c, answer)
