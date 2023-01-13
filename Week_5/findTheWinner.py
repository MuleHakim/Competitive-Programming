class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        friends = [friend for friend in range(1, n + 1)]
        index = 0

        while len(friends) > 1:
            index = (index + k - 1) % len(friends)
            friends.pop(index)

        return friends[0]

        # if n == 1:
        #     return n

        # lst = deque(range(1,n + 1))
        # while len(lst) > 1:
        #     lst.rotate(1 - k)
        #     lst.popleft()

        # return lst[0]]
