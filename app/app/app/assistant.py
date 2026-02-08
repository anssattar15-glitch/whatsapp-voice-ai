import openai
from app.config import settings

openai.api_key = settings.OPENAI_API_KEY

class VoiceAIAssistant:
    def __init__(self):
        self.system_prompt = "You are a friendly WhatsApp voice assistant."

    def respond(self, user_text: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_text}
            ]
        )
        return response.choices[0].message.content
