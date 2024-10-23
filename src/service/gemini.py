from dotenv import load_dotenv
import os
import google.generativeai as genai


class GeminiAPI:
    def __init__(self, api_key=None):
        load_dotenv()
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        self._configure_api()

    def _configure_api(self):
        if not self.api_key:
            raise ValueError("API key is missing.")
        genai.configure(api_key=self.api_key)

    def generate_content(self, prompt, maxtoken=8000, model_name='gemini-1.5-flash-latest'):
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(max_output_tokens=maxtoken)
        )

        if response.prompt_feedback.block_reason != response.prompt_feedback.BlockReason(0):
            return False, response.prompt_feedback
        return True, response.text
