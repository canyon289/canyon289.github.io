Title: You should learn SQL
Date: 2016-10-22
Category: Data Science
Tags: SQL
Slug:  LearnSQL
Authors: Ravin Kumar
Status: Published

I'm not the first to say this and I really doubt
I'll be the last. Being able to use and understand data is 
becoming, if not already, a very powerful skill. Let me
go through the two perspectives I've encountered below.

# But I'm already learning Python/Pandas/R
Cool! So you're already interested and well on your way to being
a data professional. Then there's two reasons you should learn
SQL.  

## You'll become the data girl/guy faster
If you're trying to break into an analytical role your employer
will be much more supportive, and likely even pay you, if you
can show results. I would argue that SQL is the much quicker
route to get a data role and start gaining experience for
the following reasons.

### Declarative vs Imperative Languages
Without going deeply into the nuances between declarative
and imperative languages what's easier to write and understand?

```python
import pandas as pd
df = pd.read_csv("http: iris url") # This is dependent on your data source
df.head()
```

```SQL
SELECT TOP 5 * FROM IRIS
```
With Python you'll have know how to import pandas, call
the correct method to read a csv file, know what argument
to pass to the read_csv method, know about variables, and then
know you can call a method on that assignment. A lot of the symbols
are not "English" intuitive either. 

```SQL
SELECT TOP 5 * FROM IRIS
```
Comparatively, SQL is much more approachable and basically reads straight across.
Now yes SQL has its own set of complexities and limitations but just starting
out it's been my experience that there's much less you need to learn
before you're able to do useful things. But.... 

### It's probably already setup for you
I don't have strong evidence to back this claim I would argue nearly all
businesses have a need to store data in tabular format and already do. This
means you just need to start querying it, without having to worry about setting
up a local Python or R environment, especially when most companies lock
down admin privileges anyway and make this sometimes difficult to do.

### Since it's setup there's a resident Database Admin
If the assumption above holds there already will be at least one person
whose job it is to maintain that database who knows SQL. I would argue
there's more companies that pay a DBA than companies that are hiring data scientists.
In my experience nearly all companies have data these days, not nearly as many
have Python/R stack data scientists on staff.

### SQL has a standard
SQL is more standardized than other data languages.
While there are differences the basic queries are pretty much the same
across platforms. The switching cost between Python and R is much higher.
This makes it easier to learn and use in a variety of settings, even if not 
every place you go uses the same database and SQL variant.

### You're going to have to learn it anyway
Even if you end up using Pandas or R you'll have to find some data. While it's 
true a lot of data is not in database, a lot of data is in a database.

## But I'm a manager
Even if you have direct reports that can write SQL, knowing a bit of SQL will
help you become much more literate. Some of the managers who I've worked with
have been able to use data to great effect to paint a story both to their 
direct reports and in discussions with their peers and superiors. It's harder
to argue with the results from a query.

# In Conclusion
If you're relatively new to data it's my opinion that learning SQL gives you
the most "bang for your buck". It has a relatively low barrier to entry
given that most companies already use it, and it's simpler to start out with
and get useful results. And once your employer sees some results it'll be easier
to sneak some Python/R and fancier stuff in as well!
