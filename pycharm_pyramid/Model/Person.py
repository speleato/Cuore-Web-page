__author__ = 'Kirby'
# The confirmed variable represents the level of confirmation similar to chmod. 1 means Leo confirmed, 2 means
# person confirmed, and 3 means both confirmed
class Person(object):
    def __init__(self, first_name=None, last_name=None, email=None, title=None, confirmed=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.title = title
        self.confirmed = confirmed
        '''
        self.department = department
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        '''
    def __str__(self):
        return (self.first_name)

    def submit_settings(self):
        store.save_unique("People", "email", self.email, self)
        return self
