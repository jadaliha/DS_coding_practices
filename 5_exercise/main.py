#!/usr/bin/env python3
"""
Module Docstring

Use funsql to sent an email with data density and other info

"""

__author__ = "Mahdi Jadaliha"
__version__ = "0.2.0"
__license__ = "MIT"


import os
import sys

from InquirerPy import prompt


from rich import inspect, pretty, print
pretty.install()
i = lambda x: inspect(x,methods = True)



def prompt_input():
    questions = [
        {"type": "input", "message": "What's your name:", "name": "name"},
        {
            "type": "list",
            "message": "What's your favourite programming language:",
            "choices": ["Go", "Python", "Rust", "JavaScript"],
        },
        {"type": "confirm", "message": "Confirm?"},
    ]
    return prompt(questions)

    


if __name__ == "__main__":
    print("===Enviroment Values:======")
    print(os.environ['PG_BASE'])
    print("=====Parsed Values:========")
    print(sys.argv)
    print("=====Prompts values:=======")
    prop_results = prompt_input()
    print(prop_results)




import yagmail
yag = yagmail.SMTP('ds.coding.practices@gmail.com', 'Welcome!@#1')
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.', '/local/path/song.mp3']
yag.send('jadaliha@gmail.com', 'subject', contents)

