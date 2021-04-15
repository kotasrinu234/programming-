#n--Number of stores
#m--Number of routes connecting different stores
n,m=map(int,input().split())
d={}
total_nodes=[]
for i in range(m):
    #a,b represents connected stores
    #c --Distance between stores
    a,b,c=map(int,input().split())
    if a in d:
        d[a].append([b,c])
    else:
        total_nodes.append(a)
        d[a]=[[b,c]]
    if b not in total_nodes:
        total_nodes.append(b)
    if b in d:
        d[b].append([a,c])
    else:
        d[b]=[[a,c]]
def dijkstra(graph,start):
    shortest_distance = {}

    predecessor = {}
    infinity = 9999999
    path = []
    for node in total_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
 
    while total_nodes:
        minNode = None
        for node in total_nodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        if minNode not in graph:
            total_nodes.remove(minNode)
            continue
        for k in graph[minNode]:
            childNode=k[0]
            weight=k[1]
            if childNode not in shortest_distance:
                pass
            elif weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        total_nodes.remove(minNode)
    sorted_values = sorted(shortest_distance.values()) # Sort the values
    sorted_dict = {}

    for i in sorted_values:
        for k in shortest_distance.keys():
            if shortest_distance[k] == i:
                sorted_dict[k] = shortest_distance[k]
                break
    shorted_stores=[]
    c=0
    for i in sorted_dict:
        c+=1
        shorted_stores.append(i)
        if c==5:
            break
    return shorted_stores

print(dijkstra(d,1))
