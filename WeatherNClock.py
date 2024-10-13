from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    QEasingCurve,
    QPropertyAnimation
)
from PySide6.QtGui import (
    QFont,
    QIcon,
    QPainter,
    QPixmap,
    QPainterPath,
    QMovie
)
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QWidget,
    QStackedWidget,
    QGraphicsOpacityEffect,
    QMenu,
    QSizePolicy, QLineEdit
)
from PySide6.QtCore import (
    QTimer,
    QTime,
    Qt
)

import requests
import json


def set_rounded_image(pixmap, width, height, radius):
    # 이미지 크기 맞추기
    pixmap = pixmap.scaled(width, height, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

    # 새로운 QPixmap 생성
    rounded_pixmap = QPixmap(width, height)
    rounded_pixmap.fill(Qt.transparent)  # 투명 배경

    # QPainter 설정
    painter = QPainter(rounded_pixmap)
    painter.setRenderHint(QPainter.Antialiasing, True)

    # 둥근 영역을 마스크로 설정하여 클리핑
    path = QPainterPath()
    path.addRoundedRect(0, 0, width, height, radius, radius)
    painter.setClipPath(path)  # 둥근 모서리 클리핑 설정

    # 이미지를 그리기
    painter.drawPixmap(0, 0, pixmap)

    painter.end()

    return rounded_pixmap


class FadeStackedWidget(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.current_opacity_effects = []
        self.next_opacity_effects = []
        self.fade_out_animations = []
        self.fade_in_animations = []

    def fade_to(self, index):
        if index == self.currentIndex():
            return  # 이미 해당 페이지가 표시 중인 경우 아무 동작도 하지 않음

        current_widget = self.currentWidget()
        next_widget = self.widget(index)

        # 현재 페이지 내 모든 위젯에 대해 페이드 아웃 애니메이션 설정
        self.current_opacity_effects = []
        self.fade_out_animations = []

        for child in current_widget.findChildren(QWidget):
            opacity_effect = QGraphicsOpacityEffect()
            child.setGraphicsEffect(opacity_effect)
            self.current_opacity_effects.append(opacity_effect)

            fade_out_animation = QPropertyAnimation(opacity_effect, b"opacity")
            fade_out_animation.setDuration(300)  # 500ms
            fade_out_animation.setStartValue(1)
            fade_out_animation.setEndValue(0)
            fade_out_animation.setEasingCurve(QEasingCurve.InOutQuad)
            fade_out_animation.start()

            self.fade_out_animations.append(fade_out_animation)

        self.fade_out_animations[0].finished.connect(lambda: self.on_fade_out_finished(index))

    def on_fade_out_finished(self, index):
        # 페이지 전환
        self.setCurrentIndex(index)

        # 새 페이지 내 모든 위젯에 대해 페이드 인 애니메이션 설정
        new_widget = self.currentWidget()
        self.next_opacity_effects = []
        self.fade_in_animations = []

        for child in new_widget.findChildren(QWidget):
            opacity_effect = QGraphicsOpacityEffect()
            child.setGraphicsEffect(opacity_effect)
            self.next_opacity_effects.append(opacity_effect)

            fade_in_animation = QPropertyAnimation(opacity_effect, b"opacity")
            fade_in_animation.setDuration(300)  # 500ms
            fade_in_animation.setStartValue(0)
            fade_in_animation.setEndValue(1)
            fade_in_animation.setEasingCurve(QEasingCurve.InOutQuad)
            fade_in_animation.start()

            self.fade_in_animations.append(fade_in_animation)

        self.fade_in_animations[0].finished.connect(lambda: self.on_fade_in_finished(new_widget))

    def on_fade_in_finished(self, widget):
        # 페이드 인 완료 후 QGraphicsOpacityEffect 제거
        for child in widget.findChildren(QWidget):
            child.setGraphicsEffect(None)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 500)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.stacked_widget = FadeStackedWidget()
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.stacked_widget.setParent(self.centralwidget)
        self.stacked_widget.setGeometry(QRect(0, 0, 720, 500))

        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")

        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setBold(True)
        font3 = QFont()
        font3.setFamilies([u"\ud55c\ucef4 \ub9d0\ub791\ub9d0\ub791 Regular"])
        font3.setPointSize(17)

### page1 상속 개체
        # 날씨에 따른 배경
        self.background_label = QLabel(self.page1)
        #self.background_label.setPixmap(set_rounded_image(QPixmap(r"weather_clear_background.jpg"), 675, 410, radius=10))
        self.background_label.setGeometry(QRect(23, 23, 675, 410))

        # 온도 표시 라벨
        self.label_2 = QLabel(self.page1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 440, 101, 50))
        self.label_2.setFont(font3)

        # 위치 표시
        self.location = QLabel(self.page1)
        self.location.setText('Seoul')
        self.location.setGeometry(QRect(138, 434, 150, 50))
        font_loc = QFont()
        font_loc.setFamilies([u"\ud55c\ucef4 \ub9d0\ub791\ub9d0\ub791 Regular"])
        font_loc.setPointSize(7)
        self.location.setFont(font_loc)

        # 날짜 표시
        self.date = QLabel(self.page1)
        self.date.setGeometry(QRect(127, 446, 150, 50))
        self.date.setFont(font_loc)

        # 날짜 업데이트
        self.dateTimer = QTimer()
        self.dateTimer.timeout.connect(self.update_date)
        self.dateTimer.start(1000)
        self.update_date()

        # 날씨 아이콘
        self.label_3 = QLabel(self.page1)
        #self.label_3.setPixmap(QPixmap(r"weather_clear.png").scaled(33, 33, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.label_3.setGeometry(QRect(22, 314, 300, 300))

        # 날씨 업데이트
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.update_weather)
        self.timer1.start(100000)
        self.update_weather()

        #위치 아이콘
        self.location_label = QLabel(self.page1)
        self.location_label.setPixmap(QPixmap(r"location.png").scaled(10, 10, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.location_label.setGeometry(QRect(125, 448, 25, 25))

        # 시계
        self.label_4 = QLabel(self.page1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(540, 440, 210, 50))
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.raise_()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 1초마다 update_time 호출
        self.update_time()

        self.stacked_widget.addWidget(self.page1)
### page1 end


        # 홈버튼
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(340, 453, 25, 25))
        icon = QIcon()
        icon.addFile(u"home_icon", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(25, 25))
        self.pushButton.setFlat(True)
        self.pushButton.clicked.connect(lambda: self.stacked_widget.fade_to(0))

        # 설정버튼
        self.pushButton_setting = QPushButton(self.centralwidget)
        self.pushButton_setting.setObjectName(u"pushButton")
        self.pushButton_setting.setGeometry(QRect(375, 453, 25, 25))
        icon = QIcon()
        icon.addFile(u"Settings2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_setting.setIcon(icon)
        self.pushButton_setting.setIconSize(QSize(25, 25))
        self.pushButton_setting.setFlat(True)
        self.pushButton_setting.clicked.connect(lambda: self.stacked_widget.fade_to(1))


#설정 페이지
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")

        self.label_setting_text = QLabel(self.page2)
        self.label_setting_text.setObjectName(u"label_7")
        self.label_setting_text.setGeometry(QRect(30, 15, 101, 50))
        self.label_setting_text.setFont(font3)
        self.label_setting_text.setText("설정")

        self.pushButton_setting_location = QPushButton(self.page2)
        self.pushButton_setting_location.setGeometry(QRect(30, 100, 100, 25))
        self.pushButton_setting_location.setStyleSheet('QPushButton {background-color: rgba(0, 0, 0, 10); border: '
                                                       'none; border-radius: 6px;} QPushButton:hover {'
                                                       'background-color: rgba(0, 0, 0, 40); border-radius: 6px;}'
                                                       'QPushButton:checked {background-color: rgba(0, 0, 0, '
                                                       '90); border-radius: 6px;}')
        self.pushButton_setting_location.setFlat(True)
        self.pushButton_setting_location.setCheckable(True)
        self.pushButton_setting_location.setText(" 지역")
        font_loc_button = QFont()
        font_loc_button.setFamilies([u"\ud55c\ucef4 \ub9d0\ub791\ub9d0\ub791 Regular"])
        font_loc_button.setPointSize(10)
        self.pushButton_setting_location.setFont(font_loc_button)

        self.location_label = QLabel(self.page2)
        self.location_label.setPixmap(
            QPixmap(r"location.png").scaled(15, 15, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.location_label.setGeometry(QRect(38, 101, 25, 25))


        self.location_menu = QPushButton(self.page2)
        self.location_menu.setGeometry(QRect(170, 140, 100, 25))
        self.location_menu.setText("지역 선택")
        menu = QMenu(self.page2)
        locations = ['Daejeon', 'Seoul', 'Suwon']
        for location in locations:
            menu.addAction(location, lambda loc=location: self.update_location(loc))
        self.location_menu.setMenu(menu)


        self.location_lineedit = QLineEdit(self.page2)
        self.location_lineedit.setGeometry(QRect(270, 140, 100, 25))
        self.location_lineedit.setText("Daejeon")
        self.chagelocation = QPushButton(self.page2)
        self.chagelocation.setGeometry(QRect(370, 100, 100, 25))
        self.chagelocation.setText("지역 변경")
        self.chagelocation.clicked.connect(self.locationedit)



        self.stacked_widget.addWidget(self.page2)


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.stacked_widget.setCurrentIndex(0)
        self.fade_in_initial_page()
        QMetaObject.connectSlotsByName(MainWindow)

    def locationedit(self):
        self.update_location(self.location_lineedit.text())

    def update_location(self, city):
        self.location_menu.setText(city)
        self.location.setText(city)
        self.update_weather()

    def update_weather(self):
        city = self.location.text()  # 도시
        apiKey = "eb3a3f5257647e4adf2cc4690798b08e"
        lang = 'kr'  # 언어
        units = 'metric'  # 화씨 온도를 섭씨 온도로 변경
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"
        result = requests.get(api)
        result = json.loads(result.text)
        weather = result['weather'][0]['main']
        temp = str(round(result['main']['temp'])) + ' °C'
        print(weather)

        if weather == "Clouds":
            self.background_label.setPixmap(
                set_rounded_image(QPixmap(r"weather_cloudy_background.jpg"), 675, 410, radius=10))
            self.label_3.setPixmap(
                QPixmap(r"cloudy_icon.png").scaled(30, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        elif weather == "Clear":
            self.background_label.setPixmap(
                set_rounded_image(QPixmap(r"weather_clear_background.jpg"), 675, 410, radius=10))

            self.label_3.setPixmap(
                QPixmap(r"weather_clear.png").scaled(33, 33, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        elif weather == "Rain":
            self.movie = QMovie("rain_background_gif.gif")
            self.movie.setScaledSize(self.background_label.size())
            self.background_label.setMovie(self.movie)
            self.movie.frameChanged.connect(self.update_rounded_frame)
            self.movie.start()
            self.label_3.setPixmap(
                QPixmap(r"rainy_icon.png").scaled(33, 33, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        '''elif time_current[6:8] == "PM":
            self.background_label.setPixmap(
                set_rounded_image(QPixmap(r"dark_background.jpg"), 675, 410, radius=10))
        '''
        #self.location.setText(city)
        self.label_2.setText(temp)

    def update_time(self):
        current_time = QTime.currentTime().toString('hh:mm AP')  # 현재 시간 얻기
        self.label_4.setText(current_time)

    def update_date(self):
        current_date = QDate.currentDate().toString('yyyy/MM/dd (ddd)')
        self.date.setText(current_date)
        return current_date


    def update_rounded_frame(self):
        # Get the current frame as a QPixmap
        current_frame = self.movie.currentPixmap()

        # Apply the rounded effect
        rounded_frame = set_rounded_image(current_frame, self.background_label.width(), self.background_label.height(), radius=10)

        # Set the rounded frame as the QLabel's pixmap
        self.background_label.setPixmap(rounded_frame)

    def fade_in_initial_page(self):
        initial_widget = self.stacked_widget.currentWidget()
        opacity_effect = QGraphicsOpacityEffect()
        initial_widget.setGraphicsEffect(opacity_effect)

        fade_in = QPropertyAnimation(opacity_effect, b"opacity")
        fade_in.setDuration(500)
        fade_in.setStartValue(0)
        fade_in.setEndValue(1)
        fade_in.setEasingCurve(QEasingCurve.InOutQuad)
        fade_in.start()

        # 애니메이션 객체를 참조로 유지하여 가비지 컬렉션 방지
        self.initial_fade_in = fade_in


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Clock v.1 beta", None))
        #self.label.setText(QCoreApplication.translate("MainWindow", u"Clock Beta1", None))



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())