class LetterModel:
    def __init__(self, character: str):
        self.character: str = character
        self.validCharacter: bool = False
        self.validPosition: bool = False

    def __repr__(self):
        return f"[{self.character} is_in_word: {self.validCharacter} is_in_position: {self.validPosition}]"
