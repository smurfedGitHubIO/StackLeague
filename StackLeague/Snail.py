def snail(array):
   if len(array) == 1:
       return array[0]
   n,m, i, j = len(array),len(array[0]), 0, 0
   lst = [[0,1],[1,0],[0,-1],[-1,0]]
   vis = [[False for i in range(m)] for j in range(n)]
   ans, cur, cnt = [], 0, 0
   while cnt != n*m:
       if i < n and i > -1 and j < m and j > -1 and not vis[i][j]:
           while i+lst[cur%4][0] >= n or i+lst[cur%4][0] == -1 or j+lst[cur%4][1] >= m or j+lst[cur%4][1] == -1:
               cur = (cur+1)%4
           ans.append(array[i][j])
           vis[i][j] = True
           i += lst[cur%4][0]
           j += lst[cur%4][1]
           if vis[i][j]:
               i -= lst[cur%4][0]
               j -= lst[cur%4][1]
               cur += 1
               i += lst[cur%4][0]
               j += lst[cur%4][1]
           cnt += 1
       else:
           i -= lst[cur%4][0]
           j -= lst[cur%4][1]
           cur = (cur+1)%4
   return ans