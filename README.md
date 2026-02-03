# AI-Chatbot-with-NLP

*Company*: Codtech IT Solutions

*Name*: Tottaramudi Jhansi Victoriya

*Intern ID*: CTIS1491

*Domain*: Python Programming

*Duration*: 4Weeks

*Mentor*: Neela Santhosh Kumar

description:

In this project, I developed a basic AI chatbot using Python and Natural Language Processing (NLP) techniques. The main aim of this project was to understand how machines can process human language and respond to user queries in a meaningful way. Instead of creating a complex AI system, I focused on building a beginner-friendly chatbot that uses NLP concepts like text preprocessing, TF-IDF vectorization, and cosine similarity to generate responses.

The chatbot works using a predefined knowledge base that contains a set of questions and answers. These questions represent the types of queries the user might ask, and the corresponding answers are the chatbot’s responses. Since this is a retrieval-based chatbot, it does not generate new answers on its own. Instead, it finds the most relevant answer from its database based on the similarity between the user’s input and stored questions.

To make the chatbot understand text better, I used the NLTK (Natural Language Toolkit) library. NLTK helps in processing and cleaning human language before it is analyzed. One of the important steps in this project is text preprocessing. Whenever the user types a message, the text is first converted to lowercase so that the system treats “Hello” and “hello” as the same word. Then, tokenization is done using NLTK, which means the sentence is broken into individual words. After that, punctuation marks are removed because they do not contribute much to understanding the meaning of a sentence.

Another important step is lemmatization, which is done using WordNetLemmatizer from NLTK. Lemmatization converts words into their base or root form. For example, “running” becomes “run” and “better” becomes “good.” This helps the chatbot understand that different forms of a word can have the same meaning. The same preprocessing steps are also applied to all the questions stored in the chatbot’s knowledge base so that the comparison between user input and stored questions is fair and accurate.

After preprocessing, the chatbot uses TF-IDF (Term Frequency–Inverse Document Frequency) vectorization. This technique converts text into numerical form because computers understand numbers, not words. TF-IDF gives more importance to meaningful words and less importance to common words like “is,” “the,” or “a.” All stored questions are converted into TF-IDF vectors, and the user’s input is also transformed in the same way.

Next, cosine similarity is used to compare the user’s input vector with all the stored question vectors. Cosine similarity measures how similar two sentences are based on the angle between their vector representations. The chatbot selects the question with the highest similarity score. If the similarity score is above a certain threshold, the chatbot returns the corresponding answer. If the score is too low, it means the chatbot does not understand the question, and it replies with a default message asking the user to rephrase.

The chatbot runs in a loop, continuously taking user input and providing responses until the user types “bye,” “exit,” or “quit,” which stops the program. This makes the chatbot interactive and capable of having a simple conversation with the user.

Through this project, I learned how NLP techniques are applied in real-world applications like chatbots. I understood the importance of text preprocessing, vectorization, and similarity measurement. I also improved my Python programming skills and gained practical experience in building an AI-based system from scratch. This project helped me understand the basic working of intelligent systems and how human language can be processed by machines in a structured way.
