import openai
from app.config import settings

openai.api_key = settings.OPENAI_API_KEY

def transcribe_audio(audio_path: str) -> str:
    with open(audio_path, "rb") as audio:
        result = openai.Audio.transcribe(
            model="whisper-1",
            file=audio
        )
    return result["text"]
