from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PySide6.QtCore import QTimer, QDateTime, QTime, QDate, Qt
from ui.ui_main import Ui_MainWindow
from PySide6.QtGui import QPainter, QColor, QBrush, QPixmap
import random


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('New Year')

        self.is_frame_removed = False
        self.timer = QTimer(self)
        self.snow_effect = SnowEffect(self)
        self.init_()


    def init_(self) -> None:
        self.set_bg_button.clicked.connect(self.select_image)
        self.pin_button.clicked.connect(self.toggle_window)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.setWindowFlag(Qt.FramelessWindowHint, False)
        self.setWindowFlags(Qt.Widget)

        current_date = QDateTime.currentDateTime().date()
        new_year_date = QDate(current_date.year() + 1, 1, 1)
        self.new_year = QDateTime(new_year_date, QTime(0, 0, 0))

        self.snow_effect.raise_()

        self.setCentralWidget(self.centralwidget)

    def toggle_window(self):
        screen_geometry = QApplication.primaryScreen().geometry()

        x = screen_geometry.right() - self.width()
        y = screen_geometry.bottom() - self.height() - 30

        self.move(x, y)

        # self.show()

    def update_time(self) -> None:
        remaining_time = QDateTime.currentDateTime().secsTo(self.new_year)

        if remaining_time <= 0:
            self.time_label.setText('С Новым годом!')
            self.timer.stop()
        else:
            days, rem = divmod(remaining_time, 86400)
            hours, rem1 = divmod(rem, 3600)
            minutes, seconds = divmod(rem1, 60)
            self.time_label.setText(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}")

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать изображение", "", "Images (*.png *.xpm *.jpg)")

        if file_path:
            self.set_background(file_path)

    def set_background(self, file_path):
        self.centralwidget.setStyleSheet(
            f"background-image: url({file_path}); background-position: center; background-repeat: no-repeat;")
        self.centralwidget.repaint()

class SnowEffect(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.setGeometry(0, 0, parent.width(), parent.height())
        self.setAutoFillBackground(False)

        self.snowflakes = []

        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_snowfall)
        self.timer.start(40)

    def update_snowfall(self):
        if random.random() < 0.05 and len(self.snowflakes) < 50:
            snowflake = {
                'x': random.randint(0, self.width()),
                'y': 0,
                'size': random.randint(5, 10),
                'speed': random.randint(1, 3),
            }
            self.snowflakes.append(snowflake)

        for snowflake in self.snowflakes:
            snowflake['y'] += snowflake['speed']
            if snowflake['y'] > self.height():
                snowflake['y'] = 0
                snowflake['x'] = random.randint(0, self.width())

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for snowflake in self.snowflakes:
            painter.setBrush(QBrush(QColor(255, 255, 255)))
            painter.drawEllipse(snowflake['x'], snowflake['y'], snowflake['size'], snowflake['size'])


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
