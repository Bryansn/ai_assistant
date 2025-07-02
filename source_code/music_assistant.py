from ai_assistant import (
    AIAssistant,
)  # base class for all assistants
from request import Request
from response import Response
from ai_generator import generate_ai_response


# inherits from AIAssistant and handles music related request
class MusicAssistant(AIAssistant):
    def __init__(self):  # remember last user request
        self.last_request = None

    def greetUser(self) -> None:  # greet user
        print("🎵 Hey! I'm your Music Assistant. Ready to set the vibe?")

    def handleRequest(
        self, request: Request
    ) -> None:  # save and show the users request
        print(f"Received music request: '{request.input_text}'")
        self.last_request = request

    def generateResponse(self) -> Response:  # validate request and respond
        if self.last_request:
            mood_text = self.last_request.input_text.lower()  # check for key words

            # Use GPT to generate a playlist suggestion
            prompt = f"Suggest a music playlist for this request: '{self.last_request.input_text}'"
            message = generate_ai_response(prompt)

            # Confidence logic based on known moods/genres
            if "happy" in mood_text or "chill" in mood_text:
                confidence = 0.95
            elif "sad" in mood_text or "focus" in mood_text:
                confidence = 0.85
            else:
                confidence = 0.6  # uncertain mood/genre

            # return GPT response with confidence score
            return Response(message, confidence=confidence, action_performed=True)
        # if no request
        else:
            return Response(
                "I haven't received any music request yet.",
                confidence=0.2,
                action_performed=False,
            )
