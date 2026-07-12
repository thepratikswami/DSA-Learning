from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Process cars from closest-to-target to farthest.
        cars = sorted(zip(position, speed), reverse=True)
        stack = []  # holds arrival times, strictly increasing

        for pos, spd in cars:
            time = (target - pos) / spd
            # A car merges into the fleet ahead if it arrives no later than it.
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))  # 3
    print(Solution().carFleet(10, [3], [3]))                           # 1
    print(Solution().carFleet(100, [0, 2, 4], [4, 2, 1]))              # 1
# DEBUG RUNNER END
