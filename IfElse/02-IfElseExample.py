movie_name = "Fukrey"

movies = ["Bang Bang", "Bahubali", "Krish", "Fukrey"] # List

# if movie_name == movies[0]:
#     print("Movie Found at",movies.index(movie_name))
# elif movie_name == movies[1]:
#     print("Movie Found at",movies.index(movie_name))
# elif movie_name == movies[2]:
#     print("Movie Found at",movies.index(movie_name))
# elif movie_name == movies[3]:
#     print("Movie Found at",movies.index(movie_name))
# else:
#     print("Not Found")

for i in range(len(movies)):
    if movie_name == movies[i]:
        print("Movie Found at",movies.index(movie_name))
        break
    else:
        print("Not Found")

print("Program Terminated...")