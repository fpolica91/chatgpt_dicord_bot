from revChatGPT.revChatGPT import Chatbot
import os

SESSION_TOKEN = os.getenv("CHATGPT_SESSION_TOKEN")

config = {"Authorization": '<Auth>', "session_token": SESSION_TOKEN}

chatbot = Chatbot(config, conversation_id=None)
chatbot.refresh_session()


def handle_response(message) -> str:
    prompt = message
    response = chatbot.get_chat_response(prompt)
    responseMessage = response["message"]

    return responseMessage
