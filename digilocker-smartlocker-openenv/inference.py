from env.environment import DigiLockerEnv
from env.grader import grade

env = DigiLockerEnv()

# -------- TASK NAME --------
task_name = "hard_security"

# -------- START --------
print(f"[START] task={task_name}", flush=True)

state = env.reset()
total_reward = 0
steps = 0

actions = ["verify_otp", "verify_face", "grant_access"]

for i, action in enumerate(actions, start=1):
    state, reward, done, _ = env.step(action)
    total_reward += reward
    steps += 1

    # -------- STEP --------
    print(f"[STEP] step={i} reward={reward:.2f}", flush=True)

    if done:
        break

# -------- FINAL SCORE --------
score = grade(state)

# -------- END --------
print(f"[END] task={task_name} score={score:.2f} steps={steps}", flush=True)
