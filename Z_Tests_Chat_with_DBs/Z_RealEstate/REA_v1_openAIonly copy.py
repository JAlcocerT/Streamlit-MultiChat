import os
import csv
from openai import OpenAI
from mem0 import Memory

# Set the API key
os.environ['OPENAI_API_KEY'] = 'sk-proj-'

class RealEstateAssistant:
    def __init__(self):
        self.client = OpenAI()
        self.memory = Memory()
        self.messages = [{"role": "system", "content": "You are a Real Estate Agent that will make relevant follow-up questions to the user to provide the best housing option. When you see a match in the given amenities, you can comment on them."}]
        self.follow_up_count = 0

    def ask_question(self, question, user_id):
        # Fetch previous related memories
        previous_memories = self.search_memories(question, user_id=user_id)
        prompt = question
        if previous_memories:
            prompt = f"User input: {question}\nPrevious memories: {previous_memories}"
        self.messages.append({"role": "user", "content": prompt})

        # Generate response using GPT-4
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=self.messages
        )
        answer = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": answer})

        # Store the question in memory
        self.memory.add(question, user_id=user_id)
        self.follow_up_count += 1

        # After 3 follow-up questions, query properties
        if self.follow_up_count >= 3:
            return self.query_properties(user_id)

        return answer

    def get_memories(self, user_id):
        memories = self.memory.get_all(user_id=user_id)
        return [m['text'] for m in memories]

    def search_memories(self, query, user_id):
        memories = self.memory.search(query, user_id=user_id)
        return [m['text'] for m in memories]

    def query_properties(self, user_id):
        memories = self.get_memories(user_id=user_id)
        query = " ".join(memories)
        
        # Use OpenAI to generate a response based on user memories
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a Real Estate Agent. Based on the user's memories, suggest suitable properties or provide relevant information about housing options."},
                {"role": "user", "content": f"User's memories: {query}"}
            ]
        )
        
        self.follow_up_count = 0  # Reset follow-up count after query
        return response.choices[0].message.content

# Usage example
user_id = "user_123"
ai_assistant = RealEstateAssistant()

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