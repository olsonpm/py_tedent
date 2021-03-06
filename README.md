# Tedent

Keep your multi-line templated strings lookin' good :sunglasses:

*This is a python version of [tedent](https://github.com/olsonpm/tedent)*

<br>

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [What is it?](#what-is-it)
- [What does the name stand for?](#what-does-the-name-stand-for)
- [Why create it?](#why-create-it)
- [Simple Usage](#simple-usage)
- [Questions about how the indentation works?](#questions-about-how-the-indentation-works)
- [Important Usage Notes](#important-usage-notes)
  - [input requirements](#edge-cases-and-input-requirements)
- [Test](#test)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

<br>

### What is it?

- A function similar to [dedent](https://docs.python.org/3.7/library/textwrap.html#textwrap.dedent)
  just with different semantics

<br>

### What does the name stand for?

- `Te`mplate string
- in`dent`ation

names are hard

<br>

### Why create it?

- dedent didn't handle the following case like I wanted

```py
formattedBoroughs = f"""\
[
    'Brooklyn',
    'Manhattan',
]
"""

print(
    dedent(
        f"""\
        New York boroughs
        ${formattedBoroughs}
        """
    )
)

#
# expected:
# New York boroughs
# [
#     'Brooklyn',
#     'Manhattan',
# ]
#
# actual:
#         New York boroughs
#         [
#     'Brooklyn',
#     'Manhattan',
# ]
#
```

<br>

### Simple Usage

```py
import tedent from 'tedent'

#
# *note the lack of the backslash
#
print(
    tedent(
        """
        This will be indented
          as you expect
        """
    )
)

# writes:
# This will be indented
#   as you expect
```

<br>

### Questions about how the indentation works?

Because the indentation logic is both young and convoluted, please refer to
[the code](tedent/index.py) and [tests](tests/simple.py) for details. The
library is not that big and if you have any questions please create a
github issue.

<br>

### Important Usage Notes

- First of all, this library doesn't handle tabs. I will accept a PR
  with support

- Secondly, if you always use `tedent` like the following

  ```py
  tedent(
      """
      some text
      """
  )
  ```

  then you shouldn't run into any issues. However we all know input can be
  tricky so `tedent` has a few input requirements in order to format your
  string properly.

#### input requirements

- if the argument isn't a string then an error will be thrown
- if you pass a string with three or more newlines, then
  - the first and last lines must contain only whitespace
  - the second line must contain a non-whitespace character
  - _an error will be thrown if the above two conditions are not met_
- if you pass a string with fewer than 3 newlines
  - if they only contain whitespace then an empty string is returned
  - otherwise an error is thrown
- finally, all trailing whitespace from the result is stripped

If you have questions please raise a github issue.

<br>

### Test

```py
#
# you must have poetry installed
#
$ poetry shell
$ poetry install
$ python runTests.py
```
