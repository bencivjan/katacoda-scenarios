from html.parser import HTMLParser
# from pythonfuzz.main import PythonFuzz

parser = HTMLParser()
print(parser.feed("<<>![&]P>><<!*^"))
# The value <<![& breaks it

# @PythonFuzz
# def fuzz(buf):
#     try:
#         string = buf.decode("ascii")
#         print(string)
#         parser = HTMLParser()
#         parser.feed(string)
#     except UnicodeDecodeError:
#         pass


# if __name__ == '__main__':
#     fuzz()
    
    
# import atheris

# with atheris.instrument_imports():
#   from html.parser import HTMLParser
#   import sys

# def TestOneInput(data):
#     try:
#         string = data.decode('utf-8')
#         parser = HTMLParser()
#         parser.feed(string)
#     except UnicodeDecodeError:
#         pass

# atheris.Setup(sys.argv, TestOneInput)
# atheris.Fuzz()