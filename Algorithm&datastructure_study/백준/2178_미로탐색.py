# BFS로 최소 경로 찾기 풀기
from collections import deque

len_rows , len_cols = map(int, input().split())
maze = [list(map(int, input())) for _ in range(len_rows)]
visited = [[False]*len_cols for _ in range(len_rows)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()
queue.append((0, 0))
visited[0][0] = True
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        #방문할 수 있으면 방문 처리하고 maze에 방문횟수 저장
        if 0 <= nx < len_rows and 0 <= ny <len_cols and maze[nx][ny] == 1 and not visited[nx][ny]:
            queue.append((nx, ny))
            visited[nx][ny] = True
            maze[nx][ny] = maze[x][y] + 1

print(maze[len_rows-1][len_cols-1])