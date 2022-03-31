# Testing a Python Module with Atheris

To get started with ClusterFuzzLite we need to install Atheris, ClusterFuzzLite's preferred Python fuzzing engine.

We can install the Atheris module through pip with the following command:

`python3 -m pip install atheris`{{execute}}

Atheris uses the Gray-box fuzzing strategy. As stated previously, this means that it knows partial information about the structure of the target and uses code coverage as the metric to improve the inputs that it feeds the target.

Create a new file titled myFirstFuzz.py:

`touch myFirstFuzz.py`{{execute}}

<pre class="file" data-filename="myFirstFuzz.py" data-target="replace">
import atheris
import sys

def myTarget(data):
    if data == b'caught!':
        raise RuntimeError("The error in the code has been found.")

atheris.Setup(sys.argv, myTarget)
atheris.Fuzz()
</pre>

`python3 myFirstFuzz.py`{{execute}}

<pre class="file" data-filename="myFirstFuzz.py" data-target="insert" data-marker="def myTarget(data)">
@atheris.instrument_func
</pre>

`python3 myFirstFuzz.py`{{execute}}


<pre class="file" data-filename="test2.py" data-target="replace">
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