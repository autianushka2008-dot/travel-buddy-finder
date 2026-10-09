from .destination_data import DESTINATIONS

def get_places(destination):

    if destination in DESTINATIONS:

        return DESTINATIONS[destination].get(
            "places",
            []
        )

    return []