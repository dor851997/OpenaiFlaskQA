import openai
import os

openai.api_key=os.environ.get('OPENAI_API_KEY')

def gpt_reply(input_text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",  # Use the appropriate model name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": input_text}
            ],
            max_tokens=150  # Adjust the max_tokens value based on your requirement
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"


# if __name__ == "__main__":
#     # Example usage
#     user_input = "What is the capital of France?"
#     print(gpt_reply(user_input))