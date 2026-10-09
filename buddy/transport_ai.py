from .destination_data import DESTINATIONS

def get_transport(destination):

    if destination in DESTINATIONS:

        return DESTINATIONS[destination].get(
            "transport",
            {}
        )

    return {}