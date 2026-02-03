import nltk
import string
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize Lemmatizer
lemmer = WordNetLemmatizer()

# Knowledge Base
knowledge_base = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "what is your name": "I am an NLP-based chatbot built using Python.",
    "what can you do": "I can answer questions using Natural Language Processing.",
    "what is python": "Python is a programming language widely used in AI and software development.",
    "what python works": "python works by interpreting code line by line and has extensive libraries for various applications.",
    "where the python used": "python is used in web development, data science, artificial intlligence(ai), and more.",
    "what is ai": "AI stands for Artificial Intelligence, which enables machines to learn and think.",
    "bye": "Goodbye! Have a great day!"
}

questions = list(knowledge_base.keys())
answers = list(knowledge_base.values())

# Text Preprocessing Function using NLTK
def preprocess(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tokens = [lemmer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return " ".join(tokens)

# Preprocess all questions
processed_questions = [preprocess(q) for q in questions]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(processed_questions)

# Function to generate response
def get_response(user_input):
    user_input_processed = preprocess(user_input)
    user_tfidf = vectorizer.transform([user_input_processed])

    similarity = cosine_similarity(user_tfidf, tfidf_matrix)
    best_match_index = similarity.argmax()
    best_score = similarity[0][best_match_index]

    if best_score < 0.3:
        return "Sorry, I didn't understand that. Can you rephrase?"
    else:
        return answers[best_match_index]

# Chat Loop
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Chatbot:", knowledge_base["bye"])
        break

    response = get_response(user_input)
    print("Chatbot:", response)
