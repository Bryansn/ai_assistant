from datetime import datetime
from user_profile import UserProfile
from request import Request, CommandType
from music_assistant import MusicAssistant
from fitness_assistant import FitnessAssistant
from ai_assistant import AIAssistant

print(">>> Running AI Assistant Simulation <<<\n")

# Collect user info
name = input("Enter your name: ")
age = int(input("Enter your age: "))
task = input("What do you need help with? (music/fitness): ").strip().lower()

if task == "music":
    mood = input("What mood are you in? (e.g., chill, sad): ")
    user = UserProfile(name, age, {"mood": mood}, True)
    request = Request(f"play {mood} music", datetime.now(), CommandType.SEARCH)
    assistant = MusicAssistant()

elif task == "fitness":
    goal = input("What is your fitness goal? (e.g., strength, cardio): ")
    user = UserProfile(name, age, {"goal": goal}, False)
    request = Request(f"{goal} workout", datetime.now(), CommandType.SEARCH)
    assistant = FitnessAssistant()

else:
    print("Sorry, I can only help with 'music' or 'fitness'.")
    exit()

# Run interaction
print(f"\n--- Interacting with {user.name} ---")
assistant.greetUser()
assistant.handleRequest(request)
response = assistant.generateResponse()
print(f"\nAssistant Response: {response}")
