import atheris
import sys

with atheris.instrument_imports():
  from html.parser import HTMLParser


def TestOneInput(data):
    try:
        string = data.decode('utf-8')
        parser = HTMLParser()
        parser.feed(string)
    except UnicodeDecodeError:
        pass

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
