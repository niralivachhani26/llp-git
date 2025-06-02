# app/chatbot/chatbot_processor.py

from .test_intent_main import process_message  # Note the dot (.) before test_intent_main

def get_chatbot_response(message):
    try:
        response = process_message(message)
        return response
    except Exception as e:
        return f"Error processing message: {str(e)}"
