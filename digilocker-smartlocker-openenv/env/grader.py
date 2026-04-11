def grade(state):
    score = 0.0

    if state.get("otp_verified"):
        score += 0.3

    if state.get("face_verified"):
        score += 0.3

    if state.get("locker_status") == "unlocked":
        score += 0.3

    # Keep score strictly between 0 and 1
    score = max(0.1, min(score, 0.9))

    return float(score)
