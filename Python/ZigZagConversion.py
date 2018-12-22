class Solution:
    def calculate_padded_len(self, size, factor):
        if size // factor * factor != size:
            return (size // factor + 1) * factor
        else:
            return size
        
    def convert(self, s, numRows, debug=False):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        slices = []
        running_index = 0
        down_span = numRows
        up_span = down_span - 2
        str_len = len(s)

        down_run = True
        span = 0

        if debug:
            print("Original:", (s,), len(s))
        # Make string len be multiple of (numRows+2)
        str_len = self.calculate_padded_len(str_len, numRows * 2 - 2)
        s = s + ' ' * (str_len - len(s))
        
        if debug: print((s,), len(s))
        while True:
            if down_run:
                span = down_span
                if running_index + span > str_len:
                    break
                slices.append(list(s[running_index : running_index+span]))
            else:
                span = up_span
                if running_index + span > str_len:
                    break
                reversed_up_span = list(s[running_index:running_index+span])[::-1]
                slices.append([''] + reversed_up_span + [''])
            running_index += span
            down_run = not down_run

        if debug:
            for slice in slices:
                print(slice)
        
        ts_list = map(list, zip(*slices))
        ret = ''.join([''.join(c) for c in ts_list])
        return ret.replace(' ', '')
        
              
        
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
    if answer != c[1]:
        print(c, 'but answer=', answer)
        s.convert(c[0][0], c[0][1], True)
        print()
