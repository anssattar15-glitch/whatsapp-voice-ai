import openai
from pathlib import Path
from app.config import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_voice(text: str, output_path: str):
    speech = openai.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text
    )
    Path(output_path).write_bytes(speech)
