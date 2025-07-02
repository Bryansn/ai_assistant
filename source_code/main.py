from datetime import datetime  # used to add timestamps to request
from user_profile import UserProfile  # user info like name, age, goal
from request import Request, CommandType
from music_assistant import MusicAssistant
from fitness_assistant import FitnessAssistant
from ai_assistant import AIAssistant

print(">>> Running AI Assistant Simulation with Confidence Scoring <<<\n")

# Create users with different moods and goals
user1 = UserProfile("Alice", 24, {"mood": "chill"}, True)
user2 = UserProfile("Bob", 30, {"goal": "strength"}, False)
user3 = UserProfile("Clara", 21, {"mood": "sad"}, True)
user4 = UserProfile("David", 28, {"goal": "just move"}, False)

# Create requests based on their preferences
request1 = Request("play chill music", datetime.now(), CommandType.SEARCH)
request2 = Request("strength training workout", datetime.now(), CommandType.SEARCH)
request3 = Request("play sad focus playlist", datetime.now(), CommandType.SEARCH)
request4 = Request("give me something active", datetime.now(), CommandType.SEARCH)

# Create assistants
assistant1 = MusicAssistant()
assistant2 = FitnessAssistant()
assistant3 = MusicAssistant()
assistant4 = FitnessAssistant()

# Step 4: Pair users, requests, and assistants
assistants = [assistant1, assistant2, assistant3, assistant4]
users = [user1, user2, user3, user4]
requests = [request1, request2, request3, request4]

# Step 5: Simulate interactions
for assistant, user, req in zip(assistants, users, requests):
    print(f"--- Interacting with {user.name} ---")
    assistant.greetUser()
    assistant.handleRequest(req)
    response = assistant.generateResponse()
    print(f"Assistant Response: {response}\n")
