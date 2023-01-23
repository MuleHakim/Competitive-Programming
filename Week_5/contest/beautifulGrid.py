from math import ceil


def beautifulGrid(t):
    for _ in range(t):
        n = int(input())

        grid = []
        for _ in range(n):
            row = [int(num) for num in input()]
            grid.append(row)

        cost = 0
        for row in range(ceil(n / 2)):
            for col in range(n // 2):
                count = sum(
                        [
                        grid[row][col],
                        grid[col][-1 - row],
                        grid[-1 - row][-1 - col],
                        grid[-1 - col][row],
                        ]
                    )

                cost += min(count, 4 - count)
        print(cost)
        
if __name__ == '__main__':
    test_case = int(input())
    beautifulGrid(test_case)
