Title: Writing good software requires you to have an opinion
Date: 2016-10-03 10:20
Category: General
Tags: software
Slug: OpinatedSoftware 
Authors: Ravin Kumar
Status: published

If you want to write good software I would argue that you have to develop a
a style based on experience partially based on experience but also with a 
large dose of personal opinion. In fact I would argue go as far to argue that
if you can't develop an opinion your growth a developer will be stunted.

When you're starting to learn how to program, especially if you don't have a
mentor or aren't working in a team, you likely won't have a strong guide for code style.
But you want to learn how to write software so you just have to start
But without prior experience how do you structure your code?
If you're anything like me this means you'll
end up reading a lot of blog posts, Stack Overflow answers, and books to 
find "the best way" of doing things.

# Some languages require you to opine right off the bat
Languages like Perl [leave it up to you](https://en.wikipedia.org/wiki/There%27s_more_than_one_way_to_do_it).
There really isn't a best way of doing things, so each programmer is left
with a choice of what they think is best. But as a learner this makes
things quite difficult as you'll have to both learn to read each style
and develop your own fairly early in your learning.

# Sometimes the language has "one obvious way"
In Python there's "one obvious way" to do things. As a beginner this is great.
This means you can now google away and always find "the best way" to do things.

For example if we want to print each letter I've seen a lot of beginners 
write this.

```python
array =  ["Foo", "Bar", "Baz"
for i in range(len(array)):
    print(array[i])
```
Great it works.
But now you wan to make your code better and you want to see how the experts 
structure their code. To do so you go out and pick up two books
"Writing Idiomatic Python" and "Effective Python".

You read through and you see Item 10 in Idiomatic Python "Prefer Enumerate over Range"
and items 1.2.1 and 1.2.2 in "Writing Effective Python".

"Now I know to iterate directly over an array rather over a range and index"
you say, and quickly write what almost everyone will agree is better or
more "Pythonic".

```python
for thing in array:
    print(array)
```

In Python you can actually get really far this way, as a community there are
a ton of "almost always" best practices for doing things and the Python
language does a great job encouraging this. For me it became routine to
figure out what I needed to do, then google "best way of doing X" for a while.

# But there isn't always "one obvious way"
Let's say we have a new problem now. We now want to write a program that makes
requests to websites until it receives a 404 error. If they all work we want
a message telling us so.

Here's out first attempt using the requests library. Writing Idiomatic Python
suggests this structure saying that "even if the for structure isn't clear,
our code is clear enough to teach them"

```python
import requests
for url in ["google.com", "facebook.com", "cnn.com"]:
   reqest = requests.get(url)
   if request.status_code == 404:
      print("Request Failed")
      break
else:
   print("All good")
``` 
However if we take a look at what Effective Python suggests using this approach

```python
import requests

success = True
for url in ["google.com", "facebook.com", "cnn.com"]:
   reqest = requests.get(url)
   if request.status_code == 404:
      success = False
      print("Request Failed")

if success is True:
   print("All good")
```
but this is the exact opposite of what Idiomatic Python suggests. In fact
these two books completely disagree with each other, each saying each others
method is unreadable and harmful

# It gets worse
Once you start moving into larger projects you'll find many differing opinions.
Want a web framework? Well there's django, flask, pyramid and pecan.
Unit Testing? Pick between Nose, Nose2, pytest, unittest, and doctest.
Even for this statically generated site there's Nikola, Pelican, Hyde

Let's not even get started with Javascript.
Hell, even with simple text editors there's Atom, Sublime, vim, emacs, etc

# Why you need to develop an educated opinion fast
If you can't make an educated choice quickly you'll never get anything done,
instead switching back and forth between whatever the last person told you
was the best way to do things

# How to develop an educated opinion
Unfortunately there really isn't a way to do this other than take in the advice
from others, but then also apply them and see what works best for you. When
reading code or taking feedback pay close attention to why the person is arguing
for or against a method but think about how it fits into what you know and
what you need to get done.

# But it's worth it
Watch [this](https://www.youtube.com/watch?v=bpZS9ehw98) of Kenneth Reitz
the developer of the Requests library, which also happens to be the most
popular Python package of all time. Notice how opionated he is about the state
of other libraries and what he values in software. If Kenneth had tried
to design a library that made everyone happy, it likely wouldn't have made
anyone happy.  

# In Closing
* There rarely is one right way to do things. If you keep trying to search for one
you'll never get anything done.
* Take the time to develop your own opinion
* Do this taking the time to understand others opinions by taking in information
* But also develop your own by doing things
* You'll never get everyone to agree with your approach but that doesn't mean it's wrong


