class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1 = a.split("+")
        num2 = b.split("+")
        num1[1] = num1[1].split("i")[0]
        num2[1] = num2[1].split("i")[0]
        part1 = (int(num1[0]) * int(num2[0])) - (int(num1[1]) * int(num2[1]))
        part2 = (int(num1[0]) * int(num2[1])) + (int(num1[1]) * int(num2[0]))
        return str(part1) + "+" + str(part2) + "i"


sol = Solution()
print(sol.complexNumberMultiply("1+1i", "1+1i"))
