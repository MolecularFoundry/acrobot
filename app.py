import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


class TrayApp:
    def __init__(self, icon_path="acrobot-icon.png"):
        self.app = QApplication([])
        self.app.setQuitOnLastWindowClosed(False)

        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon(icon_path))
        self.tray.setVisible(True)

        self.menu = QMenu()

        # Add a menu item
        self.action = QAction("Acronym Search")
        self.action.triggered.connect(self.showDialog)
        self.menu.addAction(self.action)

        # Add a Quit option
        self.quit_action = QAction("Quit")
        self.quit_action.triggered.connect(self.app.quit)
        self.menu.addAction(self.quit_action)

        self.tray.setContextMenu(self.menu)
        
    def showDialog(self):
        text, ok = QInputDialog.getText(QWidget(), 'input dialog', 'what acronym?')
        if ok:
            print(str(text))

    def run(self):
        self.app.exec_()
    

# Example usage:
if __name__ == "__main__":
    app = TrayApp()
    app.run()





































# import sys
# from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu,  QLineEdit, QWidget, QVBoxLayout, QLabel
# from PySide6.QtGui import QIcon, QAction
# from PySide6.QtCore import Qt

# class QueryPopup(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowFlags(Qt.Popup)
#         layout = QVBoxLayout()
#         self.input = QLineEdit()
#         self.input.setPlaceholderText("Check for an acronym...")
#         self.input.returnPressed.connect(self.handle_query)
#         self.answer_label = QLabel("")
#         layout.addWidget(self.input)
#         layout.addWidget(self.answer_label)
#         self.setLayout(layout)

#     def handle_query(self):
#         acronym = self.input.text()
#         # TODO: Query your DB here and replace with real answer

        
#         answer = f"{acronym} stands for: "
#         self.answer_label.setText(answer)

# class TrayApp:
#     def __init__(self):
#         self.app = QApplication(sys.argv)
#         self.tray_icon = QSystemTrayIcon(QIcon("icon.png"))
#         self.menu = QMenu()
#         self.popup = QueryPopup()

#         show_action = QAction("Ask a Question")
#         show_action.triggered.connect(self.show_popup)
#         quit_action = QAction("Quit")
#         quit_action.triggered.connect(self.app.quit)

#         self.menu.addAction(show_action)
#         self.menu.addAction(quit_action)

#         self.tray_icon.setContextMenu(self.menu)
#         self.tray_icon.show()

#     def show_popup(self):
#         self.popup.move(QApplication.primaryScreen().availableGeometry().center() - self.popup.rect().center())
#         self.popup.show()
#         self.popup.activateWindow()
#         self.popup.input.setFocus()

#     def run(self):
#         sys.exit(self.app.exec())

# if __name__ == "__main__":
#     TrayApp().run()
