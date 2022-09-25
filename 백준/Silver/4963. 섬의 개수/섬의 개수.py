def dfs():
    while len(stack) > 0:
        a, b = stack.pop()

        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (-1, -1), (1, -1), (1, 1)):
            ni = a + di
            nj = b + dj

            if 0 <= ni < w and 0 <= nj < h:
                if arr[ni][nj]:
                    arr[ni][nj] = 0
                    stack.append((ni, nj))


while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    else:
        arr = [list(map(int, input().split())) for _ in range(w)]

        stack = []

        cnt = 0

        for i in range(w):
            for j in range(h):
                if arr[i][j]:
                    arr[i][j] = 0
                    stack.append((i, j))
                    dfs()
                    cnt += 1

        print(cnt)
