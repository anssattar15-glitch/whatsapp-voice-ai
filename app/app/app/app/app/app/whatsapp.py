import requests
import uuid
from fastapi import APIRouter, Request
from twilio.twiml.messaging_response import MessagingResponse
from app.speech_to_text import transcribe_audio
from app.text_to_speech import generate_voice
from app.assistant import VoiceAIAssistant

router = APIRouter()
assistant = VoiceAIAssistant()

@router.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    num_media = int(form.get("NumMedia", 0))

    response = MessagingResponse()

    if num_media > 0:
        media_url = form.get("MediaUrl0")
        audio_file = f"/tmp/{uuid.uuid4()}.ogg"
        reply_audio = f"/tmp/{uuid.uuid4()}.mp3"

        audio_data = requests.get(media_url).content
        open(audio_file, "wb").write(audio_data)

        text = transcribe_audio(audio_file)
        ai_reply = assistant.respond(text)
        generate_voice(ai_reply, reply_audio)

        response.message().media(reply_audio)
    else:
        response.message("Please send a voice note 🎙️")

    return str(response)
