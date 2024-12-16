class Place():
    def __init__(self, given_name, next_places, locked=False):
        # locked=False means that the locked parameter will be False by default if not provided.
        self.name = given_name
        self.next_places = next_places
        self.locked = locked
        self.searchable_objects = []
        # add more atributes as needed

    def add_next_place(self, place_instance):
        self.next_places.append(place_instance)

orbit = Place("orbit", ["geostationary orbit", "the Moon", "Mars", "home"])