"""
    Logical processing classes used in the second assignment for CSSE1001/7030.

    ProcessResults: Abstract class that defines the logical processing interface.
    AthleteResults: Provides details of one athlete’s results for all of the
                    events in which they competed.
    CountryResults: Provides a summary of the results of all athletes who
                    competed for one country.
    EventResults  : Provides details of the results of all athlete's who
                    competed in one event.
    DeterminePlaces: Determines the place ranking of all athletes who competed
                     in one event.
"""

__author__ = "Caleb Aitken, 45309414"
__email__ = "caleb@jasa.id.au"

from entities import Athlete, Result, Event, Country, ManagedDictionary
from entities import all_athletes, all_countries, all_events, load_data


class ProcessResults(object):
    """Superclass for the logical processing commands."""

    _processing_counter = 0  # Number of times any process command has executed.

    def process(self):
        """Abstract method representing collecting and processing results data.
        """
        ProcessResults._processing_counter += 1

    def get_results(self):
        """Abstract method representing obtaining the processed results.

        Return:
            list: Subclasses will determine the contents of the resulting list.
        """
        raise NotImplementedError()


class AthleteResults(ProcessResults):
    """Determines the results achieved by one athlete."""

    _athlete_results_counter = 0  # Number of times this command has executed.

    def __init__(self, athlete):
        """
        Parameters:
            athlete (Athlete): Athlete for whom we wish to determine their results.
        """
        self._athlete = athlete

    def process(self):
        """Obtain all the results for this athlete and
           order them from best to worst placing.
           If two or more results have the same place they should be ordered
           by event name in ascending alphabetical order.
        """
        super().process()
        AthleteResults._athlete_results_counter += 1
        self._results = []
        for event in self._athlete.get_events():
            self._results.append([self._athlete.get_result(event), event])
        self._results = sorted(sorted(self._results, key=lambda event: event[1].get_name()), key=lambda result: int(result[0].get_place()))
        self._results = [item[0] for item in self._results]

    def get_results(self):
        """Obtain the processed results for _athlete.

        Return:
            list[Result]: Ordered list of the _athlete's results.
                          Sorted from best to worst, based on place in event.
                          Results with the same place are ordered by event name
                          in ascending alphabetical order.

        Raises:
            ValueError: If process has not yet been executed.
        """
        try:
            return self._results
        except Exception as exc:
            raise ValueError("process has not yet been executed") from exc

    def get_usage_ratio():
        """Ratio of usage of the AthleteResults command against all commands.

        Return:
            float: ratio of _athlete_results_counter by _processing_counter.
        """
        return (AthleteResults._athlete_results_counter
                / AthleteResults._processing_counter)

    def __str__(self):
        """(str) Return a formatted string of the results for this athlete."""
        """Implementation of this is optional but useful for observing your
           programs behaviour.
        """
        return ""


class EventResults(ProcessResults):
    """Determine the results of all athletes that competed in an event"""

    _event_results_counter = 0

    def __init__(self, event):
        """
        Parameters:
             event (Event): event for which we wish to find the results from.
        """
        self._event = event

    def process(self):
        """
        Obtain all the results for this event and
        sort them from best to worst, based on place, then
        these should be ordered by the athlete's full name.
        """
        super().process()
        EventResults._event_results_counter += 1
        self._results = []
        for athlete in self._event.get_athletes():
            self._results.append([athlete.get_result(self._event), athlete])
        self._results = sorted(sorted(self._results, key=lambda athlete: athlete[1].get_full_name()), key=lambda result: int(result[0].get_place()))
        self._results = [item[1] for item in self._results]

    def get_results(self):
        """list[Result]: list of results"""
        try:
            return self._results
        except Exception as exc:
            raise ValueError("process has not yet been exectued") from exc

    def get_usage_ratio():
        """Ratio of usage of the EventResults command against all commands.

        Return:
            float: ratio of _event_results_counter by _processing_counter.
        """
        return float(EventResults._event_results_counter
                / EventResults._processing_counter)

    def __str__(self):
        return ""


