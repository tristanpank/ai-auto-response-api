from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import openai

load_dotenv()
API_KEY = os.getenv("API_KEY")

print(API_KEY)

openai.api_key = API_KEY

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

class Convo(BaseModel):
  context: list[dict]
  message: dict

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello World!"}

@app.get("/gpt")
def root(convo: Convo):
  messages = [*convo.context, convo.message]
  chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
  return chat_completion