import copy
import time
from itertools import product as combine

from PyQt6.QtCore import QThread, pyqtSignal

from src.turing_machine.machine import TuringMachine


class CheckWordThread(QThread):
    step_passed = pyqtSignal(str)
    result_got = pyqtSignal(str)

    def __init__(self, mt: TuringMachine, word: str) -> None:
        super().__init__()
        self.continue_flag = True
        self.word = word
        self.generator = mt.process_word_verbose(word)

    def run(self) -> None:
        common_protocol_line = iter_num = None
        for protocol_lines, iter_num in self.generator:
            if not self.continue_flag:
                self.result_got.emit(f"Операция прервана на {iter_num} такте.")
                return
            common_protocol_line = "\t".join(protocol_lines)
            self.step_passed.emit(common_protocol_line + "\n")
            time.sleep(0.001)
        self.result_got.emit(
            f"Слово «{self.word}» {'' if '1' in common_protocol_line else 'НЕ '}"
            f"принадлежит языку ({iter_num} тактов)",
        )


class PlottingThread(QThread):
    iteration_passed = pyqtSignal(int)

    def __init__(self, active_mt: TuringMachine) -> None:
        super().__init__()
        self.continue_flag = True
        self.mt = copy.deepcopy(active_mt)

    def run(self) -> None:
        letter_count = 0
        while self.continue_flag:
            max_iter_counter = 0
            for word_letters in combine(self.mt.alphabet, repeat=letter_count):
                word = "".join(word_letters)
                _, iter_counter = self.mt.process_word(word)
                max_iter_counter = max(max_iter_counter, iter_counter)
            letter_count += 1
            self.iteration_passed.emit(max_iter_counter)
            time.sleep(0.25)
