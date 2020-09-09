# https://leetcode.com/problems/compare-version-numbers/
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(c) for c in version1.split(".")]
        v2 = [int(c) for c in version2.split(".")]
        if len(v1) > len(v2):
            v2 += [0] * (len(v1) - len(v2))
        else:
            v1 += [0] * (len(v2) - len(v1))

        for i in range(len(v1)):
            if v1[i] == v2[i]:
                continue
            if v1[i] > v2[i]:
                return 1
            else:
                return -1
        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.compareVersion(version1 = "0.1", version2 = "1.1"))  # -1
    print(s.compareVersion(version1 = "1.0.1", version2 = "1"))  # 1
    print(s.compareVersion(version1 = "7.5.2.4", version2 = "7.5.3"))  # -1
    print(s.compareVersion(version1 = "1.01", version2 = "1.001"))  # 0
    print(s.compareVersion(version1 = "1.0", version2 = "1.0.0"))  # 0
