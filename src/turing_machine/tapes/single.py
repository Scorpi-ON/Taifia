from typing import Literal

LAMBDA = "λ"
RADIX = 10
UNDERLINE_DIGIT_CHAR_OFFSET = 8320

Direction = Literal["R", "L", "E"]


class SingleTape:
    @staticmethod
    def num_to_underline_register_str(num: int | str) -> str:
        if isinstance(num, str):
            num = int(num)
        result = ""
        while num >= RADIX:
            result = chr(UNDERLINE_DIGIT_CHAR_OFFSET + num % RADIX) + result
            num //= RADIX
        result = chr(UNDERLINE_DIGIT_CHAR_OFFSET + num) + result
        return result

    def __init__(self) -> None:
        self._word = LAMBDA
        self._index = 0

    @property
    def word(self) -> str:
        return self._word

    @word.setter
    def word(self, word: str) -> None:
        self._index = 0
        if not word:
            word = LAMBDA
        self._word = word

    @property
    def char(self) -> str:
        return self._word[self._index]

    @char.setter
    def char(self, char: str) -> None:
        self._word = self._word[:self._index] + char + self._word[self._index + 1:]

    def move(self, direction: Direction) -> None:
        match direction:
            case "R":
                if self._word.startswith(LAMBDA):
                    self._word = self._word[1:]
                else:
                    self._index += 1
                if self._index == len(self._word):
                    self._word += LAMBDA
            case "L":
                if self._index > 0:
                    self._index -= 1
                    if self._word.endswith(LAMBDA):
                        self._word = self._word[:-1]
                elif self._word != LAMBDA:
                    self._word = LAMBDA + self._word
            case "E":
                pass
            case _:
                error_msg = f"Направление должно быть либо L, либо R. Получено {direction}"
                raise ValueError(error_msg)

    def protocol_line(self, state: str) -> str:
        if state != "z":
            state = SingleTape.num_to_underline_register_str(state)
        state = f"q{state}"
        return self._word[:self._index] + state + self._word[self._index:]
