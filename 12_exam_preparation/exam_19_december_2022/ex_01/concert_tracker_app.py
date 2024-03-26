from ex_01.band import Band
from ex_01.band_members.drummer import Drummer
from ex_01.band_members.guitarist import Guitarist
from ex_01.band_members.singer import Singer
from ex_01.concert import Concert


class ConcertTrackerApp:
    MUSICIAN_TYPES = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }
    CONCERT_REQUIREMENTS = {
        "Rock": {"Drummer": ["play the drums with drumsticks"],
                 "Singer": ["sing high pitch notes"],
                 "Guitarist": ["play rock"]
                 },
        "Metal": {"Drummer": ["play the drums with drumsticks"],
                  "Singer": ["sing low pitch notes"],
                  "Guitarist": ["play metal"]

                  },
        "Jazz": {"Drummer": ["play the drums with drum brushes"],
                 "Singer": ["sing low pitch notes", "sing high pitch notes"],
                 "Guitarist": ["play jazz"]
                 }
    }

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def get_musician(self, musician_name):
        result = next((m for m in self.musicians if m.name == musician_name), None)
        if result:
            return result
        raise Exception(f"{musician_name} isn't a musician!")

    def get_band(self, band_name):
        result = next((b for b in self.bands if b.name == band_name), None)
        if result:
            return result
        raise Exception(f"{band_name} isn't a band!")

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")
        if any(m for m in self.musicians if m.name == name):
            raise Exception(f"{name} is already a musician!")

        self.musicians.append(self.MUSICIAN_TYPES[musician_type](name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if any(b for b in self.bands if b.name == name):
            raise Exception(f"{name} band is already created!")
        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = next((c for c in self.concerts if c.place == place), None)
        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        band = self.get_band(band_name)
        musician = self.get_musician(musician_name)

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.get_band(band_name)
        musician = next((m for m in band.members if m.name == musician_name), None)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = next(filter(lambda b: b.name == band_name, self.bands))
        concert = next(filter(lambda c: c.place == concert_place, self.concerts))

        band_members = [member.__class__.__name__ for member in band.members]
        if set(band_members) != set(ConcertTrackerApp.MUSICIAN_TYPES):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        for genre, info in self.CONCERT_REQUIREMENTS.items():
            if genre == concert.genre:
                for member, skill in info.items():
                    for m in band.members:
                        if type(m).__name__ == member and not set(skill).issubset(set(m.skills)):
                            raise Exception(f"The {band_name} band is not ready to play at the concert!")
        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
