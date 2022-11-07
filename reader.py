import re


def single_tread_count_unique_word(input_filename, output_filename):
    with open(output_filename, 'a+') as output_file, open(input_filename, 'r') as input_file:
        counts = {}
        for line in input_file:
            line = re.sub('[""(),.!:?123456789-]', ' ', line)
            words = line.lower().split()

            for word in words:
                counts[word] = counts.get(word, 0) + 1

        pairs = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
        for word, count in pairs:
            output_file.write(f'{word} - {count}\n')

        input_file.close()
        output_file.close()