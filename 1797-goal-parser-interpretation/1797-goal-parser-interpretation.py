class Solution:
    def interpret(self, command: str) -> str:
            # brute force
        # command = command.replace("G", "G")
        # command = command.replace("()", "o")
        # command = command.replace("(al)", 'al')
        # return command
            # even better
        i = 0
        string = []
        while i < len(command):
            if command[i] == "G":
                string.append("G")
                i += 1
            elif command[i] == "(" and command[i+1] == ")":
                string.append("o")
                i += 2
            else:
                string.append("al")
                i += 4
        return "".join(string)
