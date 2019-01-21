from tedent import tedent as m
from tedent.invalid import (
    invalidFewerThan3Lines,
    invalidFirstOrLastLine,
    invalidSecondLine,
)


def runTests(r):
    label = "complex"
    #
    # I generally prefer to keep a 'catch all' in case combinations of units
    #   have unexpected results
    #
    actual = m(
        """
        first
          second
          third\n  fourth
        fifth

        """
    )
    expected = "first\n  second\n  third\n    fourth\nfifth"
    if actual != expected:
        r.addError(label)

    label = "empty string"
    actual = m("")
    expected = ""
    if actual != expected:
        r.addError(label)

    label = "two lines"
    actual = m("\n")
    expected = ""
    if actual != expected:
        r.addError(label)

    label = "invalid first line"
    expected = ""
    try:
        m(
            """invalid

            """
        )
        r.shouldHaveRaisedAnError(label)
    except Exception as e:
        if invalidFirstOrLastLine not in str(e):
            r.raisedUnexpectedError(label)

    label = "invalid last line"
    expected = ""
    try:
        m(
            """

            invalid"""
        )
        r.shouldHaveRaisedAnError(label)
    except Exception as e:
        if invalidFirstOrLastLine not in str(e):
            r.raisedUnexpectedError(label)

    label = "invalid less than 3 lines"
    expected = ""
    try:
        m("invalid")
        r.shouldHaveRaisedAnError(label)
    except Exception as e:
        if invalidFewerThan3Lines not in str(e):
            r.raisedUnexpectedError(label)

    label = "invalid second line"
    expected = ""
    try:
        m("\n\ninvalid\n")
        r.shouldHaveRaisedAnError(label)
    except Exception as e:
        if invalidSecondLine not in str(e):
            r.raisedUnexpectedError(label)

    return r
