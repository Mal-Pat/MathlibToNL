dir = 'mathlib4/Mathlib'
subj = 'Topology'
file = 'Basic'

f = f'{dir}/{subj}/{file}.lean'

with open(f, 'r') as file2:
    v = 0
    for line in file2:
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