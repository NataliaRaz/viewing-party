# ------------- WAVE 1 --------------------
import copy
#Creates a dictionary representing a movie with title, genre and rating.
def create_movie(title, genre, rating):
    if title and genre and rating:
        return {"title": title, "genre": genre, "rating": rating} #it's a movie_dic
    return None
# -----------------------------------------
#Adds a movie to the user's watched list.
def add_to_watched(user_data, movie): 
    if "watched" not in user_data:
        user_data["watched"] = []
    user_data["watched"].append(movie)
    return user_data
# -----------------------------------------
#Adds a movie to the user's watchils.
def add_to_watchlist(user_data, movie):
    if "watchlist" not in user_data:
        user_data["watchlist"] = []
    user_data["watchlist"].append(movie)
    return user_data
# -----------------------------------------
#Moves a movie from the watchlist to the watched list.
def watch_movie(user_data, title):
    #watchlist_copy = user_data["watchlist"][:] #shallow copy syntax
    user_data_copy = copy.deepcopy(user_data) # deep copy

    for movie in user_data_copy["watchlist"]:
        if movie["title"] == title:
            user_data_copy["watchlist"].remove(movie)
            user_data_copy["watched"].append(movie)
            
    return user_data_copy
# ------------- WAVE 2 --------------------
#Calculates the average rating of all watched movies.
def get_watched_avg_rating(user_data):
    if "watched" not in user_data or len(user_data["watched"]) == 0:
        return 0.0

    total_rating = 0
    for movie in user_data["watched"]:
        if "rating" in movie:
            total_rating += movie["rating"]
        else:
            total_rating += 0

    avg_rating = total_rating / len(user_data["watched"])
    return avg_rating

# -----------------------------------------
#Determines the most frequently watched genre. 
def get_most_watched_genre(user_data):
    if "watched" not in user_data or len(user_data["watched"]) == 0:
        return None

    genre_count = {}
    most_watched_genre = None
    highest_count = 0

    for movie in user_data["watched"]:
        if "genre" in movie:
            genre = movie["genre"]
            if genre in genre_count:
                genre_count[genre] += 1
            else:
                genre_count[genre] = 1

            if genre_count[genre] > highest_count:
                highest_count = genre_count[genre]
                most_watched_genre = genre

    return most_watched_genre

# ------------- WAVE 3 --------------------
#Finds movies the user has watched but their friends haven't.
def get_unique_watched(user_data):

    user_watched = user_data["watched"]
    
    friends_watched = []
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie["title"])
    
    unique_movies = []
    for movie in user_watched:
        if movie["title"] not in friends_watched:
                unique_movies.append(movie)
    
    return unique_movies
# -----------------------------------------
#Finds movies that at least one friend has watched but the user hasn't.
def get_friends_unique_watched(user_data):
    user_watched_titles = []
    for movie in user_data["watched"]:
        user_watched_titles.append(movie["title"])

    friends_unique_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched_titles:
                if movie not in friends_unique_movies:
                    friends_unique_movies.append(movie)

    return friends_unique_movies
# ------------- WAVE 4 --------------------
def get_available_recs(user_data):    
    #Get the user's streaming subscriptions
    subscriptions = user_data["subscriptions"]

    friends_unique_movies = get_friends_unique_watched(user_data)
    
    #Prepare an empty list for recommended movies
    recommended_movies = []

    for movie in friends_unique_movies:
        if "host" in movie:
            if movie["host"] in subscriptions:
                recommended_movies.append(movie)

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
def get_new_rec_by_genre(user_data):
    #Get the user's most watched genre
    most_watched_genre = get_most_watched_genre(user_data)

    friends_unique_movies = get_friends_unique_watched(user_data)
    
    #Prepare an empty list for recommended movies
    recommended_movies = []

    for movie in friends_unique_movies:
        if "genre" in movie:
            if movie["genre"] == most_watched_genre:
                recommended_movies.append(movie)
                
    return recommended_movies

# -----------------------------------------
def get_rec_from_favorites(user_data):
    # Create an empty list for recommended movies
    recommended_movies = []

    user_favorite_titles = [];
    for movie in user_data["favorites"]:
        user_favorite_titles.append(movie["title"])
    
    # Get the list of movies that none of the user's friends have watched
    unique_watched = get_unique_watched(user_data) 

    recommended_movies = []
    for movie in unique_watched:
        if "title" in movie:
            if movie["title"] in user_favorite_titles:
                recommended_movies.append(movie)
    
    return recommended_movies
