`python3 -m pip install atheris`{{execute}}

<pre class="file" data-filename="test.py" data-target="replace">
from html.parser import HTMLParser
from pythonfuzz.main import PythonFuzz


import atheris

with atheris.instrument_imports():
  from html.parser import HTMLParser
  import sys

def TestOneInput(data):
    try:
        string = data.decode('utf-8')
        parser = HTMLParser()
        parser.feed(string)
    except UnicodeDecodeError:
        pass

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
</pre>