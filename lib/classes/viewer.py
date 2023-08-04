class Viewer:
    def __init__(self, username):
        self.username = username
    
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


from classes.review import Review
