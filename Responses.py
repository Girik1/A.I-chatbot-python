class Responses:
    def __init__(self):
        self.responses = {
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
    
    def getResponses(self):
        return self.responses

    def respondTo(self, token):
        return self.responses[token]

    def joke(self):
        return "not yet created"

    def getDefault(self):
        return self.responses["default"]

responses = Responses()