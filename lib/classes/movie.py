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
            # raise Exception("Title must be a string between 1 and 255 characters, inclusive."

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
        return max(cls.all, key=lambda movie: movie.average_rating())


from classes.review import Review
from statistics import mean
