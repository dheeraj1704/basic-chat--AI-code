import random

# Dictionary of responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm doing well, how about you?", "Not too bad."],
    "goodbye": ["Goodbye!", "See you later!", "Farewell!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "default": ["I'm not sure how to respond.", "Could you please elaborate?", "I didn't quite catch that."],
}

# Function to get a response based on user input
def get_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if the input matches any predefined responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    # If no match is found, return a default response
    return random.choice(responses["default"])

# Main loop for chatting
print("Chatbot: Hi! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    response = get_response(user_input)
    print("Chatbot:", response)
