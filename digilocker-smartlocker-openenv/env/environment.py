class DigiLockerEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        # Initial state
        self.state = {
            "user_id": "U123",
            "otp_verified": False,
            "face_verified": False,
            "risk_score": 0.3,
            "locker_status": "locked",
            "attempts": 0
        }
        return self.state

    def step(self, action):
        reward = 0.0
        done = False

        # Track attempts
        self.state["attempts"] += 1

        # ACTION LOGIC
        if action == "verify_otp":
            if not self.state["otp_verified"]:
                self.state["otp_verified"] = True
                reward += 0.2
            else:
                reward -= 0.05  # penalty for repeat

        elif action == "verify_face":
            if not self.state["face_verified"]:
                self.state["face_verified"] = True
                reward += 0.2
            else:
                reward -= 0.05

        elif action == "grant_access":
            if self.state["otp_verified"] and self.state["face_verified"]:
                self.state["locker_status"] = "unlocked"
                reward += 0.5
                done = True
            else:
                reward -= 0.3

        elif action == "deny_access":
            if self.state["risk_score"] > 0.7:
                reward += 0.3
                done = True
            else:
                reward -= 0.1

        elif action == "flag_suspicious":
            if self.state["risk_score"] > 0.5:
                reward += 0.2
            else:
                reward -= 0.05

        elif action == "log_activity":
            reward += 0.1

        else:
            reward -= 0.1  # invalid action

        # SMALL TIME PENALTY (to encourage efficiency)
        reward -= 0.01 * self.state["attempts"]

        return self.state, float(max(min(reward, 1.0), 0.0)), done, {}

    def get_state(self):
        return self.state
