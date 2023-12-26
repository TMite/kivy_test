from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

class ConverterApp(MDApp):
    def flip(self):
        print("flipping")
    def convert(self, args):
        output = int(self.input.text,2)
        self.converted.text = str(output)
    def build(self):
        screen = MDScreen()
        self.toolbar = MDTopAppBar(title="Binary to Deci")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [["rotate-3d-variant", lambda x: self.flip()]]
        screen.add_widget(self.toolbar)

        self.input = MDTextField(
            text="Binary Number",
            halign="center",
            size_hint=(0.8,1),
            pos_hint = {"center_x": .5, "center_y": .45}
        )
        screen.add_widget(self.input)

        self.label = MDLabel(
            text="Decimal: ",
            halign="center",
            pos_hint = {"center_x": .5, "center_y": .35}
        )
        self.converted = MDLabel(
            text="---: ",
            halign="center",
            pos_hint = {"center_x": .5, "center_y": .3},
            font_style = "H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        screen.add_widget(MDFillRoundFlatButton(
            text="SUBMIT",
            font_size = 15,
            pos_hint = {"center_x": .5, "center_y": .12},
            on_press =self.convert
        ))
                                 
        #UI Widgets go here
        return screen
        
if __name__ == '__main__':
    ConverterApp().run()