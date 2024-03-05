import json
import random

from utils.trie import Trie

class Game:
    def __init__(self) -> None:
        # Loading the words
        self.word_dict = Trie()
        with open('word_list/possible_guesses.json', 'r') as f:
            valid_guesses = json.load(f)
            for word in valid_guesses:
                self.word_dict.add_word(word)

        with open('word_list/possible_answers.json', 'r') as f:
            self.valid_answers = json.load(f)
            
    def play_on_shell(self) -> None:
        true_guess = '✅'
        false_guess = '⬜️'
        false_place_guess = '🟨'
        log = []
        ans = random.choice(self.valid_answers)
        print('Start!')
        for i in range(6):
            # You have six chances
            word = ''
            while not (word.isalpha() and word.islower() and len(word) == 5 and self.word_dict.is_word(word)):
                if len(word) > 0:
                    if not (word.isalpha() and word.islower() and len(word) == 5):
                        print('Invalid input, please try it again!')
                    elif not self.word_dict.is_word(word):
                        print('Not a word!')
                word = input(f'Guess {i + 1}: ').strip()
            rec = []
            for i in range(5):
                if word[i] == ans[i]:
                    rec.append(true_guess)
                elif word[i] in ans:
                    rec.append(false_place_guess)
                else:
                    rec.append(false_guess)
            print(''.join(rec))
            log.append(rec)
            if word == ans: break
        else:
            print(f'The right answer is {ans}')
            return

        print(f'You successfully guessed the right answer within {len(log)} steps!')
        for rec in log:
            print(''.join(rec))

if __name__ == '__main__':
    game = Game()
    game.play_on_shell()