from fastapi import FastAPI
from app.whatsapp import router

app = FastAPI(title="WhatsApp Voice AI")

app.include_router(router)

@app.get("/")
def health():
    return {"status": "Voice AI running"}
