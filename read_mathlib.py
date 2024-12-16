import os
import json

# Define file paths
dir = 'mathlib4/Mathlib'
subj = 'Topology'
file = 'Basic'

f = f'{dir}/{subj}/{file}.lean'
dump = f'{subj}/{file}.jsonl'

# Keywords for extraction
keywords = ['theorem', 'lemma']

# Storage for extracted theorems/lemmas
extracted_data = []

# Read and group multi-line theorems/lemmas
with open(f, 'r') as infile:
    capturing = False
    current_entry = []

    for line in infile:
        stripped_line = line.strip()

        if any(keyword in stripped_line for keyword in keywords):  # Start capturing
            capturing = True

        if capturing:
            current_entry.append(stripped_line)

            if stripped_line.endswith(":="):  # End of the current theorem/lemma
                extracted_data.append(" ".join(current_entry))  # Combine lines
                current_entry = []  # Reset for the next entry
                capturing = False

# Ensure the output directory exists
os.makedirs(os.path.dirname(dump), exist_ok=True)

# Write grouped theorems/lemmas to JSONL
with open(dump, 'w') as outfile:
    for entry in extracted_data:
        json.dump({"theorem_or_lemma": entry}, outfile)  # Save as JSON object
        outfile.write("\n")  # Add newline for JSONL format

print(f"Extracted theorems and lemmas written to {dump}")
