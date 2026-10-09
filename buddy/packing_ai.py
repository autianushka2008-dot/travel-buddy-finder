def packing_list(destination):

    hill_stations = [
        "Manali",
        "Shimla",
        "Kashmir",
        "Darjeeling",
        "Ooty"
    ]

    beaches = [
        "Goa"
    ]

    if destination in hill_stations:

        return [
            "Jacket",
            "Woolen Clothes",
            "Shoes",
            "Medicine Kit"
        ]

    elif destination in beaches:

        return [
            "Sunglasses",
            "Beach Wear",
            "Hat",
            "Sunscreen"
        ]

    return [
        "Mobile Charger",
        "Power Bank",
        "Shoes",
        "Medicine Kit"
    ]