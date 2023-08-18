from statistics import mean

class Movie:
    all = []

    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and title:
            self._title = title
        else:
            return None
            # raise Exception("Title must be a non-empty string")

    def reviews(self):
        return [review for review in Review.all if review.movie == self]

    def reviewers(self):
        return list({review.viewer for review in self.reviews()})

    def average_rating(self):
        return (
            round(mean([review.rating for review in self.reviews()]), 1)
            if self.reviews()
            else None
        )

    @classmethod
    def highest_rated(cls):
        non_none_movies = [movie for movie in cls.all if movie.average_rating() is not None]
        return max(non_none_movies, key=lambda movie: movie.average_rating()) if non_none_movies else None


class Review:
    all = []
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        type(self).all.append(self)
    
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and 1 <= rating <= 5 and not hasattr(self, "rating"):
            self._rating = rating
        else:
            return None
            # raise Exception("Rating must be an integer between 1 and 5, inclusive.")

    @property
    def viewer(self):
        return self._viewer
    
    @viewer.setter
    def viewer(self, viewer):
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            return None
            # raise Exception("Viewer must be a Viewer instance.")
    
    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, movie):
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            return None
            # raise Exception("Movie must be a Movie instance.")

        
class Viewer:
    
    all = []
    
    def __init__(self, username):
        self.username = username
        type(self).all.append(self)
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 6 <= len(username) <= 16:
            self._username = username
        else:
            return None
            # raise Exception("Username must be a string between 6 and 16 characters, inclusive.")

    def reviews(self):
        return [review for review in Review.all if review.viewer == self]

    def reviewed_movies(self):
        return list({review.movie for review in self.reviews()})

    def has_reviewed_movie(self, movie):
        return movie in self.reviewed_movies()

    def add_review(self, movie, rating):
        return Review(self, movie, rating)
    
    def num_positive_reviews(self):
        return len([review for review in self.reviews() if 3 <= review.rating <= 5])
        
    @classmethod
    def top_positive_reviewer(cls):
        if cls.all:
            top = max(cls.all, key=lambda viewer: viewer.num_positive_reviews() )
            if top.num_positive_reviews() > 0:
                return top
        return None
