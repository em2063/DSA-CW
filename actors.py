   
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
    actors_dist = {}

    for movie, actors in actors_dict.items():
        for actor1 in actors:
            for actor2 in actors:
                if (actor1, actor2) not in edges and (actor1 != actor2):
                    g.addEdge(actor1, actor2)
                    edges.add((actor1, actor2))


    for actor in g.graph.keys():
        distances = g.bfs(actor)
        max_dist = max(distances.values())
        actors_dist[actor] = max_dist

    
    min_value = min(actors_dist.values())
    max_value = max(actors_dist.values())
    center = [key for key, value in actors_dist.items() if value == min_value]
    outliers = [key for key, value in actors_dist.items() if value == max_value]
        

    print("center: ", center)
    print("Outliers: ", outliers)


        

if __name__ == "__main__":
    main()







