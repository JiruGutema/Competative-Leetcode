import collections

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = collections.defaultdict(int)

        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            key = None
            for sub in domain.split('.')[::-1]:
                if key is None:
                    key = sub
                else:
                    key = sub + '.' + key
                counts[key] += int(count)

        result = []
        for domain, count in counts.items():
            result.append(f"{count} {domain}")
        return result