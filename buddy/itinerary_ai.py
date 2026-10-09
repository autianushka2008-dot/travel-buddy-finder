from .destination_data import DESTINATIONS

def generate_itinerary(destination):

    if destination not in DESTINATIONS:
        return {}

    places = DESTINATIONS[destination].get(
        "places",
        []
    )

    return {

        "Day 1": places[:2],

        "Day 2": places[2:4],

        "Day 3": [
            "Local Food Tour",
            "Shopping",
            "Photography"
        ]
    }