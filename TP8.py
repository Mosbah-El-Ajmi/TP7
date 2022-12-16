from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout

class GridApp(App):
    def build(self):
        grid = GridLayout(cols=5, rows=5, spacing=2, padding=2)
        for i in range(25):
            btn = Button(text="", background_color=(1, 1, 1, 1))
            btn.bind(on_press=self.on_button_press)
            grid.add_widget(btn)

        return grid

    def on_button_press(self, instance):
        instance.background_color = (0, 0, 1, 1)

class Calculette(App):

    def build(self):

        layout = BoxLayout(orientation='vertical')
        input_layout = BoxLayout(orientation='horizontal')
        self.text_input1 = TextInput(text='', multiline=False)
        self.text_input2 = TextInput(text='', multiline=False)
        self.button = Button(text='Calculer')
        self.button.bind(on_press=self.calcul)
        input_layout.add_widget(self.text_input1)
        input_layout.add_widget(self.text_input2)
        input_layout.add_widget(self.button)

        #les checkbox , seulement une ne peut etre choisie
        operation_layout = BoxLayout(orientation='horizontal')
        self.add_checkbox = CheckBox(active=True, group="operation", allow_no_selection=False)
        self.sub_checkbox = CheckBox(group="operation", allow_no_selection=False)
        self.mul_checkbox = CheckBox(group="operation", allow_no_selection=False)
        self.div_checkbox = CheckBox(group="operation", allow_no_selection=False)

        #choix du type de calcul dans les checkbox
        operation_layout.add_widget(Label(text='Addition'))
        operation_layout.add_widget(self.add_checkbox)
        operation_layout.add_widget(Label(text='Soustraction'))
        operation_layout.add_widget(self.sub_checkbox)
        operation_layout.add_widget(Label(text='Multiplication'))
        operation_layout.add_widget(self.mul_checkbox)
        operation_layout.add_widget(Label(text='Division'))
        operation_layout.add_widget(self.div_checkbox)

        #affichage du resultat
        self.result_label = Label(text='')
        layout.add_widget(input_layout)
        layout.add_widget(operation_layout)
        layout.add_widget(self.result_label)

        return layout

    def Grid(self):
        grid = GridLayout(cols=5, rows=5, spacing=2, padding=2)
        for i in range(25):
            btn = Button(text="", background_color=(1, 1, 1, 1))
            btn.bind(on_press=self.on_button_press)
            grid.add_widget(btn)

        return grid

    def on_button_press(self, instance):
        instance.background_color = (0, 0, 1, 1)

    def calcul(self, instance):
        num1 = self.text_input1.text
        num2 = self.text_input2.text
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            if self.add_checkbox.active:
                result = num1 + num2
            elif self.sub_checkbox.active:
                result = num1 - num2
            elif self.mul_checkbox.active:
                result = num1 * num2
            elif self.div_checkbox.active:
                result = num1 / num2
            self.result_label.text = str(result)
        else:
            self.result_label.text = "Erreur : veuillez entrer des nombres valides"

if __name__ == '__main__':
    Calculette().run()
    GridApp().run()
