class Band:

    all = []

    def __init__(self, name, hometown):
        self.name = name
        self._hometown = hometown
        Band.all.append(self)
        self.band_shows = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
    
    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, hometown):
        if hometown == self.hometown and isinstance(hometown, str) and len(hometown) > 0:
            self._hometown = hometown

    def concerts(self):
        return [concert for concert in Concert.all if concert.band == self]

    def venues(self):
        return list(set([concert.venue for concert in Concert.all if concert.band == self]))

    def play_in_venue(self, venue, date):
        self.band_shows.append(self)
        return Concert(date, self, venue)

    def all_introductions(self):
        pass

############################## CLASS WITH THE SSOT ##############################
class Concert:

    all = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str) and len(date) > 0:
            self._date = date
    
    @property
    def band(self):
        return self._band
    
    @band.setter
    def band(self, band):
        if isinstance(band, Band):
            self._band = band
    
    @property
    def venue(self):
        return self._venue
    
    @venue.setter
    def venue(self, venue):
        if isinstance(venue, Venue):
            self._venue = venue

    def hometown_show(self):
        pass

    def introduction(self):
        pass

############################################################################

class Venue:

    all = []

    def __init__(self, name, city):
        self.name = name
        self.city = city
        Venue.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        if isinstance(city, str) and len(city) > 0:
            self._city = city

    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]

    def bands(self):
        return list(set([concert.band for concert in Concert.all if concert.venue == self]))
    
