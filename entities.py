"""
    Entity classes used in the second assignment for CSSE1001/7030.

    Athlete: Details of an athlete participating at the games.
    Event: Details of an individual event at the games.
    Country: Details of a country and its delegation at the games.
    Result: An athlete's result in an event.
"""

__author__ = "Caleb Aitken, 45309414"
__email__ = "caleb@jasa.id.au"


# done
class Athlete(object):
    """Details of an athlete who is competing at the games."""

    def __init__(self, identifier, first_name, surname, country):
        """
        Parameters:
            identifier (str): Athlete's identification number
            first_name (str): Athlete's first name.
            surname (str): Athlete's surname.
            country (Country): Object representing this athlete's country.
        """
        self.identifier = str(identifier)
        self.first_name = str(first_name)
        self.surname = str(surname)
        self.country = country
        self.results = {}
        self.events = []

    def get_result(self, event):
        """Return the result the athlete obtained in 'event'.

        Parameters:
            event (Event): Event for which the athlete's result is wanted.
            
        Return:
            Result: Athlete's result in 'event'.
        """
        return self.results[event]

    def add_result(self, event, result):
        """Sets athlete's 'result' in 'event', overwriting if previously set.

        Parameters:
            event (Event): Event in which this athlete competed.
            result (Result): Final result obtained in event.
        """
        self.results[event] = result

    def add_event(self, event):
        """Adds event to those in which this athlete will compete.

        Parameters:
            event (Event): Event in which this athlete will compete.
        """
        self.events.append(event)

    def add_events(self, events):
        """Adds all events to those in which this athlete will compete.

        Parameters:
            events (list[Event]): List of events in which this athlete will compete.
        """
        self.events.extend(events)

    def get_events(self):
        """(list[Event]) All events in which this athlete is competing."""
        return self.events

    def get_id(self):
        """(str) Athlete's identification number."""
        return self.identifier

    def get_full_name(self):
        """(str) Athlete's full name (first + surname)."""
        return self.first_name + " " + self.surname

    def get_country(self):
        """(Country) Country delegation to which this Athlete belongs."""
        return self.country

    def __str__(self):
        return str(self.get_full_name())

    def __repr__(self):
        return str(self)


# done
class Result(object):
    """An athlete's result in an event."""

    def __init__(self, result_value):
        """
        Parameters:
            result_value (float): Time or score athlete achieved in event.
        """
        self.result_value = float(result_value)
        self.place = 0

    def get_place(self):
        """(str) Place athlete obtained in the final event.

        Raise:
            RuntimeError: if places not yet determined.
        """
        if not self.places_determined():
            raise RuntimeError("Places not yet determined")
        else:
            return str(self.place)

    def set_place(self, place):
        """Sets the place that the athlete achieved in the final event.

        Parameters:
            place (int): Place that athlete achieved in the event.
        """
        self.place = int(place)

    def places_determined(self):
        """(bool) Has places been determined yet or not."""
        if self.place == 0:
            return False
        else:
            return True

    def get_result(self):
        """(str) Time or score athlete achieved in the final event."""
        return str(self.result_value)

    def get_medal(self):
        """(str) Medal athlete achieved or empty string if no medal.

        Raise:
            RuntimeError: if places not yet determined.
        """
        if self.get_place() == '1':
            return "Gold"
        elif self.get_place() == '2':
            return "Silver"
        elif self.get_place() == '3':
            return "Bronze"
        else:
            return ""

    def __str__(self):
        return str(self.get_result())

    def __repr__(self):
        return str(self)


# done
class Event(object):
    """An event in which athletes compete."""

    def __init__(self, event_name, timed, athletes):
        """
        Parameters:
            event_name (str): Official name of this event.
            timed (bool): Indicates if this is a timed event (else scored).
            athletes (list[Athlete]): Athletes who will compete in this event.
        """
        self.event_name = str(event_name)
        if timed == "TIMED" or timed == True:
            self.timed = True
        elif timed == "SCORED" or timed == False:
            self.timed = False
        self.athletes = athletes

    def is_timed(self):
        """(bool) True if event is timed, False if event is scored."""
        return self.timed

    def get_name(self):
        """(str) Official name of this event."""
        return self.event_name

    def get_athletes(self):
        """(list[Athlete]) All athletes currently registered to compete
                           in this event.
        """
        return list(self.athletes)

    def add_athlete(self, athlete):
        """Adds athlete to those who will compete in this event.

        Parameters:
            athlete (Athlete): An athlete who will compete in this event.
        """
        self.athletes.append(athlete)

    def add_athletes(self, athletes):
        """Adds all athletes to those who will compete in this event.

        Parameters:
            athletes (list[Athlete]): List of athletes who will compete
                                      in this event.
        """
        self.athletes.extend(athletes)

    def __str__(self):
        return str(self.get_name())

    def __repr__(self):
        return str(self)


