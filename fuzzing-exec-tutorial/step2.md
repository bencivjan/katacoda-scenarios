# Pros and Cons of Fuzzing<sup>4<sup>

|Advantages of fuzzing|Disadvantages of fuzzing|
|---------------------|------------------------|
|Fuzzing is extremely efficient. Once a fuzzer is set up and running, it can work without any intervention for days or even months to identify bugs in an automated way. It can significantly reduce manual efforts.|Fuzzing is time consuming. Fuzz testing may take a long time to yield effective results.|
|Fuzzing helps to Identify high severity bugs. Fuzzing often helps find the most severe bugs that hackers can exploit, including memory leaks, crashes, and unhandled exceptions.|Fuzzing is ineffective against malware. Fuzzing focuses on the threats which may cause a program to crash or error. However, it’s ineffective against threats like Trojans, Viruses, and other Malware.|
|Fuzzing reveals bugs missed in manual review. Fuzzing often reveals bugs missed in a manual audit and the bugs missed by other testing methods due to the limitation of time and resources.|Testers need to still invest in other testing methods. Fuzzing is best used in conjunction with other testing methods like Black Box Testing, Manual Testing, etc.|
|Reveals a high-level picture. Fuzzing provides an overall view of the robustness of the application tested.|Result Interpretation is difficult. Fuzzers typically provide high-level information which describes the issue and usually does not provide a clear path to remediation.|
|Zero False Positives. Fuzzing does not produce any false positives. If the Fuzzer found an error, it’s a problem that needs to be addressed.|Can be misused by malware developer|
|Fuzzing is scalable. Several tools can test the application simultaneously, which makes Fuzzing highly scalable.|Programs with complex inputs can require much more work to produce a smart enough fuzzer to get sufficient code coverage|

