# buddy/travel_ai.py

def recommend_trip(budget):

    if budget < 5000:
        return "Lonavala"

    elif budget < 15000:
        return "Goa"

    elif budget < 30000:
        return "Manali"

    return "Kashmir"