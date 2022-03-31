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

# TODO - instrumentation
def myTarget(data):
    if data == b'caught!':
        raise RuntimeError("The error in the code has been found.")
    else:
        return "All good!"

atheris.Setup(sys.argv, myTarget)
atheris.Fuzz()
</pre>

`python3 myFirstFuzz.py`{{execute}}

After fuzzing this function, we see an interesting output: `ERROR: no interesting inputs were found. Is the code instrumented for coverage? Exiting.`

If we take a look at the Atheris documentation, we see that this error occurs when the first 2 calls to our function didn't produce any coverage events. In our case, the reason for this is that we forgot to instrument our function. Without instrumentation, Atheris has no way to tailor its inputs to maximize the code coverage.

Insert the following to allow Atheris to instrument it:

<pre class="file" data-filename="myFirstFuzz.py" data-target="insert" data-marker="TODO - instrumentation">
@atheris.instrument_func
</pre>

`python3 myFirstFuzz.py`{{execute}}

Ta Da! Atheris has successfully found the bug in our code. To see the input that caused the bug, check the stdout segment after `DE:` or check the crash report that was generated in the same directory.