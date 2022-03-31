# from html.parser import HTMLParser
# from pythonfuzz.main import PythonFuzz
import atheris

# with atheris.instrument_imports():
# #   from html.parser import HTMLParser
from bs4 import BeautifulSoup
#   import sys

# def TestOneInput(data):
#     try:
#         string = data.decode('utf-8')
#         # parser = HTMLParser()
#         # parser.feed(string)
#         soup = BeautifulSoup(string, 'html.parser')
#     except UnicodeDecodeError:
#         pass

# atheris.Setup(sys.argv, TestOneInput)
# atheris.Fuzz()

# BeautifulSoup('<<![5<//@', 'html.parser')