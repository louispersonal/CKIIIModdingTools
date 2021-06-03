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


def print_words(number_of_words):
    alphabet_one = Alphabet()
    with open('syllables.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line = 0
        for row in csv_reader:
            if line > 0:
                alphabet_one.add_syllable(row[0])
            line = line + 1
    csv_file.close()
    for u in range(number_of_words):
        word_one = Word()
        length = random.randint(2, 4)
        word_one.make_word(alphabet_one, length)
        word_one.print_word()


def localize_aboriginal():
    f = open("language/words_not_localized.txt", "r")
    f2 = open("language/words_localized.txt", "w", encoding="utf8")
    for line in f:
        word = line.strip()
        word = word.lower()
        new_word = [""]
        for letter in word:
            if letter == "d" or letter == "t":
                new_word.append("đ")
            elif letter == "j":
                new_word[-1] = "ɉ"
            elif letter == "y":
                if new_word[-1] == "n":
                    new_word[-1] = "n̪"
                elif new_word[-1] == "l":
                    new_word[-1] = "ɹ"
                else:
                    new_word.append(letter)
            elif letter == "g":
                if new_word[-1] == "n":
                    new_word[-1] = "ɳ"
                else:
                    new_word.append(letter)
            elif letter == "l":
                if new_word[-1] == "r":
                    new_word[-1] = "ɭ"
                else:
                    new_word.append(letter)
            elif letter == "r":
                if new_word[-1] == "r":
                    new_word[-1] = "Ʀ"
                else:
                    new_word.append(letter)
            elif letter == "o":
                if new_word[-1] == "o":
                    new_word[-1] = "u"
                else:
                    new_word.append(letter)
            elif letter == "a":
                if new_word[-1] == "a":
                    new_word[-1] = "ā"
                else:
                    new_word.append(letter)
            else:
                new_word.append(letter)

        new_word_string = ""
        for item in new_word:
            new_word_string = new_word_string + item

        f2.write(new_word_string.capitalize() + "\n")


if __name__ == '__main__':
    localize_aboriginal()
