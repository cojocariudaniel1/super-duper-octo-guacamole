from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QFrame


class LoadingBar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #FF4500;")  # Reddit orange
        self.setGeometry(0, 0, 0, 4)  # Start at 0 width
        self.hide()  # Initially hidden
        self.loading_progress = 0
        self.loading_timer = QTimer(self)
        self.loading_timer.timeout.connect(self.animate_loading_bar)

    def start_loading(self, duration_ms=1000):
        """Show and animate the loading bar over a given duration."""
        self.loading_progress = 0
        self.setGeometry(0, 0, 0, 4)
        self.show()

        # Calculate the increment for each timer tick
        self.increment_per_tick = self.parent().width() / (duration_ms / 10)  # Update every 10 ms
        self.loading_timer.start(10)  # Timer update every 10 ms

    def stop_loading(self):
        """Stops the animation and hides the loading bar."""
        self.loading_timer.stop()
        self.hide()

    def set_progress(self, progress):
        """Set the loading progress directly."""
        self.loading_progress = (progress * self.parent().width()) // 100
        self.setGeometry(0, 0, self.loading_progress, 4)

    def animate_loading_bar(self):
        """Animates the loading bar by incrementing progress."""
        if self.loading_progress < self.parent().width():  # Only fill the bar up to 100% width
            self.loading_progress += self.increment_per_tick  # Increment the progress
            self.setGeometry(0, 0, self.loading_progress, 4)
        else:
            self.loading_progress = self.parent().width()  # Ensure it's full
            self.setGeometry(0, 0, self.loading_progress, 4)
            self.loading_timer.stop()  # Stop animation once the bar is filled
