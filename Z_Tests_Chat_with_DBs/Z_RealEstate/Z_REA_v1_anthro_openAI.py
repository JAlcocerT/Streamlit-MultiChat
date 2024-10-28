import streamlit as st #streamlit run Z_REA_v1_an
from Z_REA_v1simple import RealEstateAssistant

# Create the assistant
ai_assistant = RealEstateAssistant()

# Set up the Streamlit interface
st.title("Real Estate Assistant")

# Get the user ID
user_id = st.text_input("Enter your User ID", "user_123")

# Get the number of back and forth
follow_up_limit = st.slider("Select the number of back and forth", 1, 10, 3)
ai_assistant.set_follow_up_limit(follow_up_limit)

# Get the user's question
question = st.text_input("Enter your question")

# When the user presses the 'Ask' button, get the response from the assistant
if st.button("Ask"):
    answer = ai_assistant.ask_question(question, user_id=user_id)
    st.write(f"Answer: {answer}")

    # Display the memories
    memories = ai_assistant.get_memories(user_id=user_id)
    st.write("Memories:")
    for memory in memories:
        st.write(f"- {memory}")