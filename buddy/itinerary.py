def generate_itinerary(destination):

    plans = {

        "Goa": [
            "Beach",
            "Water Sports",
            "Night Market"
        ],

        "Manali": [
            "Solang Valley",
            "Snow Point",
            "Mall Road"
        ]
    }

    return plans.get(
        destination,
        ["Explore City"]
    )