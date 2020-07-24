from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        utf_n_byte = 0
        while i < len(data):
            if data[i] & 0x80 == 0:
                # print(i, 0)
                i += 1
                continue
            elif data[i] & 0xf8 == 0xf0:
                utf_n_byte = 3
            elif data[i] & 0xf0 == 0xe0:
                utf_n_byte = 2
            elif data[i] & 0xe0 == 0xc0:
                utf_n_byte = 1
            else:
                return False
            # print(i, utf_n_byte)
            if i + utf_n_byte > len(data) - 1:
                return False
            while utf_n_byte > 0:
                i += 1
                # print(i, bin(data[i]), data[i] & 0xc0)
                if data[i] & 0xc0 != 0x80:
                    return False
                utf_n_byte -= 1
            i += 1
        return True


s = Solution()
print(s.validUtf8([197, 130, 1]))  # 11000101 10000010 00000001, true
print(s.validUtf8([235, 140, 4]))  # false
print(s.validUtf8([237]))  # false
