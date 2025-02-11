class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        string = []

        counter = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1], reverse=True)}
        for k, v in counter.items():
            string.append(k*v)
        return "".join(string)