# To do

[source](http://www.diveintopython.net/unit_testing/diving_in.html)

If you write unit tests, it is important to write them early, even before you write the code and
keep them updated as the code changes. This
can detect changes in the code that you did not do on purpose.

* It forces you to detail requirements in a useful fashion.
* It keeps you from overcoding.
* When refactoring code, it makes sure the new version behaves the same as the old.
* When coding in a team breaked up in assignments. Everybody takes the specs for their task, writes unit test for it and then shares it with the rest of the team. This avoids developing code that won't go well with the others.

1. Define the behaviour that you expect. List requirements
2. write a test suite that puts these functions through their paces and makes sure that they behave that way you want them to. (the test code). It includes:
    * KnownValues: expected output for a bunch of expected input
    * BadInputCheck raise "correct" exception for all possible bad inputs
    * SanityCheck, go though every single possible result. Convert front and back and retrive same as you gave
    * CaseCheck, always result uppercase