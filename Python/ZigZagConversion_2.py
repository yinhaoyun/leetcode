class Solution:
    def convert(self, s, numRows, debug=False):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        numRows = min(len(s), numRows)
        ret = [[] for x in range(numRows)]

        going_down = True
        cur_row = 0
        for c in s:
            ret[cur_row].append(c)
            cur_row += 1 if going_down else -1
            if cur_row == numRows - 1 or cur_row == 0:
                going_down = not going_down
        return ''.join([''.join(r) for r in ret])
              
        
test_cases = [(('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR'),
              (('PAYPALISHIRING', 4), 'PINALSIGYAHRPI'),
              (('PAYPALISHIRING', 1), 'PAYPALISHIRING'),
              (('A', 1), 'A'),
              (('1234567', 2), '1357246'),
              (("ABCDE", 3), 'AEBDC'),
              (('ABCD', 3), 'ABDC')]

s = Solution()
for c in test_cases:
    answer = s.convert(c[0][0], c[0][1])
    # print(c, ', answer=', answer)
    if answer != c[1]:
        print(c, 'but answer=', answer)
        s.convert(c[0][0], c[0][1], True)
        print()