class CountryResults(ProcessResults):
    """Determine the results achieved by one country."""

    _country_results_counter = 0  # number of times this command has executed

    def __init__(self, country):
        """
        Parameters:
             country (Country): Country for whom we wish to determine their results.
        """
        self._country = country

    def process(self):
        """
        Obtain a summary of the results for this country.
        Determine the number of gold, silver, bronze medals were won by athletes who competed for this county, and the number of athletes who competed for this country
        """
        super().process()
        CountryResults._country_results_counter += 1
        self.num_gold = int()
        self.num_silver = int()
        self.num_bronze = int()
        self.num_athletes = int()
        for athlete in self._country.get_athletes():
            self.num_athletes += 1
            for event in athlete.get_events():
                if athlete.get_result(event).get_medal() == "Gold":
                    self.num_gold += 1
                elif athlete.get_result(event).get_medal() == "Silver":
                    self.num_silver += 1
                elif athlete.get_result(event).get_medal() == "Bronze":
                    self.num_bronze += 1

    def get_results(self):
        """Obtain the processed results for _country

        Return:
            list[int]: number of gold, silver, and bronze medals one by country

        Raises:
            ValueError: If process has not yet been executed
        """
        return [self.get_num_gold(), self.get_num_silver(), self.get_num_bronze(), self.get_num_athletes()]

    def get_num_gold(self):
        """(int) number fo gold medals won by this country"""
        try:
            return self.num_gold
        except Exception as exc:
            raise ValueError("process has not yet been executed") from exc

    def get_num_silver(self):
        """(int) number fo silver medals won by this country"""
        try:
            return self.num_silver
        except Exception as exc:
            raise ValueError("process has not yet been executed") from exc

    def get_num_bronze(self):
        """(int) number fo bronze medals won by this country"""
        try:
            return self.num_bronze
        except Exception as exc:
            raise ValueError("process has not yet been executed") from exc

    def get_num_athletes(self):
        """(int) number of athletes that competed for this country"""
        try:
            return self.num_athletes
        except Exception as exc:
            raise ValueError("process has not yet been executed") from exc

    def get_usage_ratio():
        """Ratio of usage of the CountryResults command against all commands.

        Return:
            float: ratio of _country_results_counter by _processing_counter.
        """
        return float(CountryResults._country_results_counter
                / CountryResults._processing_counter)

    def __str__(self):
        return ""


class DeterminePlaces(ProcessResults):
    """Process the results of all athletes that compete in one event determining their place"""

    _determine_places_counter = 0

    def __init__(self, event):
        """
        Parameters:
             event (Event): event for which the processing is to occur
        """
        self._event = event

    def process(self):
        """
        Sort the athletes results for this event from best to worst
        (not that timed events a lower score is better, and
        for scored events a higher score is better) then
        give the appropriate result objects medals based on position.
        """
        super().process()
        DeterminePlaces._determine_places_counter += 1
        self._results = []
        for athlete in self._event.get_athletes():
            self._results.append([athlete, athlete.get_result(self._event)])
        if self._event.is_timed():
            self._results = sorted(sorted(self._results, key=lambda athlete: athlete[0].get_full_name()), key=lambda result: float(result[1].get_result()))
            self._results = [item[0] for item in self._results]
        elif not self._event.is_timed():
            self._results = sorted(sorted(self._results, key=lambda athlete: athlete[0].get_full_name()), key=lambda result: float(result[1].get_result()), reverse=True)
            self._results = [item[0] for item in self._results]
        self.place_counter = 0
        self.previous_result = Result(-1)
        for athlete in self._results:
            self.place_counter += 1
            if athlete.get_result(self._event).get_result() == self.previous_result.get_result():
                athlete.get_result(self._event).set_place(self.previous_result.get_place())
            else:
                athlete.get_result(self._event).set_place(self.place_counter)
                self.previous_result = athlete.get_result(self._event)

    def get_results(self):
        """"""
        try:
            return self._results
        except Exception as exc:
            raise ValueError("process has not yet been executed") from exc

    def get_usage_ratio():
        """Ratio of usage of the DeterminePlaces command against all commands.

        Return:
            float: ratio of _determine_places_counter by _processing_counter.
        """
        return float(DeterminePlaces._determine_places_counter
                / DeterminePlaces._processing_counter)

    def __str__(self):
        return ""



