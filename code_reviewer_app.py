import streamlit as st
import openai

# Set up OpenAI API Key
openai.api_key = "AIzaSyAFYzHwjqlSs234x3W5hK8nuOmBNVhBoUE"  # Replace with your API key


# Function to interact with OpenAI API for code review
def review_code(code_input):
    try:
        prompt = (
            f"You are an expert Python code reviewer. Review the following Python code for bugs, issues, "
            f"and improvements, and provide a detailed bug report with fixes. Include the corrected code:\n\n{code_input}"
        )

        # Call OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can change to a relevant model
            prompt=prompt,
            max_tokens=1500,
            temperature=0.7
        )

        # Extract the response
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"


# Function to extract corrected code from the review response
def extract_corrected_code(review_result):
    # Assume the corrected code starts after a specific keyword like "Corrected Code:" in the response
    keyword = "Corrected Code:"
    if keyword in review_result:
        return review_result.split(keyword)[-1].strip()  # Get everything after the keyword
    return "Corrected code could not be extracted."


# Streamlit UI
def main():
    st.title("GenAI App - AI Code Reviewer")
    st.markdown("**Submit your Python code to get an AI-powered review with bug reports and suggested fixes.**")

    # Code input text area
    code_input = st.text_area("Paste your Python code below:", height=300)

    # Submit button
    if st.button("Review Code"):
        if code_input.strip():
            st.info("Analyzing your code. Please wait...")
            review_result = review_code(code_input)

            # Extract corrected code
            corrected_code = extract_corrected_code(review_result)

            st.success("Code Review Completed!")

            # Display the output
            st.subheader("Review Feedback and Fixes")
            st.text_area("Review Results:", value=review_result, height=400)

            # Display corrected code in a separate section
            st.subheader("Corrected Code")
            st.text_area("Corrected Python Code:", value=corrected_code, height=300)
        else:
            st.warning("Please paste your Python code in the text area above.")

    st.markdown("Made with ❤️ using Streamlit and OpenAI.")


if __name__ == "__main__":
    main()
