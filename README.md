# ChatBot
# ChatBot
This is a simple chatbot.

If you want to have a chat in the terminal, then you can run Chat.py. If you want to use text-to-speech, then you can run VoiceChat.py. If you want to connect to the QQ robot, then you can run QBot.py. When running, please make sure you have opened Ollama, and replace the model and all the interface API Keys with your own. If you want to access the chat history, then you can delete the file "data.json". If you want to change the system prompt words, then please modify the "system.json" file. This project supports certain function_calls. When it detects that the model output contains "##function_calling", it will automatically invoke the tool. Currently, only a search engine has been integrated. If necessary, functions can be added and modified in functioncalling.py. However, the system prompt words I wrote are not very good. If needed, you can change the system prompt words by yourself.
