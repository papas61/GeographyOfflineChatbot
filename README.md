# 🌍 Geography Chatbot

An offline AI-powered Geography Chatbot built with **Python**, **Tkinter**, and **Sentence Transformers**.

The chatbot uses semantic search instead of simple keyword matching, allowing it to understand geography-related questions in a more natural way.

---

## ✨ Features

✅ Fully Offline Operation

✅ AI-Powered Semantic Search

✅ Modern Desktop GUI

✅ Natural Language Understanding

✅ Fast Responses

✅ Expandable Knowledge Base

✅ Confidence Score Display

✅ No Internet Required

✅ No API Keys Needed

✅ Cross-Platform Support

---

## 🧠 How It Works

The chatbot uses the **all-MiniLM-L6-v2** Sentence Transformer model to convert questions into numerical embeddings.

When a user asks a question:

1. 📝 The question is converted into an embedding.
2. 🔍 Cosine similarity is calculated against all stored geography questions.
3. 🎯 The most similar question is selected.
4. 💬 The matching answer is displayed.
5. ⚠️ If confidence is too low, the chatbot says it doesn't understand.

---

## 🛠 Technologies Used

* 🐍 Python 3
* 🖥️ Tkinter
* 🤖 Sentence Transformers
* 🔥 PyTorch
* 📚 all-MiniLM-L6-v2 Model

---

## 🌎 Example Topics

The chatbot can answer questions about:

* 🏛️ Capitals
* 🌍 Countries
* 🗺️ Continents
* 🏔️ Mountains
* 🌊 Oceans
* 🏜️ Deserts
* 🏞️ Rivers
* 🌋 Volcanoes
* 🧊 Glaciers
* 📍 Geographic Features

---

## 💬 Example Questions

### User:

What is the capital of France?

### Bot:

🇫🇷 Paris is the capital of France.

---

### User:

What is the largest country in the world?

### Bot:

🇷🇺 Russia is the largest country by land area.

---

### User:

What is the highest mountain on Earth?

### Bot:

🏔️ Mount Everest is the highest mountain above sea level.

---

## 📦 Installation

### 1️⃣ Clone or Download the Project

Download the source code and place it in a folder.

---

### 2️⃣ Install Dependencies

```bash
pip install sentence-transformers torch
```

---

### 3️⃣ Run the Chatbot

```bash
python geography_chatbot.py
```

---

## 📁 Project Structure

```text
GeographyChatbot/
│
├── geography_chatbot.py
├── geography_data.json
├── README.md
└── requirements.txt
```

---

## 📄 Optional JSON Knowledge Base

Instead of storing all data inside Python, you can use a JSON file.

Example:

```json
[
  ["capital of france", "Paris is the capital of France."],
  ["capital of germany", "Berlin is the capital of Germany."],
  ["highest mountain", "Mount Everest is the highest mountain on Earth."]
]
```

Load it with:

```python
import json

with open("geography_data.json", "r", encoding="utf-8") as f:
    qa_pairs = json.load(f)
```

---

## ⚙️ Configuration

### Similarity Threshold

The confidence threshold determines whether an answer is accepted.

```python
THRESHOLD = 0.3
```

### Recommended Values

| Threshold | Result                     |
| --------- | -------------------------- |
| 0.20      | More flexible matching     |
| 0.30      | Balanced                   |
| 0.50      | More accurate but stricter |

---

## 🚀 Future Improvements

* 🌐 Larger geography database
* 🎤 Voice input
* 🔊 Text-to-speech
* 🏳️ Country flags support
* 🧩 Geography quizzes
* 🗺️ Interactive maps
* 🌎 Multilingual support
* 📊 Country statistics
* 🎓 Educational learning mode

---

## 📋 Requirements

```text
sentence-transformers
torch
tkinter
```

---

## 📜 License

🆓 Free to use, modify, and distribute for educational and personal projects.

---

## 👨‍💻 Author

Created with ❤️ using Python, Tkinter, and Sentence Transformers.
# 🌍 Geography Chatbot

