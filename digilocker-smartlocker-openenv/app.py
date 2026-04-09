from fastapi import FastAPI
from env.environment import DigiLockerEnv

app = FastAPI()

env = DigiLockerEnv()

@app.post("/reset")
def reset():
    return {"state": env.reset()}

@app.post("/step")
def step(action: str):
    state, reward, done, _ = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }

@app.get("/")
def root():
    return {"message": "DigiLocker SmartLocker Env Running"}
