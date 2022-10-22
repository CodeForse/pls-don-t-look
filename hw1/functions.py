import webbrowser
from typing import List
import os


def set_invitation_htmls(couples:List[tuple]):
    iter=1
    for couple in couples:
        with open('./files/wedding_{}.html'.format(iter),'w',encoding='utf-8') as f:
            iter+=1
            message = """<html>
                <head></head>
                <body><p>Dear {} and {} we invite you to the wedding of our children</p></body>
                </html>""".format(couple[0],couple[1])  
            f.write(message)

# set_invitation_htmls([('Mr. Smith', 'Mrs. Smith')])

def open_files():
    
    for filename in os.listdir('./files/'):
        webbrowser.open('file://'+os.path.realpath('./files/'+filename))
# open_files()