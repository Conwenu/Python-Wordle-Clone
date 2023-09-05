from letter import LetterModel

class Wordle:
    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5
    LETTER_CHECK = "*"

    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []
        pass

    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @property
    def attempts_left(self):
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_try_again(self):
        return self.attempts_left > 0 and not self.is_solved

    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)

    def guess(self, word: str):
        word = word.upper()
        result = [LetterModel(x) for x in word]
        remaining_secret = list(self.secret)
        for i in range(self.WORD_LENGTH):
            letter = result[i]
            if letter.character == remaining_secret[i]:
                letter.validPosition = True
                remaining_secret[i] = self.LETTER_CHECK

        for i in range(self.WORD_LENGTH):
            letter = result[i]
            if letter.validPosition:
                continue
            for j in range(self.WORD_LENGTH):
                if letter.character == remaining_secret[j]:
                    remaining_secret[j] = self.LETTER_CHECK
                    letter.validCharacter = True
                    break
        return result
