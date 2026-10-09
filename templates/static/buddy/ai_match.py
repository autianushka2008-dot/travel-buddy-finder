def calculate_match(profile1, profile2):

    score = 0

    if profile1.city == profile2.city:
        score += 10

    if profile1.travel_style == profile2.travel_style:
        score += 20

    common = set(
        profile1.interests.lower().split(',')
    ) & set(
        profile2.interests.lower().split(',')
    )

    score += len(common) * 15

    if score > 100:
        score = 100

    return score