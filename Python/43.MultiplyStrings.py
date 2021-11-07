class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        num1, num2 = [int(n) for n in num1[::-1]], [int(n) for n in num2[::-1]]
        result = []
        for i1, n1 in enumerate(num1):
            for i2, n2 in enumerate(num2):
                i = i1 + i2
                while len(result) <= i:
                    result.append(0)
                result[i] += n1 * n2
                while result[i] > 9:
                    ten_digit = result[i] // 10
                    result[i] %= 10
                    i += 1
                    while len(result) <= i:
                        result.append(0)
                    result[i] += ten_digit
        return "".join(str(n) for n in result[::-1])


