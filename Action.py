import webbrowser
import os
from tkinter import Tk
from tkinter import filedialog


def add_application_path():
    Tk().withdraw()
    filename = filedialog.askopenfilename(initialdir="/", title="Select a file")
    print(filename)


class Action:

    # TODO Has to be stored in database
    application_paths = {}

    @staticmethod
    def open_application(name):
        os.system(name)

    @staticmethod
    def open_website(url):
        webbrowser.open(url)


def main():
    # Action.open_website("www.stackoverflow.com")

    #Action.open_application('Google Chrome')
    add_application_path()


if __name__ == '__main__':
    main()
