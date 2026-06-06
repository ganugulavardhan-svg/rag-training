from agent import agent
from vectorstore import load_documents

load_documents()

chat_history = []

print("Assistant Ready!")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    chat_history.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = agent.invoke(
        {
            "messages": chat_history
        }
    )

    assistant_message = response[
        "messages"
    ][-1].content

    print(
        "\nAssistant:",
        assistant_message
    )

    chat_history.append(
        {
            "role": "assistant",
            "content": assistant_message
        }
    )