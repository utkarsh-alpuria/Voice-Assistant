# Voice-Assistant

**Voice-Assistant** is an intelligent AI application designed for voice interactions through commands. It features a Python backend with a frontend crafted using JavaScript, HTML, and CSS.

![Voice Assistant Readme Cover](https://github.com/utkarsh-alpuria/Voice-Assistant/blob/main/web/assets/Voice%20Assistant%20Readme%20Cover%20Img.png)


## Project Structure 📁

- **`main.py`**: The entry point of the application that initializes and runs the Python Eel module.
- **`requirements.txt`**: Lists the dependencies required for the application.

### Backend 🛠️

- **`wake_word_detect.py`**: Manages wake word detection for the initial screen.
- **`listener_thread.py`**: Listens for the designated wake word ("Hey Jarvis").
- **`speech_to_text.py`**: Handles speech-to-text conversion for the chat window.
- **`.env`**: Stores environment variables such as API keys securely.

### Web 🌐

- **`main.html`**: Provides the HTML structure for both the wake word detection and chat screens.
- **`wake_word_detect.css`**: Styles the wake word detection screen.
- **`speech_to_text_chat.css`**: Styles the chat window screen.
- **`wake_word_detect.js`**: JavaScript code for integrating the frontend with backend wake word detection.
- **`speech_to_text_chat.js`**: JavaScript code for connecting the chat window with backend functionalities.

## Getting Started 🚀

1. **Install Python**: Ensure Python is installed on your machine.
2. **Clone Repository**: Clone the project repository or download the ZIP file.
3. **Open Project**: Open the project folder in your preferred code editor or IDE.
4. **Create Virtual Environment**: Run `python -m venv <name_of_virtual_environment>`.
5. **Activate Environment**: Activate the virtual environment with:
   - **Windows**: `.\<name_of_virtual_environment>\Scripts\activate`
   - **macOS/Linux**: `source <name_of_virtual_environment>/bin/activate`
6. **Install Dependencies**: Run `pip install -r requirements.txt` to install project dependencies.
7. **Obtain API Key**: Sign up on [Cohere](https://cohere.com/) and get your personal API key.
8. **Configure API Key**: Replace `"your Cohere API key"` in the `.env` file with your API key and save the changes.
9. **Run Application**: Execute `python main.py` in your terminal to start the application.
10. **Interact**: Enjoy using the Voice-Assistant application.

## How To Use 🗣️

1. **Loading Time**: The application may take 0.5-1 minute to load depending on your machine’s specifications.
2. **Wake Word Detection**: On launch, click the microphone button 🎤. Wait for the text "Listening" to appear.
3. **Activate Assistant**: When "Listening" is visible, say the wake word ("Hey Jarvis"). The text will change to "Jarvis Active," and you’ll hear "Jarvis Activated!" 🔊
4. **Chat Window**: You’ll be directed to the chat window with a welcome message: "Welcome! How can I help you?" 💬
5. **Voice Conversation**: Click the microphone button at the bottom of the chat window to start a voice conversation. Speak your query when prompted with "Ask..." 🗨️
6. **Pause/Resume Conversation**: To pause, say "Thank you and goodbye." The system will respond with "Goodbye!" and pause the conversation. Resume by clicking the microphone button again. 🔄
7. **Text Conversation**: Alternatively, type your query in the message input and press the send button or hit Enter. Text responses are faster. 📝
8. **Polite Responses**: The bot is programmed to respond politely, only interacting when spoken to or texted. 😊
