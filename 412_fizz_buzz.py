class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        for value in range(1, n + 1):
            if value % 15 == 0:
                result.append('FizzBuzz')
            elif value % 3 == 0:
                result.append('Fizz')
            elif value % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(value))
        return result
