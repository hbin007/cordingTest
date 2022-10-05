def solution(board, moves):
    from collections import deque

    moves = deque(moves)
    buckets = []
    cot = 0

    while moves:
        move = moves.popleft()

        for i in range(len(board)):
            x = board[i][move - 1]

            if x != 0:
                board[i][move - 1] = 0

                if buckets and buckets[-1] == x:
                       buckets.pop()
                       cot += 2
                else:
                    buckets.append(x)
                break
    return cot