from .destination_data import DESTINATIONS

def ai_travel_assistant(destination):

    if destination not in DESTINATIONS:
        return {}

    return DESTINATIONS[destination]