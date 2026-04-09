from env.environment import DigiLockerEnv

env = DigiLockerEnv()
state = env.reset()

actions = ["verify_otp", "verify_face", "grant_access"]

total_reward = 0

for action in actions:
    state, reward, done, _ = env.step(action)
    total_reward += reward
    if done:
        break

print("Final Score:", total_reward)
