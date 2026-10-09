def get_hotels(destination):

    hotels = {

        "Goa": [
            {"name": "Taj Resort Goa", "rating": "4.8 ⭐", "price": "₹6000/night"},
            {"name": "Holiday Inn Goa", "rating": "4.5 ⭐", "price": "₹4500/night"},
            {"name": "The Leela Goa", "rating": "4.9 ⭐", "price": "₹8500/night"}
        ],

        "Pune": [
            {"name": "JW Marriott Pune", "rating": "4.9 ⭐", "price": "₹7000/night"},
            {"name": "Conrad Pune", "rating": "4.8 ⭐", "price": "₹6500/night"},
            {"name": "Hyatt Pune", "rating": "4.6 ⭐", "price": "₹5500/night"}
        ],

        "Mumbai": [
            {"name": "Taj Mahal Palace", "rating": "4.9 ⭐", "price": "₹10000/night"},
            {"name": "The Oberoi Mumbai", "rating": "4.8 ⭐", "price": "₹9000/night"},
            {"name": "Trident Nariman Point", "rating": "4.7 ⭐", "price": "₹7500/night"}
        ],

        "Delhi": [
            {"name": "The Leela Palace", "rating": "4.9 ⭐", "price": "₹9500/night"},
            {"name": "ITC Maurya", "rating": "4.8 ⭐", "price": "₹8500/night"},
            {"name": "Taj Palace", "rating": "4.7 ⭐", "price": "₹8000/night"}
        ],

        "Jaipur": [
            {"name": "Rambagh Palace", "rating": "5.0 ⭐", "price": "₹12000/night"},
            {"name": "ITC Rajputana", "rating": "4.8 ⭐", "price": "₹7000/night"},
            {"name": "Hilton Jaipur", "rating": "4.6 ⭐", "price": "₹5000/night"}
        ],

        "Udaipur": [
            {"name": "Taj Lake Palace", "rating": "5.0 ⭐", "price": "₹15000/night"},
            {"name": "Trident Udaipur", "rating": "4.8 ⭐", "price": "₹6500/night"},
            {"name": "Fateh Garh", "rating": "4.7 ⭐", "price": "₹6000/night"}
        ],

        "Manali": [
            {"name": "Snow Valley Resort", "rating": "4.6 ⭐", "price": "₹4000/night"},
            {"name": "Manali Heights", "rating": "4.7 ⭐", "price": "₹4500/night"},
            {"name": "The Orchard Greens", "rating": "4.5 ⭐", "price": "₹3500/night"}
        ],

        "Shimla": [
            {"name": "The Oberoi Cecil", "rating": "4.9 ⭐", "price": "₹8500/night"},
            {"name": "Radisson Shimla", "rating": "4.7 ⭐", "price": "₹6500/night"},
            {"name": "Snow Valley Shimla", "rating": "4.5 ⭐", "price": "₹4000/night"}
        ],

        "Kashmir": [
            {"name": "Khyber Resort", "rating": "5.0 ⭐", "price": "₹12000/night"},
            {"name": "Radisson Srinagar", "rating": "4.7 ⭐", "price": "₹7000/night"},
            {"name": "Hotel Pine Spring", "rating": "4.5 ⭐", "price": "₹4500/night"}
        ],

        "Lonavala": [
            {"name": "Della Resorts", "rating": "4.8 ⭐", "price": "₹9000/night"},
            {"name": "Fariyas Resort", "rating": "4.6 ⭐", "price": "₹6500/night"},
            {"name": "Upper Deck Resort", "rating": "4.5 ⭐", "price": "₹5000/night"}
        ],

        "Mahabaleshwar": [
            {"name": "Evershine Resort", "rating": "4.7 ⭐", "price": "₹5500/night"},
            {"name": "Le Meridien", "rating": "4.8 ⭐", "price": "₹7000/night"},
            {"name": "Brightland Resort", "rating": "4.5 ⭐", "price": "₹4500/night"}
        ],

        "Bangalore": [
            {"name": "The Leela Palace", "rating": "4.9 ⭐", "price": "₹8500/night"},
            {"name": "Taj West End", "rating": "4.8 ⭐", "price": "₹8000/night"},
            {"name": "ITC Gardenia", "rating": "4.7 ⭐", "price": "₹7500/night"}
        ],

        "Hyderabad": [
            {"name": "Taj Falaknuma", "rating": "5.0 ⭐", "price": "₹15000/night"},
            {"name": "Park Hyatt", "rating": "4.8 ⭐", "price": "₹9000/night"},
            {"name": "Novotel HICC", "rating": "4.6 ⭐", "price": "₹6000/night"}
        ],

        "Chennai": [
            {"name": "ITC Grand Chola", "rating": "4.9 ⭐", "price": "₹9000/night"},
            {"name": "Taj Coromandel", "rating": "4.8 ⭐", "price": "₹8500/night"},
            {"name": "Hyatt Regency", "rating": "4.6 ⭐", "price": "₹7000/night"}
        ],

        "Kolkata": [
            {"name": "ITC Royal Bengal", "rating": "4.9 ⭐", "price": "₹8500/night"},
            {"name": "Taj Bengal", "rating": "4.8 ⭐", "price": "₹8000/night"},
            {"name": "The Oberoi Grand", "rating": "4.7 ⭐", "price": "₹7000/night"}
        ],

        "Agra": [
            {"name": "Oberoi Amarvilas", "rating": "5.0 ⭐", "price": "₹14000/night"},
            {"name": "ITC Mughal", "rating": "4.8 ⭐", "price": "₹7000/night"},
            {"name": "Taj Hotel Agra", "rating": "4.6 ⭐", "price": "₹5000/night"}
        ],

        "Rishikesh": [
            {"name": "Aloha on the Ganges", "rating": "4.8 ⭐", "price": "₹6000/night"},
            {"name": "Ganga Kinare", "rating": "4.7 ⭐", "price": "₹5500/night"},
            {"name": "Divine Resort", "rating": "4.5 ⭐", "price": "₹4000/night"}
        ],

        "Darjeeling": [
            {"name": "Mayfair Darjeeling", "rating": "4.9 ⭐", "price": "₹7000/night"},
            {"name": "The Elgin", "rating": "4.8 ⭐", "price": "₹6500/night"},
            {"name": "Summit Swiss", "rating": "4.5 ⭐", "price": "₹4000/night"}
        ],

        "Mysore": [
            {"name": "Radisson Blu Mysore", "rating": "4.8 ⭐", "price": "₹6000/night"},
            {"name": "Fortune JP Palace", "rating": "4.6 ⭐", "price": "₹4500/night"},
            {"name": "Royal Orchid", "rating": "4.5 ⭐", "price": "₹4000/night"}
        ],

        "Ooty": [
            {"name": "Savoy Ooty", "rating": "4.8 ⭐", "price": "₹6500/night"},
            {"name": "Sterling Ooty", "rating": "4.6 ⭐", "price": "₹5000/night"},
            {"name": "Gem Park", "rating": "4.5 ⭐", "price": "₹4500/night"}
        ]
    }

    return hotels.get(destination, [])