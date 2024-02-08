class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0]<temp:
                top = stack.pop()
                ans[top[1]] = idx-top[1]
            stack.append((temp, idx))
        return ans


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t= temperatures
        track = [-1]*101
        ans = [0]*len(t)

        for i in range(len(t)-1, -1, -1):
            temp = t[i]
            track[temp] = i
            #search in the forward array
            mini = 10**5+1 # here it got me
            for wtemp in range(temp+1, 101):
                if track[wtemp] != -1 and mini > track[wtemp]:
                    mini = track[wtemp]
            if mini != 10**5+1:
                ans[i]=mini-i
        return ans
        