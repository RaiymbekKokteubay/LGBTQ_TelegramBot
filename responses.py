def sample_responses(input_text):
    user_message = str(input_text).lower()
    if user_message in ("start", "hello"):
        return "Hey! Press the button to start"
    if user_message in ("help", "help!"):
        return "bots mission"
    return "I did not understand."