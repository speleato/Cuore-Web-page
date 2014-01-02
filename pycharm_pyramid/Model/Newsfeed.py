# Newsfeed class keeps track of the number of posts in each department, used for pagination
class Newsfeed(object):
    def __init__(self, name=None, numPosts=0):
        self.name=name
        self.numPosts=numPosts

    def __str__(self):
        return self.name