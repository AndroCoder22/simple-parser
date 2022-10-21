import requests
from bs4 import BeautifulSoup as BS
import webbrowser

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

r = requests.get("https://pdalife.to/android/adventure/")
h = BS(r.content, "lxml")
result = h.find_all("a", class_ = "color-android")
hrefs = []
texts = []
for i in range(len(result)):
    hrefs.append(result[i].get("href"))
    texts.append(result[i].text.strip())


class app(App):
    def build(self):
        layout = GridLayout(cols = 1, size_hint_y = len(texts)/18)
        sv = ScrollView()
        for i in range(len(texts)):
            btn = Button(text = texts[i-1])
            btn.bind(on_release = self.open)
            layout.add_widget(btn)
        sv.add_widget(layout)
        return sv
    def open(self, instance):
        i = texts.index(instance.text)
        webbrowser.open(f"https://pdalife.to/android/adventure{hrefs[i]}")
        
app().run()