class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))[::-1]
        stack = []
        for pos, speed in cars:
            dist = target - pos
            if not stack:
                stack.append(dist / speed)
            elif (dist / speed) > stack[-1]:
                stack.append(dist / speed)

        return len(stack)