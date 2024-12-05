from src.turing_machine.tapes.single import Direction, SingleTape

DirectionsTuple = tuple[Direction, ...]
StrTuple = tuple[str, ...]


class MultiTape:
    def __init__(self, tape_count: int) -> None:
        self._tapes = tuple(SingleTape() for _ in range(tape_count))

    @property
    def word(self) -> str:
        return self._tapes[0].word

    @word.setter
    def word(self, word: str) -> None:
        self._tapes[0].word = word
        for tape in self._tapes[1:]:
            tape.word = ""

    @property
    def chars(self) -> StrTuple:
        return tuple(tape.char for tape in self._tapes)

    @chars.setter
    def chars(self, chars: StrTuple) -> None:
        for i, tape in enumerate(self._tapes):
            tape.char = chars[i]

    def move(self, directions: DirectionsTuple) -> None:
        for i, tape in enumerate(self._tapes):
            tape.move(directions[i])

    def protocol_lines(self, state: str) -> StrTuple:
        return tuple(tape.protocol_line(state) for tape in self._tapes)
