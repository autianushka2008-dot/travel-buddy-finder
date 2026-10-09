def calculate_match(profile1, profile2):

    score = 0

    if profile1.travel_style == profile2.travel_style:
        score += 40

    if profile1.city == profile2.city:
        score += 20

    if abs(profile1.budget - profile2.budget) <= 5000:
        score += 20

    common_interests = len(
        set(profile1.interests.split(','))
        &
        set(profile2.interests.split(','))
    )

    score += common_interests * 5

    return min(score, 100)