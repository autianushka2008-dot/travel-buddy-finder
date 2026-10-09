import importlib

try:
    geodesic = importlib.import_module("geopy.distance").geodesic
except ImportError:
    # Fallback haversine implementation returning an object with .km
    from math import radians, sin, cos, asin, sqrt

    class _Dist:
        def __init__(self, km):
            self.km = km

    def geodesic(a, b):
        # a and b are (lat, lon)
        lat1, lon1 = map(radians, a)
        lat2, lon2 = map(radians, b)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        hav = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
        r = 6371.0
        return _Dist(2 * r * asin(sqrt(hav)))


def interest_score(i1, i2):
    set1 = set(i1.lower().split(","))
    set2 = set(i2.lower().split(","))
    return len(set1 & set2) / max(len(set1 | set2), 1)


def location_score(u1, u2):
    dist = geodesic((u1.profile.lat, u1.profile.lng),
                    (u2.profile.lat, u2.profile.lng)).km

    if dist < 50:
        return 1
    elif dist < 200:
        return 0.6
    return 0.2


def ai_match(user1, user2):
    score = 0
    score += interest_score(user1.profile.interests, user2.profile.interests) * 50
    score += location_score(user1, user2) * 30
    score += 20
    return round(score, 2)
# buddy/utils.py

def split_expense(total, members):
    return round(total / members, 2)