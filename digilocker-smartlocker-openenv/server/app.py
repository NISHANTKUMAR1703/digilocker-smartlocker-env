from fastapi import FastAPI
import uvicorn
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


# ✅ REQUIRED MAIN FUNCTION
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


# ✅ REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()
