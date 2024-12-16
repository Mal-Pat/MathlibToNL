dir = 'mathlib4/Mathlib'
subj = 'Topology'
file = 'Basic'

f = f'{dir}/{subj}/{file}.lean'

section_keywords = ['variable']
keywords = ['theorem', 'lemma']

with open(f, 'r') as infile:
    v = 0
    for line in infile:
        if 'theorem' in line:
            if ':=' in line:
                print(line)
            else:
                v += 1
        if v != 0:
            if ':=' in line:
                print(line)
                v = 0
            else:
                print(line)
                continue

dump = f'{subj}/{file}.jsonl'

with open(dump, 'w') as outfile:
    pass