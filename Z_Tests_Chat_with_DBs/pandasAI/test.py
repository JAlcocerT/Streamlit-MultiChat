import openai
import pandas as pd

# Set up OpenAI API credentials
openai.api_key = "sk-proj-"

# Create a sample housing dataset using a Pandas DataFrame
data = {
    "Address": ["123 Main St", "456 Elm St", "789 Oak St"],
    "City": ["New York", "Los Angeles", "Chicago"],
    "Price": [500000, 750000, 600000],
    "Bedrooms": [2, 3, 4],
    "Bathrooms": [1, 2, 3]
}
df = pd.DataFrame(data)

# Function to query the OpenAI API for information about the housing data
def ask_openai(question, context):
    prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = response.choices[0].text.strip()
    return answer

# Example usage
question1 = "What is the average price of the houses?"
context1 = df.to_string(index=False)
answer1 = ask_openai(question1, context1)
print("Question 1:", question1)
print("Answer 1:", answer1)

question2 = "Which city has the house with the most bedrooms?"
context2 = df.to_string(index=False)
answer2 = ask_openai(question2, context2)
print("\nQuestion 2:", question2)
print("Answer 2:", answer2)