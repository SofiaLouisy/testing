"""
Följande innebär att om denna kod körs som huvudprogram (direkt från terminalen)
så görs testet, annars inte.

Anledningen att man använder ramverk är för att om man skriver vanliga tester
så funkar det fint och allt sånt, men man måste GÖRA nått själv
(köra programmet från terminalen) för att testet ska göras

Ramverk hjälper till för att AUTOMATISERA. Tester körs, rapport fås
utan att man behöver tänka

Ramverket hittar och kör test

Unittest supports
* test automation
* sharing of setup and shutdown code for tests
* aggregation of tests into collections
* more assert-options than a regular test. self.assert
is used rather than assert so that the results can be collected

NOSE uses unittest (or anything also) and has functions for
* writing timed tests
* testing for exceptions

Other advantages of NOSE
* collects tests automatically
* supports fixtures at package, module class and test case level,
so initialization can be done as infrequently as possible
* Comes with plugin hooks for loading, watching and reporting on tests



* actively developed, 
* fairly stable and 
* has good plug-in architecture,
that lets the user extend it in convenient ways (om vi har ett 
protokoll eller nått som inte finns, så är det lätt att extenda 
nose och skriva till en sån modul)
* integrates well with distutils (vi kan installera paket in i nose. 
Distutils hjälper till att packa ner paket så de kan bli distribuerade)
* can be adapted to mimic any other unit test discovery framework
pretty easily




python kan inte köra på fler än en tråd. Det är den stora begränser

pypy är en pythonimplementation som är byggt på ett annorlunda vis,
så att det blir snabbare och mer kompatibel. Numpy för avancerade
simuleringar eller beräkningstunga grejer (numpy) så är pypy bra.
Snabbt, kompatibelt, stackless (försöker att kolla hur mycket som
behövs i kompileringen så det slipper körs dynamiskt). Men pypy
kan inte stöda alla paket som python har, (eftersom det kanske
inte kommer funkar lika bra)

Python tar inte lika mycket minne som java, men det betalar vi
i prestanda.

"""

















if __name__ == "__main__":
    unittest.main() 