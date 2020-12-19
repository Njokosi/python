"""
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.



Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"
"""


class Solution:
    def interpret(self, command: str) -> str:

        # Response to be returned after traversing through the text
        result = ""

        # Tracker tracking the characters in the command
        i = 0
        while i < len(command):
            # If there are opening and closing brackets in consecutive positions
            if command[i] == "(" and command[i + 1] == ")":
                result += "o"
                i += 2
            elif command[i] in "()":
                i += 1
            else:
                result += command[i]
                i += 1
        return result


c = ""
c.replace("()", "o")
print(c)
print(Solution().interpret(c))
