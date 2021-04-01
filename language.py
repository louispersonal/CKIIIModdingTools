import random
import csv


class Syllable:
    def __init__(self, letters):
        self.letters = letters


class Alphabet:
    def __init__(self):
        self.syllables = []

    def add_syllable(self, syllable):
        self.syllables.append(syllable)


class Word:
    def __init__(self):
        self.word = []

    def make_word(self, alphabet, number_syllables):
        for i in range(number_syllables):
            self.word.append(random.choice(alphabet.syllables))

    def print_word(self):
        word_string = ""
        line_count = 0
        for x in self.word:
            word_string = word_string + self.word[line_count]
            line_count = line_count + 1
        print(word_string)


if __name__ == '__main__':
    alphabet_one = Alphabet()
    with open('syllables.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line = 0
        for row in csv_reader:
            if line > 0:
                alphabet_one.add_syllable(row[0])
            line = line + 1
    csv_file.close()
    for u in range(100):
        word_one = Word()
        length = random.randint(2, 4)
        word_one.make_word(alphabet_one, length)
        word_one.print_word()
