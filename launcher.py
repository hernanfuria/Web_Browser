from global_imports import *
from main_application_ui import WebBrowserMainUI


def launcher():
    app = QApplication(sys.argv)
    ft_ui = WebBrowserMainUI()
    app.exec_()


if __name__ == '__main__':
    launcher()
