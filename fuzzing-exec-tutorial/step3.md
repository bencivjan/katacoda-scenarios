# Important Definitions<sup>3</sup>

**Bot**
A machine which runs ClusterFuzz tasks.

**Corpus**
A set of inputs for a fuzz target. In most contexts, it refers to a set of minimal test inputs that generate maximal code coverage.

**Corpus pruning**
A task which takes a corpus and removes unnecessary inputs while maintaining the same code coverage.

**Crash state**
A signature that we generate from the crash stacktrace for deduplication purposes.