# Important Definitions<sup>3</sup>

**Bot**
A machine which runs ClusterFuzz tasks.

**Corpus**
A set of inputs for a fuzz target. In most contexts, it refers to a set of minimal test inputs that generate maximal code coverage.

**Corpus pruning**
A task which takes a corpus and removes unnecessary inputs while maintaining the same code coverage.

**Crash state**
A signature that we generate from the crash stacktrace for deduplication purposes.

**Crash type**
The type of a crash. ClusterFuzz uses this to determine the severity.

**Instrumentation**
Definitions here

For security vulnerabilities this may be (but not limited to):
- Bad-cast
- Heap-buffer-overflow
- Heap-double-free
- Heap-use-after-free
- Stack-buffer-overflow
- Stack-use-after-return
- Use-after-poison

Other crash types include:
- Null-dereference
- Timeout
- Out-of-memory
- Stack-overflow
- ASSERT

**Fuzz target**
A function or program that accepts an array of bytes and does something interesting with these bytes using the API under test.

**Fuzzer**
A program which generates/mutates inputs of a certain format for testing a target program.

**Fuzzing engine**
A tool used for performing coverage guided fuzzing. The fuzzing engine typically mutates inputs, gets coverage information, and adds inputs to the corpus based on new coverage information.

**Sanitizer**
A dynamic testing tool that uses compile-time instrumentation to detect bugs during program execution. Examples:
- ASan (aka AddressSanitizer)
- LSan (aka LeakSanitizer)
- MSan (aka MemorySanitizer)
- UBSan (aka UndefinedBehaviorSanitizer)
- TSan (aka ThreadSanitizer)

Sanitizers are best supported by the Clang compiler. ASan, or AddressSanitizer, is usually the most important sanitizer as it reveals the most memory corruption bugs.

**Testcase**
An input for the target program that causes a crash or bug. On a testcase details page, you can download a “Minimized Testcase” or “Unminimized Testcase”, these refer to the input that needs to be passed to the target program.

https://google.github.io/clusterfuzz/reference/glossary/