def demo_entities():
    """Simple test code to demonstrate using the entity classes.
       Output is to console.
    """
    TIMED = True
    SCORED = False

    print("Demonstrate creating country objects:")
    CAN = Country("Canada", "CAN")
    AUS = Country("Australia", "AUS")
    all_countries.add_item(CAN.get_country_code(), CAN)
    all_countries.add_item(AUS.get_country_code(), AUS)
    for country in all_countries.get_items():
        print(country)

    print("\nDemonstrate creating athlete objects, adding them to",
          "all_athletes and countries:")
    a1 = Athlete("1", "Athlete", "One", CAN)
    a2 = Athlete("2", "Athlete", "Two", CAN)
    a3 = Athlete("10", "Athlete", "Three", CAN)
    a4 = Athlete("4", "Athlete", "Four", AUS)
    a5 = Athlete("5", "Athlete", "Five", AUS)
    a6 = Athlete("20", "Athlete", "Six", AUS)
    for athlete in [a1, a2, a3, a4, a5, a6]:
        all_athletes.add_item(athlete.get_id(), athlete)
    athletes = all_athletes.get_items()
    for athlete in athletes:
        print(athlete)
    CAN.add_athletes([a1, a2, a3])
    AUS.add_athletes([a4, a5, a6])
    print("\nDemonstrate finding an athlete in all_athletes:")
    print(all_athletes.find_item("2"))

    # Create event objects and add athletes to the events.
    e1 = Event("Event1", TIMED, [a1, a2, a3, a4, a5])
    all_events.add_item(e1.get_name(), e1)
    a2.add_event(e1)
    a3.add_event(e1)
    a4.add_event(e1)
    a5.add_event(e1)
    e2 = Event("Event2", SCORED, [a1, a2, a3, a5, a6])
    all_events.add_item(e2.get_name(), e2)
    a2.add_event(e2)
    a3.add_event(e2)
    a5.add_event(e2)
    a6.add_event(e2)
    a1.add_events([e1, e2])

    # Create result objects for each athlete in the events.
    a1.add_result(e1, Result(10.5))
    a2.add_result(e1, Result(9.5))
    a3.add_result(e1, Result(11.5))
    a4.add_result(e1, Result(8.5))
    a5.add_result(e1, Result(12.5))

    a1.add_result(e2, Result(100.5))
    a2.add_result(e2, Result(99.5))
    a3.add_result(e2, Result(98.5))
    a5.add_result(e2, Result(90.5))
    a6.add_result(e2, Result(89.5))


def demo_processing():
    """Simple test code to demonstrate using the processing classes.
       Output is to console.
    """
    print("\n\nDemonstrate processing of results:")
    for athlete in all_athletes.get_items():
        athlete_results = AthleteResults(athlete)
        athlete_results.process()
        results = athlete_results.get_results()
        print(results)
        # Do something with this athlete's results.

    print("\nDemonstrate listing the results for an event:")
    event = all_events.find_item("Event1")
    results_dict = {}
    for athlete in event.get_athletes():
        results_dict[athlete.get_result(event).get_result()] = \
            athlete.get_result(event)
    for result in sorted(results_dict):
        print(result)

    print("\nAthleteResults was used",
          "{0:.1%}".format(AthleteResults.get_usage_ratio()),
          "of the time of all results processing commands.")


if __name__ == "__main__":
#    demo_entities()
#    demo_processing()
    load_data("data_files/athletes.csv", "data_files/countries.csv", "data_files/events.csv", "data_files/timed_event_results.csv", "data_files/scored_event_results.csv")
    for country in all_countries.get_items():
        print(country)
    for athlete in all_athletes.get_items():
        print(athlete.get_full_name(), athlete.get_country(), athlete.get_events())
        for event in athlete.get_events():
            print("    ", event, athlete.get_result(event))
    for event in all_events.get_items():
        print(event.get_name(), event.is_timed(), event.get_athletes())
    DeterminePlaces(all_events.find_item("Women's Speedskating 1000m")).process()