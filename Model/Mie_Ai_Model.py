import os
import json
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

class MieAIModel:
    def __init__(self, temperature=0.5, top_p=0.95, top_k=64, max_output_tokens=256):
        os.environ["API_KEY"] = "AIzaSyBi9KLhDqqLnG0MU5rwUs4ZpXIEgJ7Gn1E"
        genai.configure(api_key=os.environ["API_KEY"])
        
        self.generation_config = {
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
            "max_output_tokens": max_output_tokens,
        }
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            safety_settings={
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            },
            generation_config=self.generation_config,
        )

    def call_ai(self, input_text):
        response = self.model.generate_content([
            """ช่วย role play เป็นตัวละครนี้ : Mie Ai """,
            f"input: {input_text}",
            "output: ",
            ])
        
        return response.text