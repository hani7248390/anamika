from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Anamika chatbot is running"}

@app.get("/chat")
def chat(q: str):
    return {
        "question": q,
        "answer": f"Anamika says: {q} का जवाब अभी सिखाया जा रहा है"
    }
