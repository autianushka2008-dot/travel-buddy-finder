from .destination_data import DESTINATIONS

def get_restaurants(destination):

    if destination in DESTINATIONS:

        return {
            "restaurants": DESTINATIONS[destination]["restaurants"],
            "food": DESTINATIONS[destination]["food"]
        }

    return {
        "restaurants": [],
        "food": []
    }