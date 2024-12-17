import json
import openai  

input_file = "Topology/Basic.jsonl"
output_file = "Topology/Basic_translations.jsonl"

def translate_to_natural_language(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  
            messages=[
                {"role": "system", "content": "You are a helpful assistant that translates formal mathematical theorems into natural language explanations."},
                {"role": "user", "content": f"Translate the following theorem or lemma into natural language: {text}"}
            ]
        )

    # Translate the following theorems or lemms from lean4 to natural language. Output only the translation and do NOT use any unnecessary english words. 
        
        translation = response['choices'][0]['message']['content']
        return translation
    except Exception as e:
        print(f"Error translating text: {e}")
        return None


translated_data = []
with open(input_file, 'r') as infile:
    for line in infile:
        entry = json.loads(line)
        theorem_or_lemma = entry.get("theorem_or_lemma")

        if theorem_or_lemma:
            print(f"Translating: {theorem_or_lemma}")
            translation = translate_to_natural_language(theorem_or_lemma)

            if translation:
                translated_data.append({
                    "original": theorem_or_lemma,
                    "translation": translation
                })



with open(output_file, 'w') as outfile:
    for entry in translated_data:
        json.dump(entry, outfile)
        outfile.write("\n")

print(f"Translations written to {output_file}")