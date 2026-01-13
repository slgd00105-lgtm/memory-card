from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QHBoxLayout, QGroupBox, QButtonGroup
from random import shuffle

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Box')
main_win.resize(550, 300)
main_win.number = -1

counter = 0

class Question():
    def __init__(self, text, right, wrong1, wrong2, wrong3):
        self.question = text
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = [
    Question('Какой из перечисленных самый большой континент?', 'Азия','Европа','Африка','Северная америка'),
    Question('Какая самая высокая гора в мире?', 'Эверест','Макалу','Чогори','Канченджага'),
    Question('Какая самая длинная река в мире?', 'Амазонка','Енисей','Нил','Миссури'),
    Question('Самое глубокое озеро?', 'Байкал','Тангаинька','Восток','Мартин'),
    Question('Чем отличается остров от полуострова', 'полуостров соединен с материком','полуостров больше острова','полуостров это половина острова','это синоним'),
    Question('Какая самая высокая гора в солнечной системе?', 'Олимп','Эверест','Лхоцзе','Чогори'),
    Question('Какая из стран с наибольшим населением?', 'Индия','Турция','Америка','Россия'),
    Question('Какой стране пренадлежит антарктида?', 'Большое кол-во стран','Франция','Австралия','Россия'),
    Question('Какой море самое большое по площади?', 'Саргассово море','Черное море','Карское море','Коралловое море'),
    Question('В каком океане находится точка немо? (самая дальняя точка от суши)', 'Тихий океан','Атлантический океан','Индийский океан','Северный ледовитый океан')
]

shuffle(questions_list)

def show_result():
    qwin.hide()
    awin.show()
    button.setText('Следующий вопрос')

def show_question():
    answers.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    answers.setExclusive(True)

    awin.hide()
    qwin.show()
    button.setText('Ответить')

def ask(q):
    shuffle(rbuttons)
    rbuttons[0].setText(q.right)
    rbuttons[1].setText(q.wrong1)
    rbuttons[2].setText(q.wrong2)
    rbuttons[3].setText(q.wrong3)
    question.setText(q.question)
    rightness.setText(f'Правильный ответ: {q.right}')
    show_question()

def check_answer():
    global counter
    if rbuttons[0].isChecked():
        w_l.setText('Правильно')
        show_result()
        counter += 1
    elif rbuttons[1].isChecked() or rbuttons[2].isChecked() or rbuttons[3].isChecked():
        w_l.setText('Неправильно')
        show_result()

def next_question():
    main_win.number += 1
    if main_win.number >= len(questions_list):
        ewin = QMessageBox()
        ewin.setText(f'Правильных ответов: {counter}/{len(questions_list)} \n{counter/len(questions_list)*100}%')
        ewin.exec_()
        button.setText('Завершить')
    else:
        q = questions_list[main_win.number]
        ask(q)

def click():
    if button.text() == 'Ответить':
        check_answer()
    elif button.text() == 'Завершить':
        app.quit()
    else:
        next_question()

qwin = QGroupBox('Варианты ответов')
awin = QGroupBox('Ответ')

question = QLabel('Вопрос')
button = QPushButton('Ответить')

layout = QVBoxLayout()

answers = QButtonGroup()
ans1 = QRadioButton('ответ')
ans2 = QRadioButton('ответ')
ans3 = QRadioButton('ответ')
ans4 = QRadioButton('ответ')
rbuttons = [ans1, ans2, ans3, ans4]
    

answers.addButton(ans1)
answers.addButton(ans2)
answers.addButton(ans3)
answers.addButton(ans4)

qwlayouth = QHBoxLayout()
qwlayoutv1 = QVBoxLayout()
qwlayoutv2 = QVBoxLayout()
group_line = QHBoxLayout()

# first

qwlayoutv1.addWidget(ans1, alignment=Qt.AlignCenter)
qwlayoutv1.addWidget(ans2, alignment=Qt.AlignCenter)
qwlayoutv2.addWidget(ans3, alignment=Qt.AlignCenter)
qwlayoutv2.addWidget(ans4, alignment=Qt.AlignCenter)

qwlayouth.addLayout(qwlayoutv1)
qwlayouth.addLayout(qwlayoutv2)

qwin.setLayout(qwlayouth)

group_line.addWidget(qwin, alignment = Qt.AlignVCenter, stretch = 16)

# second

rightness = QLabel('Правильный ответ!')
w_l = QLabel('Правильно/Неправильно')

alayout = QVBoxLayout()

alayout.addWidget(w_l, alignment = Qt.AlignLeft)
alayout.addWidget(rightness, alignment = Qt.AlignCenter)

awin.setLayout(alayout)

layout.addWidget(question, alignment = Qt.AlignCenter, stretch = 2)
layout.addWidget(awin, alignment = Qt.AlignVCenter)
layout.addLayout(group_line)
layout.addWidget(button, alignment = Qt.AlignCenter, stretch = 2)

awin.hide()

main_win.setLayout(layout)

button.clicked.connect(click)
next_question()

main_win.show()
app.exec_()