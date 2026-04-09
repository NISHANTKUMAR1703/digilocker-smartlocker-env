def grade(state):
    """
    Grades the final state of the environment.
    Returns a score between 0.0 and 1.0
    """

    score = 0.0

    # 1. OTP Verification (partial reward)
    if state.get("otp_verified"):
        score += 0.3

    # 2. Face Verification (partial reward)
    if state.get("face_verified"):
        score += 0.3

    # 3. Access Control (final success)
    if state.get("locker_status") == "unlocked":
        score += 0.4

    # Ensure score is within range
    return float(min(score, 1.0))
