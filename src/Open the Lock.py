class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0
        visited = set(deadends)
        steps = 0
        queue = deque()
        queue.append("0000")
        while queue:
            for _ in range(len(queue)):
                nums = queue.popleft()
                if nums == target:
                    return steps
                if nums in visited:
                    continue
                visited.add(nums)
                for idx in range(4):
                    num = int(nums[idx])
                    next_num = (num + 10 + 1) % 10
                    prev_num = (num + 10 - 1) % 10
                    queue.append(nums[:idx] + str(prev_num) + nums[idx + 1:])
                    queue.append(nums[:idx] + str(next_num) + nums[idx + 1:])
            steps += 1
        return -1
                    
