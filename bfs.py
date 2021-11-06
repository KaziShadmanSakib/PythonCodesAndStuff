from queue import Queue

graph = {
  '0' : ['1','2','3'],
  '1' : ['3', '4'],
  '2' : ['3'],
  '3' : ['5','6'],
  '4' : ['7','8'],
  '5' : ['6'],
  '6' : ['7'],
  '7' : ['8'],
  '8' : ['7']
}

visited = [] 
queue = Queue()

def bfs(visited, graph, node):
  visited.append(node)
  queue.put(node)

  while not queue.empty():
    s = queue.get()
    print (s) 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.put(neighbour)

# Driver Code
bfs(visited, graph, '0')