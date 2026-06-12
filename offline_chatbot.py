from sentence_transformers import SentenceTransformer, util
import tkinter as tk
from tkinter import scrolledtext

model = SentenceTransformer('all-MiniLM-L6-v2')

qa_pairs = [
    ("hello hi hey greetings γεια καλησπέρα",
     "Hello! Ask me anything about geography."),
    ("capital of greece",
     "The capital of Greece is Athens."),
    ("capital of france",
     "The capital of France is Paris."),
    ("capital of germany",
     "The capital of Germany is Berlin."),
    ("capital of italy",
     "The capital of Italy is Rome."),
    ("largest country",
     "Russia is the largest country in the world by land area."),
    ("smallest country",
     "Vatican City is the smallest country in the world."),
    ("longest river",
     "The Nile is often considered the world's longest river."),
    ("amazon river",
     "The Amazon River carries the largest volume of water in the world."),
    ("highest mountain",
     "Mount Everest is the highest mountain above sea level."),
    ("sahara desert",
     "The Sahara is the largest hot desert in the world."),
    ("continent africa",
     "Africa is the second-largest continent by area and population."),
    ("continent asia",
     "Asia is the largest continent on Earth."),
    ("continent europe",
     "Europe contains about 44 countries depending on definitions used."),
    ("pacific ocean",
     "The Pacific Ocean is the largest ocean on Earth."),
    ("atlantic ocean",
     "The Atlantic Ocean separates the Americas from Europe and Africa."),
    ("indian ocean",
     "The Indian Ocean is the third-largest ocean."),
    ("north america",
     "North America includes Canada, the United States, Mexico, and others."),
    ("south america",
     "South America is home to the Amazon Rainforest."),
    ("australia",
     "Australia is both a country and a continent."),
    ("antarctica",
     "Antarctica is the coldest continent on Earth."),
    ("equator",
     "The Equator divides Earth into the Northern and Southern Hemispheres."),
    ("prime meridian",
     "The Prime Meridian passes through Greenwich, England."),
    ("what is a continent",
     "A continent is one of Earth's large landmasses."),
    ("what is a country",
     "A country is a political territory with its own government."),
    ("what is a peninsula",
     "A peninsula is land surrounded by water on three sides."),
    ("what is an island",
     "An island is land completely surrounded by water."),
    ("what is a volcano",
     "A volcano is an opening in Earth's crust where magma can escape."),
    ("what is a glacier",
     "A glacier is a large mass of slowly moving ice."),
    ("what is a delta",
     "A river delta forms where a river deposits sediment near its mouth."),
    ("thanks thank you",
     "You're welcome! Ask me another geography question.")
]

question_texts = [q for q, a in qa_pairs]
question_embeddings = model.encode(question_texts, convert_to_tensor=True)

# Similarity threshold — below this, the bot says it doesn't understand
THRESHOLD = 0.3


# Semantic matching replaces keyword matching
def get_response(user_input):
    input_embedding = model.encode(user_input, convert_to_tensor=True)
    similarities = util.cos_sim(input_embedding, question_embeddings)[0]
    best_idx = similarities.argmax().item()
    best_score = similarities[best_idx].item()

    if best_score < THRESHOLD:
        return best_score, "Sorry, I don't understand. Try asking about australia, europe."

    return best_score, qa_pairs[best_idx][1]

class ChatbotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Geography Chatbot")
        self.root.geometry("400x500")
        self.root.configure(bg="#2E2E2E")

        tk.Label(
           root, text = "Geography Chatbot", font = ("Helvetica", 16, "bold"),
            fg = "#FFFFFF", bg="#2E2E2E"
        ).pack(pady=10)

        self.chat_area = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, height=20, width= 50, font=("Arial", 11),
            bg="#3C3C3C", fg = "#E0E0E0", insertbackground="white"
        )
        self.chat_area.pack(pady=10, padx=10)
        self.chat_area.insert(tk.END,
                              "Welcome to GeographyChat\n"
                              "Ask about geography!\n")
        self.chat_area.config(state="disabled")

        input_frame = tk.Frame(root, bg="#2E2E2E")
        input_frame.pack(pady=5)

        self.input_field =tk.Entry(
            input_frame, width=40, font=('Arial', 11), bg="#4A4A4A", fg="#FFFFFF",
            insertbackground="white"
        )
        self.input_field.pack(side=tk.LEFT,padx=5)
        self.input_field.bind("<Return>", self.send_message)

        # Send button
        tk.Button(
            input_frame, text="Send", command=self.send_message, font=("Arial", 11),
            bg="#4CAF50", fg="#FFFFFF", activebackground="#45A049"
        ).pack(side=tk.LEFT, padx=5)

        # Clear button
        tk.Button(
            root, text="Clear Chat", command=self.clear_chat, font=("Arial", 11),
            bg="#F44336", fg="#FFFFFF", activebackground="#D32F2F"
        ).pack(pady=5)

    def send_message(self, event=None):
        user_input = self.input_field.get().strip()
        if not user_input:
            return

        score, response = get_response(user_input)
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"\nYou: {user_input}\n")
        self.chat_area.insert(tk.END, f"Match confidence: {score:.2f}\n")
        self.chat_area.insert(tk.END, f"Bot: {response}\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)
        self.input_field.delete(0, tk.END)

    def clear_chat(self):
        self.chat_area.config(state='normal')
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.insert(tk.END,
                              "Welcome to GeographyChat!\n"
                              "Ask about geography!\n")
        self.chat_area.config(state='disabled')

def main():
    root = tk.Tk()
    app = ChatbotUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
