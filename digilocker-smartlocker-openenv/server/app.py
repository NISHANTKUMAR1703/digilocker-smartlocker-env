from fastapi import FastAPI
from env.environment import DigiLockerEnv

app = FastAPI()

env = DigiLockerEnv()

@app.post("/reset")
def reset():
    return {"state": env.reset()}

@app.post("/step")
def step(action: dict):
    action_value = action.get("action", "")
    state, reward, done, _ = env.step(action_value)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }

@app.get("/")
def root():
    return {"status": "running"}
