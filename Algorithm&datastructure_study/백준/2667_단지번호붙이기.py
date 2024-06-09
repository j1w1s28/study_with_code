# dfs로 연결된 단지 수 찾기

def dfs(x, y):
    # 범위를 벗어나거나 방문한 집인 경우 0 반환
    if x < 0 or x >= N or y < 0 or y >= N or visited[x][y] or maps[x][y] == 0:
        return 0
    
    visited[x][y] = True
    count = 1
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        # 상하좌우 계속 방문 가능하면 방문해서 count 횟수 증가
        count += dfs(x + dx, y + dy)
    # 증가된 count 반환
    return count


N = int(input())
maps = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
result = []

#지도 반복문으로 돌아가면서 방문하지 않은 집과 집이 있으면 dfs 수행
for i in range(N):
    for j in range(N):
        if not visited[i][j] and maps[i][j] == 1:
            result.append(dfs(i, j))

#정답 출력
print(len(result))
for i in sorted(result):
    print(i)