An offline AI-powered Geography Chatbot built with **Python**, **Tkinter**, and **Sentence Transformers**.

The chatbot uses semantic search instead of simple keyword matching, allowing it to understand geography-related questions in a more natural way.

---

## ✨ Features

✅ Fully Offline Operation

✅ AI-Powered Semantic Search

✅ Modern Desktop GUI

✅ Natural Language Understanding

✅ Fast Responses

✅ Expandable Knowledge Base

✅ Confidence Score Display

✅ No Internet Required

✅ No API Keys Needed

✅ Cross-Platform Support

---

## 🧠 How It Works

The chatbot uses the **all-MiniLM-L6-v2** Sentence Transformer model to convert questions into numerical embeddings.

When a user asks a question:

1. 📝 The question is converted into an embedding.
2. 🔍 Cosine similarity is calculated against all stored geography questions.
3. 🎯 The most similar question is selected.
4. 💬 The matching answer is displayed.
5. ⚠️ If confidence is too low, the chatbot says it doesn't understand.

---

## 🛠 Technologies Used

* 🐍 Python 3
* 🖥️ Tkinter
* 🤖 Sentence Transformers
* 🔥 PyTorch
* 📚 all-MiniLM-L6-v2 Model

---

## 🌎 Example Topics

The chatbot can answer questions about:

* 🏛️ Capitals
* 🌍 Countries
* 🗺️ Continents
* 🏔️ Mountains
* 🌊 Oceans
* 🏜️ Deserts
* 🏞️ Rivers
* 🌋 Volcanoes
* 🧊 Glaciers
* 📍 Geographic Features

---

## 💬 Example Questions

### User:

What is the capital of France?

### Bot:

🇫🇷 Paris is the capital of France.

---

### User:

What is the largest country in the world?

### Bot:

🇷🇺 Russia is the largest country by land area.

---

### User:

What is the highest mountain on Earth?

### Bot:

🏔️ Mount Everest is the highest mountain above sea level.

---

## 📦 Installation

### 1️⃣ Clone or Download the Project

Download the source code and place it in a folder.

---

### 2️⃣ Install Dependencies

```bash
pip install sentence-transformers torch
```

---

### 3️⃣ Run the Chatbot

```bash
python geography_chatbot.py
```

---

## 📁 Project Structure

```text
GeographyChatbot/
│
├── geography_chatbot.py
├── geography_data.json
├── README.md
└── requirements.txt
```

---

## 📄 Optional JSON Knowledge Base

Instead of storing all data inside Python, you can use a JSON file.

Example:

```json
[
  ["capital of france", "Paris is the capital of France."],
  ["capital of germany", "Berlin is the capital of Germany."],
  ["highest mountain", "Mount Everest is the highest mountain on Earth."]
]
```

Load it with:

```python
import json

with open("geography_data.json", "r", encoding="utf-8") as f:
    qa_pairs = json.load(f)
```

---

## ⚙️ Configuration

### Similarity Threshold

The confidence threshold determines whether an answer is accepted.

```python
THRESHOLD = 0.3
```

### Recommended Values

| Threshold | Result                     |
| --------- | -------------------------- |
| 0.20      | More flexible matching     |
| 0.30      | Balanced                   |
| 0.50      | More accurate but stricter |

---

## 🚀 Future Improvements

* 🌐 Larger geography database
* 🎤 Voice input
* 🔊 Text-to-speech
* 🏳️ Country flags support
* 🧩 Geography quizzes
* 🗺️ Interactive maps
* 🌎 Multilingual support
* 📊 Country statistics
* 🎓 Educational learning mode

---

## 📋 Requirements

```text
sentence-transformers
torch
tkinter
```

---

## 📜 License

🆓 Free to use, modify, and distribute for educational and personal projects.

---

## 👨‍💻 Author

Created with ❤️ using Python, Tkinter, and Sentence Transformers.

<img width="505" height="667" alt="image" src="https://github.com/user-attachments/assets/c8356637-bc0c-4b4b-8f28-3569b48fda1c" />

