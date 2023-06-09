class Movie:

    def __init__(self, title):
        self.title = title

    def reviews(self, new_review=None):
        from classes.review import Review
        pass

    def reviewers(self, new_reviewer=None):
        from classes.review import Review
        pass

    def average_rating(self):
        pass

    @classmethod
    def highest_rated(cls):
        pass
