def calculate_reward(prev_state, current_state, action):
    """
    Computes step-wise reward (0.0 to 1.0)
    based on progress between previous and current state.
    """

    reward = 0.0

    # 1. OTP verification reward
    if (not prev_state.get("otp_verified") 
        and current_state.get("otp_verified")):
        reward += 0.2

    # 2. Face verification reward
    if (not prev_state.get("face_verified") 
        and current_state.get("face_verified")):
        reward += 0.2

    # 3. Successful access reward
    if (prev_state.get("locker_status") != "unlocked" 
        and current_state.get("locker_status") == "unlocked"):
        reward += 0.5

    # 4. Security handling (deny suspicious user)
    if action == "deny_access" and current_state.get("risk_score", 0) > 0.7:
        reward += 0.3

    # 5. Logging activity (small reward)
    if action == "log_activity":
        reward += 0.1

    # 6. Penalty for unnecessary/repeated actions
    if action in ["verify_otp", "verify_face"]:
        if prev_state.get(action.split("_")[1] + "_verified"):
            reward -= 0.05

    # 7. Time/efficiency penalty
    attempts = current_state.get("attempts", 1)
    reward -= 0.01 * attempts

    # Clip reward between 0 and 1
    reward = max(0.0, min(1.0, reward))

    return float(reward)
