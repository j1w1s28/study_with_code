#단지 번호 붙이기와 매우 유사

#DFS로 풀이
import sys
sys.setrecursionlimit(10**6)
def dfs(x,y):
    # 범위를 벗어나거나 방문한 집인 경우 0 반환
    if x < 0 or x >= N or y < 0 or y >= M or visited[x][y] or maps[x][y] == 0:
        return 0
    
    visited[x][y] = True
    count = 1
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        # 상하좌우 계속 방문 가능하면 방문해서 count 횟수 증가
        count += dfs(x + dx, y + dy)
    # 증가된 count 반환
    return count

Test_case = int(input())
for _ in range(Test_case):
    M, N, K = map(int, input().split())
    maps = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    for _ in range(K):
        # X,Y 뒤집어 져있어서 Y,X로 받아줌
        Y, X = map(int, input().split())
        maps[X][Y] = 1
    
    results = []
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and maps[i][j] == 1:
                results.append(dfs(i, j))
    
    print(len(results))

