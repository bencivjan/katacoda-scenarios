# Types of Fuzzers / More Details

There are several types of fuzzers, three are black-box, white-box, and grey-box.

Black-box fuzzers are unaware of the program internals and an example would be to purely generate random inputs. The advantage to this type of fuzzer would be its ability to execute many inputs very quickly and to scale easily. Although, without leveraging program internals it is considered to be a shallow type of fuzzer which can only detect surface level bugs.

White-box fuzzers are leveraging program internals in an attempt to increase code coverage and discover deeply hidden bugs. Specific locations in the program could be targeted using this type of fuzzer, making it highly effective. Although, there is a chance where this type of fuzzer takes much longer execute each input and would lead back to a black-box fuzzer being more effective. With this in mind there are attempts to create black-box fuzzers which learn about program internals to eventually perform similarly to a white-box fuzzer, this would be to "combine the efficiency of blackbox fuzzers and the effectiveness of whitebox fuzzers"

Gray-box fuzzers use instrumentation to trace block transitions exercised by input which leads to a balance of performance as well as increased code coverage.
