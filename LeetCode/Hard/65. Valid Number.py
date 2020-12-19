"""
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. It would be best if you gathered all requirements up
front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.


"""
import re


class Solution:
    def isNumber(self, text: str) -> bool:
        # Remove the spaces at the beginning and the end
        text = text.strip()

        print(f"The text is {text}")
        # For decimal places we split with . and join

        if 'e' in text:
            text = re.split(r"[e\s]\s*", text)

            # Checks if no number in the beginning or the end of e e.g e1 and 1e
            if text[0] == '' or text[-1] == '':
                return False
            text = "".join(text)

        # split with delimiters full stop, letter 'e' and space followed by any amount of extra whitespace.
        text = re.split(r"[e.\s]\s*", text)

        print(f"After splitting: {text}")

        text = ''.join(text)
        print(f"After splitting and joining we get {text}")

        # Check if the given text is decimal
        if text.isdecimal():
            return True

        # Check if the given text is decimal

        return False


t0 = ""
print(Solution().isNumber(t0))

t1 = "0"
print(Solution().isNumber(t1))

t2 = " 0.1 "
print(Solution().isNumber(t2))

t3 = "abc"
print(Solution().isNumber(t3))

t4 = "1 a"
print(Solution().isNumber(t4))

t5 = "2e10"
print(Solution().isNumber(t5))

t6 = " -90e3   "
print(Solution().isNumber(t6))

t7 = " 1e"
print(Solution().isNumber(t7))

t8 = "e3"
print(Solution().isNumber(t8))

t9 = " 6e-1"
print(Solution().isNumber(t9))

t10 = " 99e2.5 "
print(Solution().isNumber(t10))

t11 = "53.5e93"
print(Solution().isNumber(t11))

t12 = " --6 "
print(Solution().isNumber(t12))

t13 = "-+3"
print(Solution().isNumber(t13))

t14 = "95a54e53"
print(Solution().isNumber(t14))
