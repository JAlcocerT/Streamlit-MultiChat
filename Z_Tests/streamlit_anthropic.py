### https://www.youtube.com/watch?v=ximj9QWle-g
#https://www.linkedin.com/pulse/build-generative-ai-app-claude-3-powerful-llm-sri-laxmi-zpofc/?trackingId=7m%2FnAkWGQOaNlbsYnLm3xg%3D%3D

import streamlit as st
import anthropic

def main():
    st.title("Your Emotional Assistant")

    # Get the API key from the user
    api_key = st.text_input("Enter your Anthropic API Key:", type="password")

    if api_key:
        # Create the Anthropi client
        client = anthropic.Anthropic(api_key=api_key)

        # Get user input
        user_input = st.text_area("Enter your thoughts or feelings for the day:")

        if st.button("Analyze Mood"):
            message = client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=689,
                temperature=0,
                messages=[
                    {"role": "user", "content": f"Based on the following text, can you analyze the overall mood or sentiment expressed by the person?\n\n{user_input}"}
                ]
            )

           
            mood_analysis = ''.join(block.text for block in message.content)  # Adjusted line

            # Display the mood analysis using Markdown for formatting
            st.markdown("**Mood Analysis:**")
            st.write(mood_analysis)

            # Define mood categories
            mood_categories = ["Happy", "Sad", "Angry", "Anxious", "Neutral"]

            # Categorize the mood based on keywords or patterns
            mood_category = "Neutral"
            for category in mood_categories:
                if category.lower() in mood_analysis.lower():
                    mood_category = category
                    break

            # Display the mood category with emphasis
            mood_display = f"**Mood Category:** {mood_category}"
            if mood_category == "Happy":
                st.success(mood_display)
            elif mood_category == "Sad" or mood_category == "Angry":
                st.error(mood_display)
            elif mood_category == "Anxious":
                st.warning(mood_display)
            else:  # Neutral or any other category
                st.info(mood_display)

            # Provide recommendations
            if mood_category != "Neutral":
                message = client.messages.create(
                    model="claude-3-sonnet-20240229",
                    max_tokens=689,
                    temperature=0,
                    messages=[
                        {"role": "user", "content": f"Based on the mood analysis '{mood_analysis}' and the mood category '{mood_category}', can you provide some recommendations or suggestions to help the person feel better?"}
                    ]
                )
                recommendations = ''.join(block.text for block in message.content)  # Adjusted line to concatenate the text

                st.write("**Recommendations:**")
                st.write(recommendations)
    else:
        st.warning("Please enter your Anthropic API Key to use the app.")

if __name__ == "__main__":
    main()        