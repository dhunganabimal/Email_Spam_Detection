from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_spam
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# origins = [
#
#     "http://127.0.0.1:5500/frontend/index.html"
#     "http://127.0.0.1:5500"
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Email(BaseModel):
    sender: str
    subject: str
    body: str

@app.get("/")
def home():
    return {"message": "Spam API running 🚀"}

@app.post("/predict")
def predict(email: Email):
    return predict_spam(
        email.sender,
        email.subject,
        email.body
    )
