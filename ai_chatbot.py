import random

class Chatbot:
    def __init__(self, name="Charlie"):
        self.name = name
        self.memory = None

    def respond(self, message):
        # Define the bot's responses
        responses = {
            "hi": [
                "Hey there! How's it going?",
                "Hi! What's up?",
                "Hello! What's new with you?"
            ],
            "how are you": [
                "I'm doing awesome, thanks for asking! How about you?",
                "I'm feeling great, thanks! How's your day going?",
                "All good on my end! How about you? :)"
            ],
            "bye": [
                "Goodbye! Catch you later!",
                "See you soon! Take care!",
                "Bye! Don't be a stranger!"
            ],
            "joke": [
                "Why don't skeletons fight each other? They don't have the guts!",
                "Why was the math book sad? Because it had too many problems!",
                "I told my computer I needed a break... It froze."
            ],
            "memory": [
                "Hmm, you just told me that earlier, but I'm happy to chat again! 🙂",
                "I remember you mentioned that! It's nice to talk again."
            ],
            "default": [
                "Hmm, I didn't quite catch that. Can you say that again?",
                "I'm still learning, but I'm sure we'll figure it out together.",
                "Sorry, I didn’t get that. Could you rephrase?"
            ]
        }

        # Handle memory: Recall what the user last said
        if message.lower() == "remember what I said?":
            return f"You mentioned: {self.memory}" if self.memory else "I don't remember anything yet. Tell me something!"
        
        # Save the last message in memory (unless the user says goodbye)
        if message.lower() != "bye":
            self.memory = message

        message = message.lower()
        # Try to match the message to a predefined key (like "hi" or "bye")
        for key in responses:
            if key in message:
                return random.choice(responses[key])
        
        # Default response if no match is found
        return random.choice(responses["default"])

def chat():
    bot = Chatbot()
    print(f"{bot.name}: Hey! I'm {bot.name}. What's on your mind?")

    while True:
        user_input = input("You: ")
        
        # Ending conversation if 'bye' is mentioned
        if "bye" in user_input.lower():
            print(f"{bot.name}: {random.choice(['Goodbye!', 'See you soon!', 'Take care!'])}")
            break
        
        # Handle joke request
        if "joke" in user_input.lower():
            response = bot.respond("joke")
        else:
            response = bot.respond(user_input)
        
        print(f"{bot.name}: {response}")

if __name__ == "__main__":
    chat()
