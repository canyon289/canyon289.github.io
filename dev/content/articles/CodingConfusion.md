Title: Coding Confusion
Date: 2018-03-12
Category: Programming
Category: Visualization
Tags: Visualization
Tags: Programming
Slug: CodingConfusion
Authors: Ravin Kumar
Status: Published 


Recently I've been teaching more coding than ever, both to coworkers and
to students in my bootcamp. While they're all catching on and getting
results, its made me step back and realize, modern day programming is not
straightforward and with all the various parts, often is just plain confusing.

# Your first program
Python is a popular programming language so it feels simple enough to tell a 
new programmer, "Hey open up a text editor and write the following commands"

```python
print("Hello World")
```
At this point the you feel accomplished, the student feels accomplished, 
but then it quickly wears off as both of you realize this program doesn't
do anything useful. So you start trying to explain the next steps, but where
do you start?

# Your first productionized program
There's data types in Python, such as lists, dictionaries, etc. There's also
the concept of iteration and control loops. But DRY is a thing so you 
quickly have to explain functions, but then you get into scope, and with
Python there's whitespace formatting to cover as well. 

Somewhere in there you fit in a lesson about shell commands, and depending
on whether they're in Windows or a POSIX client you wave your hands about
OS file systems.

All the code shouldn't be in one file though or it's confusing, so then you explain
Python import machinery, but modules have their own nuances. Somewhere
in there you ramble on about functional design vs OOP.

Well now the student has something more complex working and they're thrilled
but they want to deploy it. So now you need to teach them about git, but
its also important that they know about isolated environments through
virtualenv, or conda. A conversation ensues about dependencies and why
pinning versions for imported packages might be necessary.

After all this they finally get their code packaged up and put into a repo.
Their code works and is available  but man it's ugly so you start explaining
the importance of code quality, and how PEP8 is a thing, and why spaces after
single line comments and camel casing are oh so important. A linting
package is installed a bunch of messages appear on the console
after you show they how to run it.

They didn't know about unit testing though so you go through a lecture on
Test Driven Development. Their monolithic logic needs to be refactored.

And now their code needs to be deployed, so you ask them hard questions
of how it will be used. If it's going to be a local package did they make
sure it worked across all operating systems and python versions?

They instead want a webapp, which eliminates most of the issues above, sweet!
You ask them which web framework they want to use but now they need to learn
about WSGIs and API design. An explanation about networking and HTTP response
codes fits in there as well.

Don't forget the front end though, where they now jump into HTML/CSS/Javascript.
You explain that while most of the concepts above are still relevant, they're
ever so different in another language. And let's hope they don't need a backend
or you'll spend the rest of the day explaining what an ORM is but only
after you teach them bare SQL so they know what's going on under the hood.

Then you need to talk about Continuous Integration and explain various
deployment strategies from Virtual Machines to Docker Containers to self hosting
versus cloud hosting.

And if they're doing machine learning be sure to cover at least a semester's
worth of statistics.

# The Point
Going from starter code to production is a lot of steps and for people
that are new to programming it can be very frustrating because the code seemed
to work 10 steps ago. If you're a seasoned
programmer take a second to step back and realize how many moving parts
there are to deploying a "maintainable production ready" app/library,
and how to someone new it can be very difficult to
see the forest for the trees! There's a lot of steps and concepts between Hello World
and a robust library or application. When teaching someone new just take a breath
and remember what it took you to gain that understanding as you guide your
junior programmer. They will appreciate the help.

