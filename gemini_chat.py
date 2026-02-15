from google import genai

client = genai.Client(api_key="apikey")

chat = client.chats.create(
    model="gemini-3-flash-preview"
)

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("GoodBye!!")
        break

    response = chat.send_message(user_input)
    print("Gemini:", response.text)
