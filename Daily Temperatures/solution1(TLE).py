class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        temperatures_length = len(temperatures)
        answer = [0] * temperatures_length
        for i in range(temperatures_length-1):
            x = 1
            while(temperatures[i+x] <= temperatures[i]):
                if i+x == temperatures_length - 1:
                    x = 0
                    break
                else:
                    x += 1
            answer[i] = x   
        return answer