from fastapi import FastAPI
from chatbot import chatbot

app = FastAPI()

@app.get("/chat")

def chat(message: str):

    response = chatbot(message)

    return {"response": response}