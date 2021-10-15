# from _typeshed import IdentityFunction
# import sys

graph = {


'a':{'b':42},
'b':{'c':21,'d':95},
'c':{'d':90,'e':16, 'f':88},
'd':{'r':133},
'e':{'g':83,'f':92},
'f':{'j':17},
'r':{'x':44},
'g':{'h':8},
'j':{'k':5,},
'x':{'n':82},
'h':{'i':59},
'k':{'l':29},
'i':{'j':71},
'l':{'n':98, 'm':121},
'n':{'m':83, 'p':57},
'm':{'o':11},
'o':{'p':36},
'p':{'q':104},
'q':{'p':104},
}

def dijkstra(graph,start,goal):

    shortest_distance = {}
    track_predecessor = {}
    unseenNodes = graph
    infinity = 999999
    track_path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start]=0

    while unseenNodes:
        min_distance_node = None
        for node in unseenNodes:
            if min_distance_node is None:
                 min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                     min_distance_node = node
        path_options = graph[min_distance_node].items()
        for child_node, weigth in path_options:
            if weigth + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weigth + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node
        unseenNodes.pop(min_distance_node)
    currentNode = goal

    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print ("el camino no es valido")
            break
    track_path.insert(0,start)

    if shortest_distance[goal] != infinity:
        print("distancia minima es  " + str(shortest_distance[goal]))
        print("el camino mas corto es  " + str(track_path))

dijkstra(graph, 'a', 'q')