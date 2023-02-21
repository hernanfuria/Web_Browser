from global_imports import *
from paths import *


class WebPage(QWidget):

    def __init__(self):
        super(WebPage, self).__init__()

        self.tab_v_layout = QVBoxLayout()
        self.search_bar_h_layout = QHBoxLayout()

        self.back_button = QToolButton()
        self.back_button.setIcon(QIcon(back_button_icon_path))
        self.forward_button = QToolButton()
        self.forward_button.setIcon(QIcon(forward_button_icon_path))
        self.search_lineedit = QLineEdit()
        self.search_lineedit.returnPressed.connect(self.searchLineEditEnterKeyPressed)

        self.search_bar_h_layout.addWidget(self.back_button)
        self.search_bar_h_layout.addWidget(self.forward_button)
        self.search_bar_h_layout.addWidget(self.search_lineedit)

        self.web_view = QtWebEngineWidgets.QWebEngineView()
        self.web_view.load(QtCore.QUrl('https://www.google.com'))

        self.tab_v_layout.addLayout(self.search_bar_h_layout)
        self.tab_v_layout.addWidget(self.web_view)

        self.setLayout(self.tab_v_layout)

    def searchLineEditEnterKeyPressed(self):
        typed = self.search_lineedit.text()

        if typed[:4] == 'www.':
            typed = f"https://{typed}"
        else:
            typed = f"https://www.{typed}"

        self.search_lineedit.setText(typed)
        self.web_view.load(QtCore.QUrl(typed))



class WebBrowserMainUI(QMainWindow):

    def __init__(self):
        super(WebBrowserMainUI, self).__init__()

        # load the ui file
        uic.loadUi(web_browser_main_ui_path, self)

        self.initUI()
        self.initBehaviors()

        # show
        self.show()

    def initUI(self):
        self.tabWidget = self.findChild(QTabWidget, 'tabWidget')
        self.addNewTab()

    def initBehaviors(self):
        self.tabWidget: QTabWidget
        self.tabWidget.currentChanged.connect(self.currentTabChanged)

    def currentTabChanged(self):
        self.tabWidget: QTabWidget

        tabs_amount = self.tabWidget.count()
        add_tab_pseudo_tab_index = tabs_amount - 1
        if self.tabWidget.currentIndex() == add_tab_pseudo_tab_index:
            self.addNewTab()

    def addNewTab(self):
        self.tabWidget: QTabWidget

        tab_contents = WebPage()
        insert_index = self.tabWidget.count() - 1
        tab_text = "New tab"
        self.tabWidget.insertTab(insert_index, tab_contents, tab_text)
        self.tabWidget.setCurrentIndex(insert_index)
