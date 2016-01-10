import sys

def get_input(filename):
  with open(filename) as f:
    # number of problems - we don't need this
    f.readline()

    data = []
    while True:
        info_line = f.readline()
        data_line = f.readline()
        if not data_line:
            break;
        max_price = int(info_line.split(' ')[1].strip())
        d = [int(x) for x in data_line.split(' ')]
        data = data + [(max_price, d)]
  return data

def sequence_from_start(max_price, xs):
    sequences = []
    current_sequence = []
    for x in xs:
        current_sequence.append(x)
        if sum(current_sequence) <= max_price:
            sequences.append(current_sequence[:])
        else:
            break;

    return sequences

problems = get_input(sys.argv[1])

for nr, (max_price, data) in enumerate(problems):
    sequences = []
    for i in range(len(data)):
        sequences = sequences + sequence_from_start(max_price, data[i:])

    print('Case #' + str(nr + 1) + ': ' + str(len(sequences)))
