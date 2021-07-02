#template of dfs
import sys
sys.setrecursionlimit(1000000)

visited = [False]*n

def dfs(i):
    visited[i] = True
    for j in E[i]:
        if not(visited[j]):
            visited[j] = True
            dfs(j)
dfs(start)