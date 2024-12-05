import re
from collections.abc import Generator
from pathlib import Path

from src.turing_machine.tapes.multiple import DirectionsTuple, MultiTape, StrTuple

CommandKey = tuple[str, StrTuple]
CommandValue = tuple[str, StrTuple, DirectionsTuple]
Command = dict[CommandKey, CommandValue]


class TuringMachine:
    UNNECESSARY_TEXT_REGEXP = re.compile(r" *(?:#.*)?(?:\n|$)")
    COMMAND_FILE_HEADER_REGEXP = re.compile(r"^(.+)\n([^ ]+)\n(\d+)\n")

    @staticmethod
    def get_multitape_command_regexp(count: int) -> re.Pattern:
        return re.compile((
            r"^q(\d+) (.(?:,(?:.)){0}) ->"
            r" q(\d+|z) (.(?:,(?:.)){0}) ([LER](?:,[LER]){0})$"
        ).format("{%s}" % (count - 1)))

    def __init__(self, filename: str | Path) -> None:
        self._filename = filename
        self._alphabet: frozenset[str, ...]
        self._lang: str
        self._tape_obj: MultiTape
        self._command_regexp: re.Pattern
        self._commands: Command
        self._load_from_file(filename)

    @property
    def filename(self) -> str:
        return self._filename

    @property
    def alphabet(self) -> frozenset[str, ...]:
        return self._alphabet

    @property
    def lang(self) -> str:
        return self._lang

    def _set_tape_count(self, value: int) -> None:
        if value < 1:
            msg = "Количество лент должно быть больше 0"
            raise ValueError(msg)
        self._command_regexp = self.get_multitape_command_regexp(value)
        self._tape_obj = MultiTape(value)

    def _load_from_file(self, filename: str | Path) -> None:
        with Path(filename).open(encoding="utf8") as file:
            algorithm = file.read()

        algorithm = self.UNNECESSARY_TEXT_REGEXP.sub("\n", algorithm)
        while "\n\n" in algorithm:
            algorithm = algorithm.replace("\n\n", "\n")

        if not algorithm:
            msg = "Файл алгоритма для машины Тьюринга пуст"
            raise ValueError(msg)

        header = self.COMMAND_FILE_HEADER_REGEXP.match(algorithm)
        if header:
            self._set_tape_count(int(header.group(3)))
            self._alphabet = frozenset(header.group(2))
            self._lang = header.group(1)
            algorithm = self.COMMAND_FILE_HEADER_REGEXP.sub("", algorithm, 1)
        else:
            msg = "Файл алгоритма для машины Тьюринга не соответствует формату"
            raise ValueError(msg)

        self._parse_commands(algorithm.splitlines())

    def _parse_commands(self, str_commands: list[str]) -> None:
        old_state: str
        old_chars_str: str
        old_chars: StrTuple
        state: str
        chars_str: str
        chars: StrTuple
        directions_str: str
        directions: DirectionsTuple

        self._commands = {}
        for command in str_commands:
            match_obj = self._command_regexp.match(command)
            if not match_obj:
                msg = f"Не удалось распарсить строку алгоритма:\n{command}"
                raise ValueError(msg)

            old_state, old_chars_str, state, chars_str, directions_str = \
                match_obj.groups()
            old_chars, chars, directions = (
                tuple(string.split(","))
                for string in (old_chars_str, chars_str, directions_str)
            )  # type: ignore[blanket-type-ignore]
            self._commands[(old_state, old_chars)] = (state, chars, directions)

    def reload(self) -> None:
        self._load_from_file(self._filename)

    def process_word(self, word: str) -> tuple[str, int]:
        state = "0"
        self._tape_obj.word = word
        iter_counter = 0
        while state != "z":
            command_key = (state, self._tape_obj.chars)
            command_value = self._commands.get(command_key)
            if not command_value:
                break
            iter_counter += 1
            state, self._tape_obj.chars, directions = command_value
            self._tape_obj.move(directions)
        return self._tape_obj.word, iter_counter

    def process_word_verbose(self, word: str) -> Generator[tuple[StrTuple, int]]:
        state = "0"
        self._tape_obj.word = word
        iter_counter = 0
        while state != "z":
            command = self._commands.get((state, self._tape_obj.chars))
            if not command:
                break
            iter_counter += 1
            protocol_lines = self._tape_obj.protocol_lines(state)
            yield protocol_lines, iter_counter
            state, self._tape_obj.chars, directions = command
            self._tape_obj.move(directions)
        protocol_lines = self._tape_obj.protocol_lines(state)
        yield protocol_lines, iter_counter
