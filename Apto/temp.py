def classify_message_type(text):
    # This function classifies the message type based on keywords.
    # Modify this function as needed to improve classification accuracy.
    if "send image of" in text:
        return "image"
    return "text"