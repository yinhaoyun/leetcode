# 929. Unique Email Addresses

from typing import List
from collections import defaultdict


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = defaultdict(set)
        for e in emails:
            local, domain = e.split('@')
            local = local.split('+')[0].replace('.', '')
            d[domain].add(local)

        return sum([len(s) for s in d.values()])


s = Solution()
print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
)) # 2
print(s.numUniqueEmails(['a@gmail.com', 'b@gmail.com', 'c@gmail.com', 'c+abc@gmail.com']))