# done
class Country(object):
    """Representation of a country's delegation."""

    def __init__(self, country_name, country_code):
        """
        Parameters:
            country_name (str): Official name of this country.
            country_code (str): 3 letter code used to represent this country.
        """
        self.country_name = str(country_name)
        self.country_code = str(country_code)
        self.athletes = []

    def get_athletes(self):
        """(list[Athlete]) All athletes competing for this country."""
        return self.athletes

    def add_athlete(self, athlete):
        """Adds athlete as a member of this country's delegation.

        Parameters:
            athlete (Athlete): An athlete who will compete for this country.
        """
        self.athletes.append(athlete)

    def add_athletes(self, athletes):
        """Adds all athletes as members of this country's delegation.

        Parameters:
            athletes (list[Athlete]): List of athletes who will compete
                                      for this country.
        """
        self.athletes.extend(athletes)

    def get_name(self):
        """(str) Country's official name."""
        return self.country_name

    def get_country_code(self):
        """(str) Country's 3 letter representation code."""
        return self.country_code

    def __str__(self):
        return str(self.get_name() + " (" + self.get_country_code() + ")")

    def __repr__(self):
        return str(self)


# done
class ManagedDictionary(object):
    """A generic collection as a managed dictionary."""

    def __init__(self):
        self._items = {}

    def add_item(self, key, item):
        """Adds an item to this collection.
           Overwriting previous item if key was mapped to an item already.

        Parameters:
            key (immutable): Unique key for the item.
            item (value): The item to be added to this collection.
        """
        self._items[key] = item

    def get_items(self):
        """(list) All items in this collection."""
        return list(self._items.values())

    def find_item(self, key):
        """Return the item which corresponds to this key.

        Parameters:
            key (immutable): Unique key for an item.

        Return:
            (value): Item that corresponds to this key.

        Raises:
            (KeyError): If 'key' does not correspond to an item.
        """
        return self._items[key]


"""
    Globally defined collections of all key entity objects.
    These are to be used to store all of each type of entity objects that
    are created by your program.
"""
all_athletes = ManagedDictionary()
all_countries = ManagedDictionary()
all_events = ManagedDictionary()


# done
def load_data(athletes, countries, events,
              timed_events_results, scored_events_results):
    """Loads the data from the named data files.

    Data is loaded into the all_athletes, all_countries and all_events
    collections. Results are accessible through the objects in these collections.

    Parameters:
        athletes (str) : Name of file containing athlete data.
        countries (str): Name of file containing country data.
        events (str)   : Name of file containing events data.
        timed_events_results (str) : Name of file containing results for timed
                                     events.
        scored_events_results (str): Name of file containing results for scored
                                     events.
    """
    with open(countries, "r") as raw_countries:
        for row in raw_countries:
            row = row.rstrip('\n').split(',')
            all_countries.add_item(row[0], Country(row[1], row[0]))
    with open(athletes, "r") as raw_athletes:
        for row in raw_athletes:
            row = row.rstrip('\n').split(',')
            all_athletes.add_item(row[0], Athlete(row[0], row[1], row[2], all_countries.find_item(row[3])))
    with open(events, "r") as raw_events:
        for row in raw_events:
            row = row.rstrip('\n').split(',')
            all_events.add_item(row[0], Event(row[0], row[1], []))
    with open(timed_events_results, "r") as raw_timed_events_results:
        for row in raw_timed_events_results:
            row = row.rstrip('\n').split(',')
            all_events.find_item(row[1]).add_athlete(all_athletes.find_item(row[0]))
            all_athletes.find_item(row[0]).add_event(all_events.find_item(row[1]))
            all_athletes.find_item(row[0]).add_result(all_events.find_item(row[1]), Result(row[2]))
    with open(scored_events_results, "r") as raw_scored_events_results:
        for row in raw_scored_events_results:
            row = row.rstrip('\n').split(',')
            all_events.find_item(row[1]).add_athlete(all_athletes.find_item(row[0]))
            all_athletes.find_item(row[0]).add_event(all_events.find_item(row[1]))
            all_athletes.find_item(row[0]).add_result(all_events.find_item(row[1]), Result(row[2]))
    for athlete in all_athletes.get_items():
        all_countries.find_item(athlete.get_country().get_country_code()).add_athlete(athlete)




if __name__ == "__main__":
    print("This module provides the entities for the Olympic games results",
          "processing application and is not meant to be executed on its own.")
