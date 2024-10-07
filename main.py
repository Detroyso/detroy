from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from random import shuffle

# Вопросы для викторины
questions = [
    {
        "question": "Какой тип данных в Python используется для хранения текста?",
        "options": ["int", "str", "list", "bool"],
        "answer": "str"
    },
    {
        "question": "Какой символ используется для обозначения комментариев в Python?",
        "options": ["#", "//", "/*", "!"],
        "answer": "#"
    },
    {
        "question": "Какой метод используется для добавления элемента в список?",
        "options": [".append()", ".add()", ".insert()", ".extend()"],
        "answer": ".append()"
    }
]

KV = '''
ScreenManager:
    MainScreen:

<MainScreen>:
    name: 'main'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)

        MDLabel:
            id: question_label
            text: "Вопрос появится здесь"
            halign: "center"
            theme_text_color: "Primary"
            font_style: "H5"

        BoxLayout:
            orientation: 'vertical'
            spacing: dp(10)

            MDRaisedButton:
                id: btn1
                text: "Вариант 1"
                on_press: app.check_answer(self)

            MDRaisedButton:
                id: btn2
                text: "Вариант 2"
                on_press: app.check_answer(self)

            MDRaisedButton:
                id: btn3
                text: "Вариант 3"
                on_press: app.check_answer(self)

            MDRaisedButton:
                id: btn4
                text: "Вариант 4"
                on_press: app.check_answer(self)

        MDLabel:
            text: "Ответьте на все вопросы"
            halign: "center"
'''

class MainScreen(Screen):
    pass

class QuizApp(MDApp):
    def build(self):
        self.score = 0
        self.index = 0
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def on_start(self):
        self.update_question()

    def update_question(self):
        if self.index < len(questions):
            current_question = questions[self.index]
            self.root.get_screen('main').ids.question_label.text = current_question["question"]
            options = current_question["options"]
            shuffle(options)
            self.root.get_screen('main').ids.btn1.text = options[0]
            self.root.get_screen('main').ids.btn2.text = options[1]
            self.root.get_screen('main').ids.btn3.text = options[2]
            self.root.get_screen('main').ids.btn4.text = options[3]
        else:
            self.show_result()

    def check_answer(self, instance):
        current_question = questions[self.index]
        if instance.text == current_question["answer"]:
            self.score += 1
        self.index += 1
        self.update_question()

    def show_result(self):
        dialog = MDDialog(
            title="Результат",
            text=f"Ваш счёт: {self.score} из {len(questions)}",
            buttons=[MDFlatButton(text="OK", on_release=self.close_dialog)]
        )
        dialog.open()

    def close_dialog(self, instance):
        instance.parent.parent.dismiss()
        self.stop()

if __name__ == '__main__':
    QuizApp().run()
