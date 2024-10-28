# from embedchain import App
# app = App()
# app.add('/path/to/file.csv', data_type='csv')


#pip install openai mem0ai

###https://docs.mem0.ai/examples/personal-travel-assistant

import os
from openai import OpenAI
from mem0 import Memory
import csv


# Set the OpenAI API key
os.environ['OPENAI_API_KEY'] = 'sk-proj-'

# class PersonalTravelAssistant:
#     def __init__(self):
#         self.client = OpenAI()
#         self.memory = Memory()
#         self.messages = [{"role": "system", "content": "You are a Real Estate Agent that will make relevant follow up questions to the user to provide the best housing option."}]

class PersonalTravelAssistant:
    def __init__(self):
        self.client = OpenAI()
        self.memory = Memory()
        self.messages = [{"role": "system", "content": "You are a Real Estate Agent that will make relevant follow up questions to the user to provide the best housing option."}]
        
        # Load flat examples from CSV and add to memory
        with open('flat_examples.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                flat_example = f"Location: {row['location']}, Price: {row['price']}, Rooms: {row['rooms']}, Amenities: {row['amenities']}"
                self.memory.add(flat_example, user_id='flat_examples')

    def ask_question(self, question, user_id):
        # Fetch previous related memories
        previous_memories = self.search_memories(question, user_id=user_id)
        prompt = question
        if previous_memories:
            prompt = f"User input: {question}\n Previous memories: {previous_memories}"
        self.messages.append({"role": "user", "content": prompt})

        # Generate response using GPT-4o
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=self.messages
        )
        answer = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": answer})

        # Store the question in memory
        self.memory.add(question, user_id=user_id)
        return answer

    def get_memories(self, user_id):
        memories = self.memory.get_all(user_id=user_id)
        return [m['text'] for m in memories]

    def search_memories(self, query, user_id):
        memories = self.memory.search(query, user_id=user_id)
        return [m['text'] for m in memories]

# Usage example
user_id = "traveler_123"
ai_assistant = PersonalTravelAssistant()

def main():
    while True:
        question = input("Question: ")
        if question.lower() in ['q', 'exit']:
            print("Exiting...")
            break

        answer = ai_assistant.ask_question(question, user_id=user_id)
        print(f"Answer: {answer}")
        memories = ai_assistant.get_memories(user_id=user_id)
        print("Memories:")
        for memory in memories:
            print(f"- {memory}")
        print("-----")

if __name__ == "__main__":
    main()
