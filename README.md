# Simple Product Catalog Client and Server

This is a simple product catalog client and server implemented in python.  It is so simple as to be trivial: no one would ever use this code.  I created this as I experimented with pipenv and the typing and unittest modules while using Visual Studio Code.

## unittest?

The unittest module has two features that I dislike: "test cases" are implemented as subclasses and the parent class has camel case method names.  However, my second attempt to wrap my head around pytest was no more successful than the first.  On a large project, I'd invest the time to understand it, but since I use python for smaller projects, I've stayed with the easy to learn and use unittest.

## typing

I have used type hints before.  They have alerted me to bugs without running code.  Great.  There are still two consequences that annoy me.  First is readability.  When types are simple, code still looks clean.  When I need unions or sequences of mappings, the hints start taking over visually.  The code is harder to read and understand, at least to me.  Second is maintenance.  When I add another alternative to a union, that creates a cascade of necessary updates.  It's a lot like maintaining unit tests, which I hate but willingly do because I get so much value from the unit tests.  I'm not convinced that I get enough value from type hints to warrant the maintenance.  Maybe if I used PyCharm instead of VS Code I would be able to use a re-factoring to do the cascading changes.

## pipenv

I've used virtualenv, conda and venv.  They all work just fine.  However, I often forget the subtle differences between them and, for that matter, which of my projects use which.  I wanted to standardize on venv to minimize third party dependencies.  Before I did that, I decided to try pipenv, which I've liked so far.  It feels a little like npm, which is nice, and allows me to forget about the virtual environment altogether if I want.
