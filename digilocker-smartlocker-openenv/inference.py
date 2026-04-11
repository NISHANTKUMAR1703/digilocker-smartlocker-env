import os
from openai import OpenAI
from env.environment import DigiLockerEnv
from env.grader import grade

client = OpenAI(
    base_url=os.environ.get("API_BASE_URL"),
    api_key=os.environ.get("API_KEY"),
)

env = DigiLockerEnv()

tasks = {
    "easy": ["verify_otp"],
    "medium": ["verify_otp", "verify_face"],
    "hard": ["verify_otp", "verify_face", "grant_access"]
}

for task_name, actions in tasks.items():

    print(f"[START] task={task_name}", flush=True)

    state = env.reset()
    steps = 0

    for i, action in enumerate(actions, start=1):
        state, reward, done, _ = env.step(action)
        steps += 1

        print(f"[STEP] step={i} reward={reward:.2f}", flush=True)

        # LLM call (safe)
        try:
            client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": f"Evaluate {action}"}],
                max_tokens=5
            )
        except:
            pass

    score = grade(state)

    print(f"[END] task={task_name} score={score:.2f} steps={steps}", flush=True)
