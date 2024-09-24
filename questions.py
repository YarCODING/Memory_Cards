from PyQt5.QtWidgets import QLabel, QRadioButton

# Лічильник правильних і неправильних відповідей
correct = 0
wrong = 0

class Question:
    def __init__(self, question_text:str, answer_right:str, answer_wrong1:str, answer_wrong2:str, answer_wrong3:str):
        self.question_text = question_text
        self.rightAnswer = answer_right
        self.wrongAnswer1 = answer_wrong1
        self.wrongAnswer2 = answer_wrong2
        self.wrongAnswer3 = answer_wrong3
        questions.append(self)

    def show(self, lb_question: QLabel, rbuttons:QLabel, index: int):
        lb_question.setText(f"{index+1}. {self.question_text}")
        rbuttons[0].setText(self.rightAnswer)
        rbuttons[1].setText(self.wrongAnswer1)
        rbuttons[2].setText(self.wrongAnswer2)
        rbuttons[3].setText(self.wrongAnswer3)

    def check(self, lb_user_answer:QLabel, rbList:list, lb_answer:QLabel, lb_result:QLabel):
        global correct, wrong
        if rbList[0].isChecked():
            lb_user_answer.setText(self.rightAnswer)
            correct += 1
        elif rbList[1].isChecked():
            lb_user_answer.setText(self.wrongAnswer1)
            wrong += 1
        elif rbList[2].isChecked():
            lb_user_answer.setText(self.wrongAnswer1)
            wrong += 1
        elif rbList[3].isChecked():
            lb_user_answer.setText(self.wrongAnswer1)
            wrong += 1
        else:
            wrong += 1

        lb_answer.setText(self.rightAnswer)

        if lb_user_answer.text() == self.rightAnswer:
            lb_result.setText('<h1 style="color: rgb(50,205,50);">Правильно</h1>')
        else:
            lb_result.setText('<h1 style="color: rgb(250, 55, 55);">Неправильно</h1>')
    
    def showEndResult(self, lb_right_number: QLabel, lb_wrong_number:QLabel, lb_finish_text:QLabel):
        global correct, wrong
        lb_finish_text.show()
        lb_right_number.setText(f'<h2 style="color: rgb(50,205,50);">Правильних: {correct}</h2>')
        lb_wrong_number.setText(f'<h2 style="color: rgb(250, 55, 55);">Неправильних: {wrong}</h2>')
        lb_right_number.show()
        lb_wrong_number.show()

# створення питань
questions = []
Question('В якому році почалася 2 Світова Війна?', '1939', '1940', '1950', '1914')
Question('Скільки важить кілограм афальту, якщо папуга летить на північ?', '1 кг', '1 т', '2 кг', '10 кг')
Question('В якому році з\'явився мем Жабеня Пєпє?', '2005', '2010', '1999', '2020')
Question('Що є національною твариною Шотландії?', 'Эдиноріг', 'Кінь', 'Вовк', 'Корова')
Question('Який безалкогольний напій першим узяли в космос?', 'Кока-Кола', 'Фанта', 'Пепсі', 'Спрайт')
Question('Як називався батончик "Снікерс" до його зміни назви в 1990 році?', 'Marathon', 'Race', 'Smile', 'Sprint')
Question('Хто винайшов лампочку?', 'Томас Едісон', 'Альберт Ейнштейн', 'Ісаак Ньютон', 'Нікола Тесла')
Question('Який елемент першим з\'являється у періодичній таблиці?', 'Гідроген', 'Гелій', 'Карбон', 'Оксиген')
Question('Який рік вважається початком Середньовіччя?', '476', '800', '1453', '1492')
Question('Який математик вперше ввів символ нескінченності (∞)?', 'Джон Валліс', 'Ісаак Ньютон', 'Леонард Ейлер', 'Карл Гаусс')
Question('Як називається перший штучний супутник Землі?', 'Супутник-1', 'Аполлон-11', 'Вояджер-1', 'Марінер-4')
Question('Що таке "філософський камінь" у середньовічній алхімії?', 'Міфічна речовина, яка нібито могла перетворювати метали на золото', 'Камінь, що наділяв безсмертям', 'Магічний інструмент для передбачення майбутнього', 'Символ досконалості людини')
Question('Що таке суперпозиція у квантовій фізиці?', 'Стан, коли частинка може перебувати одночасно у кількох станах', 'Злиття двох хвиль у одну', 'Взаємодія електромагнітних полів', 'Підвищення енергії частинки до максимуму')
Question('Що робить персонаж у мемі "This is fine"?', 'Сидить у палаючій кімнаті і каже, що все добре', 'Танцює на вулиці під дощем', 'П\'є каву на фоні вибуху', 'Втікає від падаючого метеориту')
Question('Чого не може торнадо?', 'Стояти на місці', 'Підняти у повітря автомобіль', 'Вирвати з корінням дерево', 'Зруйнувати будівлю')
Question('Як називається приміщення на судні, де мешкають матроси?', 'Кубрик', 'Келія', 'Квартира', 'Кабінет')
# Question('', '', '', '', '')