from .destination_data import DESTINATIONS

def get_weather(destination):

    if destination in DESTINATIONS:
        return DESTINATIONS[destination]["weather"]

    return "Weather information unavailable"