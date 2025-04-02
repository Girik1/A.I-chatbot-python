import random
import sys
from Responses import responses

class Chatbot:
    def __init__(self, name="Charlie"):
        self.name = name
        self.memory = None

    def respond(self, message):
        # Define the bot's responses
        message = message.lower()

        if message == "remember what I said?": # Handle memory: Recall what the user last said
            return f"You mentioned: {self.memory}" if self.memory else "I don't remember anything yet. Tell me something!"
        elif message == "joke":
            print(responses.joke())

        # Save the last message in memory (unless the user says goodbye)
        if message != "bye":
            self.memory = message

        try:
            print(self.name + ": " + responses.respondTo(message)[random.randint(0, len(responses.respondTo(message))-1)])
        except:
            print(self.name + ": " + responses.getDefault()[random.randint(0, len(responses.getDefault())-1)])
        
        if message == "bye":
            sys.exit()

def chat():
    bot = Chatbot()
    print(f"{bot.name}: Hey! I'm {bot.name}. What's on your mind?")

    while True:
        user_input = input("You: ")

        bot.respond(user_input)

if __name__ == "__main__":
    chat()
