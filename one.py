G = [[ 0, 1, 1, 0, 1, 0],
[ 1, 0, 1, 1, 0, 1],
[ 1, 1, 0, 1, 1, 0],
[ 0, 1, 1, 0, 0, 1],
[ 1, 0, 1, 0, 0, 1],
[ 0, 1, 0, 1, 1, 0]]
node = "abcdef"
t_={}
for i in range(len(G)):
t_[node[i]] = i
degree =[]
for i in range(len(G)):
  degree.append(sum(G[i]))
colorDict = {}
for i in range(len(G)):
  colorDict[node[i]]=["Blue","Red","Yellow","Green"]
sortedNode = list(node)
n = len(degree)

for i in range(n):
    for j in range(0, n-i-1):
        if degree[j] < degree[j+1]:
            degree[j], degree[j+1] = degree[j+1], degree[j]
            sortedNode[j], sortedNode[j+1] = sortedNode[j+1], sortedNode[j]
theSolution={}
for n in sortedNode:
  setTheColor = colorDict[n]
  theSolution[n] = setTheColor[0]
  adjacentNode = G[t_[n]]
  for j in range(len(adjacentNode)):
     if adjacentNode[j]==1 and (setTheColor[0] in colorDict[node[j]]):
        colorDict[node[j]].remove(setTheColor[0])
  for t,w in sorted(theSolution.items()):
    print("Node",t," = ",w)
