class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = []
        content = {}
        for path in paths:
            path = path.split()
            root = path[0]
            for file in path[1:]:
                file = file.split('(')
                file_name = file[0]
                file_content = file[1][:-1]
                if file_content not in content:
                    content[file_content] = []
                content[file_content].append(root + '/' + file_name)

        for i in content.values():
            if len(i) > 1:
                ans.append(i)
        return(ans)