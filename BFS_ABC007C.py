
#ABC007 C BFS
#この問題は、隣接グラフを用いずとも４近傍を列挙すればOK

from collections import deque
r,c = map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
s=[]
for i in range(r):
    t = input()
    s.append(t)

sy-=1
sx-=1
gy-=1
gx-=1

#↓始点からの最小移動回数を管理する2次元配列。-1の時未到達
dist = []
for i in range(r):
    dist.append([-1]*c)

q = deque()
q.append([sy,sx])
dist[sy][sx] = 0

while len(q)>0:
    i,j = q.popleft()
    if s[i][j] =="#":
        continue
    for i2,j2 in ([i+1,j],[i-1,j],[i,j+1],[i,j-1]):
        if not(0<=i2<r and 0<=j2<c):
            continue
       
        if dist[i2][j2]==-1:
          dist[i2][j2] = dist[i][j] + 1
          q.append([i2,j2])
print(dist[gy][gx])
        
