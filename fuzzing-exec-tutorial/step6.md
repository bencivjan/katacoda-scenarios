# Fuzzing a Python Library with Atheris

We just fuzzed our own function successfully, but we can fuzz other libraries with Atheris as well. Let's take a look at a popular Python library that parses HTML.

First create a function called libFuzzing.py:

`touch libFuzzing.py`{{execute}}

And insert the following code into the file:

<pre class="file" data-filename="libFuzzing.py" data-target="replace">
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

It should be apparent that we are unable to instrument the specific function that we are testing, because we don't have immediate access to the source code. To be able to still instrument the function that we are testing, we import the libraries under `with atheris.instrument_imports()`. This tells Atheris to instrument these libraries before fuzzing.

Now run the code with `python3 libFuzzing.py`{{execute}}

We now notice that HTMLParser() has raised an error. To check the input that caused it to crash, open the auto-generated crash log in the current directory.

At first glance, it seems that since the HTML we fed the parser was invalid, this should be expected behavior. However, according to the HTMLParser docs: "Parsing invalid HTML (e.g. unquoted attributes) also works".<sup>5</sup> So it seems we have found a real bug in a real-world library!

In fact, this bug has been brought up in developer forums and you can follow the progress [here](https://bugs.python.org/issue32876).

***Can you find the secret bug?***
Without looking at the source code, see if you can reveal the secret bug in `fuzz_for_secret.py`

Hints:

Make sure to instrument `from fuzz_for_secret import main`

`main` takes a string as input

Put the bug input into a browser for a surprise :)
