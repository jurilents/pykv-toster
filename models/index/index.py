from kivy.app import App

class IndexApp(App):
    def build(self):
        return

    def button1_on_press(self):
        print("Idy u sraku\ntochnishe ya hotil stazaty\n\"Hello World!\"")


if __name__ == '__main__':
    app = IndexApp()
    app.run()