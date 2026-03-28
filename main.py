import os, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions

def main():
    # Fetch user prompt command line argument
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt),
    )

    if args.verbose:
        print("User prompt: ", messages)
        print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
        print("Response tokens: ",response.usage_metadata.candidates_token_count)
    print("Response: ", response.text)
    for fc in response.function_calls:
        print(f"Calling function: {fc.name}({fc.args})")



if __name__ == "__main__":
    main()
