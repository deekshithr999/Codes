class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exec_times = [0]*n
        stack = []
        prev_time = 0

        for log in logs:
            log_info = log.split(":")
            fun_id, action, timestamp = int(log_info[0]), log_info[1], int(log_info[2])

            if action == "start":
                if stack:
                    exec_times[stack[-1]]+=timestamp - prev
                stack.append(fun_id)
                prev = timestamp
            else:
                exec_times[stack.pop()] += timestamp -prev +1
                prev = timestamp + 1 #Edge case
        return exec_times


        

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exec_times = [0]*n
        stack = []
        for log in logs:
            log_split = log.split(':')
            fun_id, condition, timestamp = int(log_split[0]), log_split[1], int(log_split[2])
            if condition == "start":
                stack.append((fun_id, timestamp))
            else:
                ele = stack.pop()
                carry = timestamp - ele[1]+1
                exec_times[fun_id]+=carry
                if stack:
                    exec_times[stack[-1][0]]-= carry
        return exec_times