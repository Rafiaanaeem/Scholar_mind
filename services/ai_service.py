import time
import logging
from groq import Groq
from config.settings import settings

logger = logging.getLogger(__name__)

class AIService:
    """Handles interactions with the Groq LLM API."""

    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.model_name = getattr(settings, 'GROQ_MODEL', 'llama3-8b-8192') 

    def _make_api_call(self, prompt: str) -> str:
        """Internal method to handle the API call with exponential backoff."""
        max_retries = 3
        
        for attempt in range(max_retries):
            try:
                completion = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": "You are an expert academic research assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.4,
                )
                return completion.choices[0].message.content
                
            except Exception as e:
                logger.error(f"Groq API Error on attempt {attempt + 1}: {str(e)}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  
                else:
                    logger.error("Max retries reached. AI request failed.")
                    return f"Error: Unable to generate response from Groq. Details: {str(e)}"

    def generate_topics(self, field_of_study: str) -> str:
        """Generates a list of 5 trending research topics."""
        prompt = f"Act as an expert academic advisor. Generate a list of 5 trending, highly relevant research topics in the field of: '{field_of_study}'. Present them as a clean, bulleted Markdown list."
        return self._make_api_call(prompt)

    def generate_research_package(self, topic: str) -> str:
        """Generates a comprehensive research foundation."""
        prompt = f"""Act as a senior researcher. Generate a comprehensive research foundation for the topic: '{topic}'.
        Format the output strictly in Markdown with the exact following headers:
        ## Executive Summary
        ## Research Questions
        ## Literature Review Focus
        ## Proposed Methodology
        ## Future Directions
        """
        return self._make_api_call(prompt)