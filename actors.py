from collections import deque

def open_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        actors_dict = {}
        for line in file:
            full_data = line.strip().split('/')
            movie = full_data[0]
            actors = full_data[1:]
            if movie not in actors_dict:
                actors_dict[movie] = []
            actors_dict[movie].extend(actors)
    
    return actors_dict

class Graph: 

    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, s):
        visited = {actor: False for actor in self.graph}
        distances = {}

        queue = []

        queue.append(s)
        visited[s] = True
        distances[s] = 0
        while queue:
            s = queue.pop(0)

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    distances[i] = distances[s] + 1
                    
        return distances

def main():
    file_path = r'C:\Users\Ethan\Desktop\uni\DSA CW\movies-test.txt'
    edges = set()
    actors_dict = open_file(file_path)

    g = Graph()

    for movie, actors in actors_dict.items():
        for i, actor1 in enumerate(actors):
            for actor2 in actors[i+1:]:
                if ((actor1, actor2) not in edges or (actor2, actor1)) not in edges and (actor1 != actor2):
                    g.addEdge(actor1, actor2)
                    edges.add((actor1, actor2))
                    
                    

if __name__ == "__main__":
    main()

