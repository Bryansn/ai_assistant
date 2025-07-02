class Response:
    # store the assistants reply, confidence
    def __init__(self, message: str, confidence: float, action_performed: bool):
        # Validate message
        if not isinstance(message, str) or not message.strip():
            raise ValueError("Message must be a non-empty string.")

        # Validate confidence
        if not isinstance(confidence, float) or not (0.0 <= confidence <= 1.0):
            raise ValueError("Confidence must be a float between 0.0 and 1.0.")

        # Validate action_performed
        if not isinstance(action_performed, bool):
            raise ValueError("action_performed must be a boolean value.")

        # store data inside object, can use later
        self.message = message
        self.confidence = confidence
        self.action_performed = action_performed

    # prints in nice format
    def __repr__(self):
        return (
            f"Response(message='{self.message}', "
            f"confidence={self.confidence}, action_performed={self.action_performed})"
        )
