class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if i < 0:
                while stack and stack[-1] > 0:
                    if -i < stack[-1]: i = None; break
                    elif -i == stack[-1]: stack.pop(); i = None; break
                    else: stack.pop()
            if i: stack.append(i)
        return stack
