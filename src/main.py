import os
import sys
from pathlib import Path

import pyqtgraph as pg
from PyQt6 import QtWidgets
from PyQt6.QtCore import QRegularExpression as QRegExp
from PyQt6.QtGui import QPalette
from PyQt6.QtGui import QRegularExpressionValidator as QRegExpValidator
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from pyqtgraph import exporters

from src.turing_machine.machine import TuringMachine
from src.ui.form import Ui_mainWindow
from src.working_threads import CheckWordThread, PlottingThread

ALGORITHM_PATH = Path("src/algorithm")


class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.active_MT: TuringMachine | None = None
        self.loaded_MTs: list[TuringMachine] = []
        self.load_mt()
        self.check_word_thread: CheckWordThread | None = None

        self.plotWidg.setLabel("left", "Макс. число итераций")
        self.plotWidg.setLabel("bottom", "Длина слова")
        self.iterations_data = []
        self.plotting_thread: PlottingThread | None = None

        self.tabWidg.currentChanged.connect(self.save_act_update_state)
        self.wordTextInp.returnPressed.connect(self.check_word_or_stop_checking)
        self.checkWordBtn.clicked.connect(self.check_word_or_stop_checking)
        self.startPlottingBtn.clicked.connect(self.plotting)
        self.algorithmCombo.currentIndexChanged.connect(self.switch_algorithms)
        self.saveAct.triggered.connect(self.save)

    def load_mt(self) -> None:
        if not ALGORITHM_PATH.exists() or not os.listdir(ALGORITHM_PATH):
            QMessageBox.critical(
                self,
                "Алгоритмы не найдены",
                "Не удалось распознать ни одного алгоритма в папке src/algorithm! Создайте хотя бы один файл алгоритма"
                " в этом  и попробуйте снова.",
            )
            sys.exit(-1)

        prev_lang = self.active_MT.lang if self.active_MT else None
        self.algorithmCombo.clear()
        for p in ALGORITHM_PATH.iterdir():
            if p.name.endswith(".tur"):
                try:
                    mt = TuringMachine(p)
                except ValueError as e:
                    QMessageBox.warning(
                        self,
                        "Ошибка парсинга алгоритма",
                        f"При парсинге файла \"{p.name}\" произошла ошибка.\n\n{e}",
                    )
                else:
                    self.loaded_MTs.append(mt)
                    if prev_lang and mt.lang == prev_lang:
                        self.active_MT = mt
                    self.algorithmCombo.addItem(mt.lang)
        if self.active_MT is None:
            self.algorithmCombo.setCurrentIndex(0)
            self.switch_algorithms(0)

    def switch_algorithms(self, index: int) -> None:
        self.active_MT = self.loaded_MTs[index]
        alphabet_validator = QRegExpValidator(
            QRegExp(f"[{''.join(self.active_MT.alphabet)}]*"),
        )
        self.wordTextInp.setValidator(alphabet_validator)

    def check_word_or_stop_checking(self) -> None:
        if self.check_word_thread and self.check_word_thread.isRunning():
            self.check_word_thread.continue_flag = False
            self.checkWordBtn.setText("Проверить")
        else:
            self.turingProtocolTextOutp.clear()
            if self.algDevModeAct.isChecked():
                try:
                    self.active_MT.reload()
                except ValueError as e:
                    QMessageBox.warning(
                        self,
                        "Ошибка парсинга алгоритма",
                        f"При парсинге файла \"{self.active_MT.filename}\" произошла ошибка.\n\n{e}",
                    )
                    return
            self.check_word_thread = CheckWordThread(
                self.active_MT,
                self.wordTextInp.text(),
            )
            self.check_word_thread.step_passed.connect(
                lambda log_str: self.turingProtocolTextOutp.textCursor().insertText(log_str),
            )
            self.check_word_thread.result_got.connect(self.word_checked)
            self.check_word_thread.start()
            self.checkWordBtn.setText("Завершить")

    def word_checked(self, result: str) -> None:
        self.checkWordBtn.setText("Проверить")
        self.turingProtocolTextOutp.textCursor().insertText(result)
        self.statusbar.showMessage(result)
        self.save_act_update_state()

    def plotting(self) -> None:
        if self.plotting_thread and self.plotting_thread.isRunning():
            self.plotting_thread.continue_flag = False
            self.startPlottingBtn.setText("Начать построение")
        else:
            self.statusbar.clearMessage()
            self.plotWidg.clear()
            if self.algDevModeAct.isChecked():
                try:
                    self.active_MT.reload()
                except ValueError as e:
                    QMessageBox.warning(
                        self,
                        "Ошибка парсинга алгоритма",
                        f"При парсинге файла \"{self.active_MT.filename}\" произошла ошибка.\n\n{e}",
                    )
                    return
            self.plotting_thread = PlottingThread(self.active_MT)
            self.plotting_thread.iteration_passed.connect(self.update_plot)
            self.plotting_thread.finished.connect(self.iterations_data.clear)
            self.plotting_thread.start()
            self.startPlottingBtn.setText("Завершить построение")
        self.save_act_update_state()

    def update_plot(self, new_iterations_count: int) -> None:
        self.iterations_data.append(new_iterations_count)
        self.plotWidg.plot(self.iterations_data)

    def save_act_update_state(self) -> None:
        if self.tabWidg.currentWidget() is self.checkWordTab:
            self.saveAct.setText("Сохранить протокол")
            self.saveAct.setEnabled(
                bool(self.check_word_thread)
                and not self.check_word_thread.isRunning(),
            )
        else:
            self.saveAct.setText("Сохранить график")
            self.saveAct.setEnabled(self.plotting_thread is not None)

    def save(self) -> None:
        if self.tabWidg.currentIndex() == 0:
            filename = QtWidgets.QFileDialog.getSaveFileName(
                parent=self,
                filter="Текстовые файлы (*.txt)",
                caption="Выберите файл для сохранения протокола работы МТ",
            )[0]
            if filename:
                if not filename.endswith(".txt"):
                    filename += ".txt"
                with Path(filename).open(mode="w", encoding="utf8") as file:
                    file.write(self.turingProtocolTextOutp.toPlainText())
        else:
            filename = QtWidgets.QFileDialog.getSaveFileName(
                parent=self,
                filter="Изображения (*.png)",
                caption="Выберите файл для сохранения графика",
            )[0]
            if filename:
                if not filename.endswith(".png"):
                    filename += ".png"
                exporter = exporters.ImageExporter(self.plotWidg.scene())
                exporter.parameters()["width"] = 1920
                exporter.export(filename)


def set_plot_theme(app: QApplication) -> None:
    palette = app.palette()
    light_theme_enabled = palette.color(QPalette.ColorRole.Window).lightness() > 128
    background_color, foreground_color = ("w", "k") if light_theme_enabled else ("k", "w")

    pg.setConfigOption("background", background_color)
    pg.setConfigOption("foreground", foreground_color)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    set_plot_theme(app)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
