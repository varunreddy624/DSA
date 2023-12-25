#n - number of nodes in the tree
#adj - adjacency list representation of tree

from math import log2

dist=[0]*(n+1)
v=[0]*(n+1)
inT=[0]*(n+1)
outT=[0]*(n+1)
c=[0]
size=int(log2(n))+1
up=[[1 for j in range(size)]for i in range(n+1)]

def is_ancestor(i,j):
    return inT[i]<=inT[j] and outT[i]>=outT[j]

def lca(a,b):
    if is_ancestor(a,b):
        return a
    if is_ancestor(b,a):
        return b
    for i in range(size-1,-1,-1):
        if not is_ancestor(up[a][i], b):
            a=up[a][i]

    return up[a][0]

def dfs(i,p,adj):
    inT[i]=c[0]
    c[0]+=1

    v[i]=1
    up[i][0]=p
    for s in range(1,size):
        up[i][s]=up[up[i][s-1]][s-1]

    for j in adj[i]:
        if v[j]==0:
            dist[j]=dist[i]+1
            dfs(j,i,adj)
    outT[i]=c[0]