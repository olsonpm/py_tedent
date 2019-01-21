from case_conversion import separate_words
from tedent.fns import forEach, invokeAttr
from . import rest, simple
from .Results import Results
from .utils import getModuleBasename

modules = [simple, rest]


def runTests():
    resultsList = []
    for m in modules:
        moduleName = separate_words(getModuleBasename(m))
        r = Results(moduleName, level=0)
        results = m.runTests(r)
        resultsList.append(results)

    forEach(invokeAttr("printResults"))(resultsList)


__all__ = ["runTests"]
