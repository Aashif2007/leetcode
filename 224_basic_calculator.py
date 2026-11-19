class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(i: int) -> tuple[int, int]:
            result = number = 0
            sign = 1
            while i < len(s):
                char = s[i]
                if char.isdigit():
                    number = number * 10 + int(char)
                elif char in '+-':
                    result += sign * number
                    number = 0
                    sign = 1 if char == '+' else -1
                elif char == '(':
                    number, i = evaluate(i + 1)
                elif char == ')':
                    return result + sign * number, i
                i += 1
            return result + sign * number, i

        return evaluate(0)[0]
