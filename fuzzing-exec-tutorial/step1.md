OSS-Fuzz is Googles open source repository for fuzzing, it includes ClusterFuzzLite as its solution for CI workflows. ClusterFuzzLite uses the Atheris package for fuzzing python.

## Intending Learning Outcomes:
1. Backround on Fuzzing as a testing technique
2. Understanding the pros and cons of implementing Fuzzing versus standard unit testing
3. The ability to integrate Google's Atheris Open Source Python fuzzer with a Python project
4. How to add fuzzing to a CI workflow with Github actions

## Overview of what will be accomplished throughout this tutorial:

1. Integrating Google's Atheris with a Python project
2. Creating a GitHub repository to host project
3. Setting up Fuzzing CI pipeline through GitHub Actions on new repo

# Background:

"Fuzzing or fuzz testing is an automated software testing technique that involves providing invalid, unexpected, or random data as inputs to a computer program. The program is then monitored for exceptions such as crashes, failing built-in code assertions, or potential memory leaks."<sup>1</sup>

The best fuzzers are ones that provide input that is on the boundary of validity. Rather than providing completely invalid inputs that would be immediately rejected by the program, a good fuzzer should provide *valid-enough* input so that a function will accept it but produce wrong or unexpected results. This results in the best testing of edge cases and can stress-test the program very well when used appropriately.

Fuzzing is an extremely useful technique when examining the security of a software program. One of the most useful areas of code to fuzz is a 'trust boundary'. A trust boundary is a section of code where the input is from an untrusted user (i.e. A form input, http request, etc.) as opposed to a trusted user (eg. config file that can only be modified by an admin). This can help to reveal any unexpected behaviors that could be triggered by a malicious user.

To improve the effectiveness of fuzzing beyond what can be acheived through pure random testing it is common to modify existing inputs rather than generate input from scratch.
