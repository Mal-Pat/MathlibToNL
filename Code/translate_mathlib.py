import openai

# Set your OpenAI API key

def translate_lean_code_to_text(lean_code: str):
    try:
        # Make the API call to OpenAI's ChatCompletion endpoint
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or use "gpt-3.5-turbo" if you're using that model
            messages=[
                {"role": "system", "content": "You are a mathematical assistant."},
                {"role": "user", "content": f"Translate the following Lean code: '{lean_code}'"}
            ]
        )
        
        # Extract and print the translated message
        translated_text = response.choices[0].message['content']
        print("Translation Output:", translated_text)
        
        # You can also write this output to a file if needed
        with open("translation_output.txt", "w") as f:
            f.write(translated_text)

    except Exception as e:
        print(f"Error during translation: {e}")

# Example Lean code (you can replace this with any Lean code)
lean_code_example = """
example : 2 + 2 = 4 :=
begin
  exact rfl, -- Proves that 2 + 2 = 4 using reflexivity
end
"""

# Call the function to translate the Lean code
translate_lean_code_to_text(lean_code_example)