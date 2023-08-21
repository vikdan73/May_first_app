from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.button import MDIconButton

class MainApp(MDApp):
    def build(self):
        layout = MDBoxLayout(orientation='vertical')

        mLabel = MDLabel(text="KivyMD", halign="center")


        #mButton = MDRaisedButton(text="Click Me", pos_hint={'center_x': 0.5})
        #mButton.bind(on_release=self.on_button_click)

        mIconButton = MDIconButton(icon="android", pos_hint={'center_x': 0.5})
        mIconButton.bind(on_release=self.on_button_click)

        list_view = MDList()
        item1 = OneLineListItem(text="Item 1")
        item2 = OneLineListItem(text="Item 2")
        item3 = OneLineListItem(text="Item 3")

        list_view.add_widget(item1)
        list_view.add_widget(item2)
        list_view.add_widget(item3)

        layout.add_widget(mLabel)
        layout.add_widget(mIconButton)
        layout.add_widget(list_view)

        return layout

    def on_button_click(self, instance):
        print("Button clicked!")


if __name__ == "__main__":
    MainApp().run()
