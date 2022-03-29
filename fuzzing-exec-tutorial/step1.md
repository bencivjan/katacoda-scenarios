# ClusterFuzzLite Executable Tutorial - Brad Palagi, Ben Civjan

## Intending Learning Outcomes:
1. Backround on Fuzzing as a testing technique
2. Explanation on the value of implementing Fuzzing as a CI DevOps fashion
3. The ability to setup ClusterFuzzLight fuzzer on a Go project to be ran as a CI job with GitHub Actions in a git repo

## Overview of what will be accomplished throughout this tutorial:

1. Setting up ClusterFuzzLight on a Go project
2. Integrating Fuzzing into a Git respository, using GitHub Actions to perform Fuzzing as a CI job 
3. Illustrated flowchart on the overall process of this fuzzing implementation

# Background:

"Fuzzing or fuzz testing is an automated software testing technique that involves providing invalid, unexpected, or random data as inputs to a computer program. The program is then monitored for exceptions such as crashes, failing built-in code assertions, or potential memory leaks." 

To improve the effectiveness of fuzzing beyond what can be acheived through pure random testing it is common to modify existing inputs rather than generate input from scratch.

"An effective fuzzer generates semi-valid inputs that are "valid enough" so that they are not directly rejected from the parser and "invalid enough" so that they might stress corner cases and exercise interesting program behaviours." 
There are several types of fuzzers, three are black-box, white-box, and grey-box.

Black-box fuzzers are unaware of the program internals and an example would be to purely generate random inputs. The advantage to this type of fuzzer would be its ability to execute many inputs very quickly and to scale easily. Although, without leveraging program internals it is considered to be a shallow type of fuzzer which can only detect surface level bugs.

White-box fuzzers are leveraging program internals in an attempt to increase code coverage and discover deeply hidden bugs. Specific locations in the program could be targeted using this type of fuzzer, making it highly effective. Although, there is a chance where this type of fuzzer takes much longer execute each input and would lead back to a black-box fuzzer being more effective. With this in mind there are attempts to create black-box fuzzers which learn about program internals to eventually perform similarly to a white-box fuzzer, this would be to "combine the efficiency of blackbox fuzzers and the effectiveness of whitebox fuzzers"

Gray-box fuzzers use instrumentation to trace block transitions exercised by input which leads to a balance of performance as well as increased code coverage.

https://en.wikipedia.org/wiki/Fuzzing



# Value of Fuzztesting (in a CI Fasion)

Fuzz testing itself can be valuable in finding bugs which were missed by test cases created by a developer. It would be impossible to think of all edge cases on ones own. 

To identify a bug a fuzzer needs to be able to determine a faulty behaviour from a feature. A typical fuzzer will report inputs that lead to a crash, and there are other sanitizers which can detect memory related errors, race conditions, undefined behaviour, etc.

https://en.wikipedia.org/wiki/Fuzzing



https://docs.google.com/document/d/1N-12_6YBPpF9o4_Zys_E_ZQndmD06wQVAM_0y9nZUIE/edit

