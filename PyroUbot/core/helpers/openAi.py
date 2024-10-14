import asyncio

import requests 
import openai

from PyroUbot import AI_GOOGLE_API

class OpenAi:
    @staticmethod
    async def google_ai(question):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key={AI_GOOGLE_API}"
        payload = {"contents": [{"role": "user", "parts": [{"text": question}]}], "generationConfig": {"temperature": 1, "topK": 0, "topP": 0.95, "maxOutputTokens": 8192, "stopSequences": []}}
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return f"Failed to generate content. Status code: {response.status_code}"

    @staticmethod
    async def ImageDalle(question):
        response = await asyncio.to_thread(
            openai.Image.create,
            prompt=question,
            n=1,
        )
        return response["data"][0]["url"]

    @staticmethod
    async def SpeechToText(file):
        audio_file = open(file, "rb")
        response = await asyncio.to_thread(openai.Audio.transcribe, "whisper-1", audio_file)
        return response["text"]
