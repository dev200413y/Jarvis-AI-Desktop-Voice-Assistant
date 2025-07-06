# Jarvis-AI-Desktop-Voice-Assistant
# 🤖 Jarvis Voice Assistant (Python Project)

A beginner-friendly Python-based voice assistant named **Jarvis**, inspired by Iron Man's AI. This assistant can perform basic tasks like searching Wikipedia, opening websites, playing music, sending emails, and telling the time — all through voice commands.

## 🚀 Features

- 🎤 Voice-activated interaction using `speech_recognition`
- 🗣 Text-to-speech (TTS) with `pyttsx3`
- 🌐 Wikipedia search via voice
- 📺 Open YouTube, Google, Stack Overflow
- 🎶 Play local music files
- 🕒 Tell the current time
- 📧 Send emails using SMTP
- 📁 Open local applications like Visual Studio Code

## 🧠 Technologies Used

| Technology        | Purpose                           |
|-------------------|------------------------------------|
| `pyttsx3`         | Text-to-speech engine              |
| `speech_recognition` | Convert voice to text          |
| `wikipedia`       | Fetch data from Wikipedia          |
| `webbrowser`      | Launch browser links               |
| `datetime`        | Get current system time            |
| `os`              | Interact with local file system    |
| `smtplib`         | Send emails via Gmail              |

## ⚙️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/dev200413y/Jarvis-AI-Desktop-Voice-Assistant.git
   cd jarvis-voice-assistant
2.Install Dependencies
  pip install pyttsx3
  pip install SpeechRecognition
  pip install wikipedia   

3. Microphone Access
   Ensure your system microphone is working properly.
   Adjust microphone permissions if needed.


4. Update Email Credentials
   Replace 'YOUREMAIL@gmail.com' and 'your_password_here' in the code with your actual email and app password.
   Important: Use App Passwords if you have 2FA enabled.

5. Run the Assistant
   python jarvis.py. 
