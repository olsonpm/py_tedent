from tedent import tedent as m


def runTests(r):
    label = "no indentation"
    actual = m(
        """
        first
        second
        """
    )
    expected = "first\nsecond"
    if actual != expected:
        r.addError(label)

    label = "second line indented beyond anchor"
    actual = m(
        """
        first
            second
        """
    )
    expected = "first\n    second"
    if actual != expected:
        r.addError(label)

    label = "second line indented behind anchor"
    actual = m(
        """
        first
    second
        """
    )
    expected = "first\n    second"
    if actual != expected:
        r.addError(label)

    label = "trailing empty line removed"
    actual = m(
        """
        first\n    second

        """
    )
    expected = "first\n    second"
    if actual != expected:
        r.addError(label)

    label = "trailing space in last line removed"
    actual = m(
        f"""
        first\n    second{" "}{" "}
        """
    )
    expected = "first\n    second"
    if actual != expected:
        r.addError(label)

    label = "indent affects subsequent lines"
    # indent is relative to prior line
    actual = m(
        f"""
        first
          second\n  third\n    fourth
        """
    )
    expected = "first\n  second\n    third\n      fourth"
    if actual != expected:
        r.addError(label)

    label = (
        "only indent subsequent lines with less leading space than the anchor"
    )
    actual = m(
        f"""
        first
          second
          third\n  fourth
        """
    )
    expected = "first\n  second\n  third\n    fourth"
    if actual != expected:
        r.addError(label)

    return r
