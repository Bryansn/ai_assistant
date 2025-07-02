from ai_assistant import AIAssistant  # import base assistant class (inheritance)
from request import Request
from response import Response
from ai_generator import generate_ai_response  # import to get GPT response


# Inherits from AIAssitant,
# overrides greetUser, handleRequest, generateResponse
class FitnessAssistant(AIAssistant):
    def __init__(self):
        self.last_request = None  # remember the last request to reply to it later

    def greetUser(self) -> None:  # Print gretting message
        print("Hey there! I'm your Fitness Assistant. Let's crush your fitness goals!")

    def handleRequest(
        self, request: Request
    ) -> None:  # save and show the user fitness request
        print(f"Processing fitness request: '{request.input_text}'")
        self.last_request = request

    def generateResponse(
        self,
    ) -> Response:  # validate request and build prompt
        if self.last_request:
            prompt = (
                f"Suggest a workout plan based on: '{self.last_request.input_text}'"
            )
            message = generate_ai_response(prompt)

            # confidence score based on the goal mentioned
            goal_text = self.last_request.input_text.lower()
            if "strength" in goal_text:
                confidence = 0.95
            elif "cardio" in goal_text:
                confidence = 0.85
            else:
                confidence = 0.6

            # Return the response
            return Response(message, confidence=confidence, action_performed=True)
        else:
            # if no request is recived
            return Response(
                "No fitness request received yet.",
                confidence=0.2,
                action_performed=False,
            )
