class Place():
    def __init__(self, given_name, given_size, locked=False):
        # locked=False means that the locked parameter will be False by default if not provided.
        self.name = given_name
        self.size = given_size
        self.locked = locked
        self.next_places = []
        self.searchable_objects = []
        # add more atributes as needed

    def add_next_place(self, place_instance):
        self.next_places.append(place_instance)

    def unlock(self):
        pass

    # add more methods as needed
