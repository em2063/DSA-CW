
def open_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        actors_dict = {}
        for line in file:
            full_data = line.strip().split('/')
            movie = full_data[0]
            actors = full_data[1:]
            for actor in actors:
                if actor not in actors_dict:
                    actors_dict[actor] = []
                if movie not in actors_dict[actor]:
                    actors_dict[actor].append(movie)
                print(actor, actors_dict[actor])


def main():
    file_path = r'C:\Users\Ethan\Desktop\uni\DSA CW\movies-test.txt'
    actors_dict = open_file(file_path)



if __name__ == "__main__":
    main()