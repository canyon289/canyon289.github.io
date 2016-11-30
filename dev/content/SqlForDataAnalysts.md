Title: SQL for Data Analysts
Date: 2016-11-28
Category: Programming 
Tags: Data, SQL
Slug: SqlForDataAnalysts 
Authors: Ravin Kumar
Status: published

SQL is a very extensive language but as a Data Analyst you don't have to know
all the ins and outs to start doing useful work. Here's a list of SQL concepts
and commands in a rough order of importance for Data Analysts. I'm basing this
list off of my experience using SQL to answer business questions at 
SpaceX and National Oilwell Varco. At both companies I used T-SQL/SQL Server
but the general ideas and commands are present in pretty much every flavor of
SQL.

# The Basics
If you want to produce any results you'll have to start here.

## 1.Tables
Fundamental to relational databases is the concept of tables, all the data
is stored in these. Quickly learn how business concepts are reprsented in
tables. You'll quickly find that a couple central tables usually contain an
overwhelming majority of the useful information for a business area. For instance
sales, customers, expenses, etc. Start with those and inevitably
you'll start learning the others.

## 2. Select
Select is the workhorse command that will return your results. Might seem
obvious but there are some important concepts like select, like **Select &ast**,
**Select Top** and the order in which Logical Query Processing executes a Select.
More on this later

## 3. Where
Getting a whole table isn't usually very useful. Learn the where filters
like the **like** comparison, conditional filters, and datetime filters.

## 4. Joins
This is entirely fundamental to working with SQL. Aside from just getting
the query to execute, knowing when to use and inner vs left join can totally
change the meaning of your results. Master this quickly, including less
used joins like comma or natural joins.

## 5. Aliasing
As soon as you start joining tables together, you'll likely run into
duplicate column names on keys, or columns like CreateDate. Aliasing
will ensure the query processor is actually grabbing the columns you want,
but it will also mean you can rename columns to make sense to people. Aside from
column aliasing, table aliasing will also help you keep things straight and
is required for subqueries

## 6. Subquery Syntax
Sometimes you'll need to join half the rows from one table with half the rows
on another other table. Subqueries are the simplest way to do this.

## 7. Order By
People usually care the most about the highest or lowest values of things. When
you're returning millions of results you can't really scan by eye to figure
it out. Order by does the work for you and, like it sounds, orders results

# Intermediate SQL
After getting the basics people will start asking more pointed questions like,
**What's my sales per Region?** or **What are the 2nd most expensive parts
we produce?** To answer these questions you'll need some more knowledge.

## 8a. Built in Functions
You'll need to these to do things like sum over a column, or count the number
of records, but you'll also need these to numerically rank results.

## 8b. Groupby and Partition By
At the same time you'll need to learn how to use aggregations to use the functions
above. Usually people ask questions like what's the cost per part, or what's the
sales per region. A quick groupby and sum will answer these questions in a jiffy.
Partition by is another way to do aggregations that doesn't require subqueries
if you're only aggregating one column out of many. 

## 9. Having
Where filters rows, having filters groups. Better explained with examples
that can be [found here](http://www.w3schools.com/sql/sql_having.asp)

## 10. Cross Apply and Outer Apply
Cross Apply and Outer Apply are advanced joins that let you use information
from one table into another in a more advanced way than traditional joins.
For instance one example is being able to use join on table valued functions
that results. Another is to use information from one table as a filter condition
in a subquery that's generating another table that you're joining on. You'll
quickly find out when you need these when you realize you can't accomplish certain
joins with just left and inner joins.

## Advanced SQL
## 11. Variables
Variables will you reuse values throughout your code and make certain things
more obvious. For instance if you're filtering for records after a certain date
sometimes you could put the dates directly in the where line, but after a while
it can become cumbersome to find it in your code. Declaring a variable at the
top with your date, and using the variable later in your code helps you
quickly modify your code and others. It especially helps when you reuse
the date multiple times, declaring it once as a variable means you only
need to edit it one place.

## 12. While Loops 
With variables you can effectively use while loops. Variables and while loops
will be necessary to traverse databases that are representations of graph structures.
For example getting a reporting chain, to see who's boss, is who's boss, is who's boss.
Or getting all parts that are a part of a Bill of Material. Or tracing transactions
over time for a certain serial number part.

## 13. Common Table Expressions 
Common table expressions are a useful way to annotate your code, they're
somewhat analagous to object oriented programming where you can slowly
build a results set over a more easily readable series of operations. You'll
see what I mean when your queries starts with select, has 20 columns from
various tables, and then 15 joins to get all the columns together. It gets
a bit hard to keep it all straight. 

## 14. Recursive Common Table Expressions
However a big reason to learn Common Table Expressions is to take advantage
of recursive common table expressions. These serve a similar function
to while loops, but are a slightly different flavor and in my opinion are
a better syntax. Use this often to perform recursion on data concepts 
that require it.

# Generating your own tables
Once your queries start getting complex it'll help to store results
in intermediate tables. To manage these you'll need to get familar with commands
such as 

## 15. Select * into #(table_name(
The easiest way to create a temp table, just select some values and 
tell SQL Server to automagically create a table from the results.

## 16. Create Table
While Select into is great, as you progress you'll sometimes need to
have more control over the data types and other details like indexes in your 
temp table. To do so you'll have to start with Create Table, which then allows
you to specify all of these details. 

## 17. Insert Values into
An empty table is fairly useless though. **Insert Values into** will
help you populate your newly created table quickly.

## 18. Drop Table
And sometimes you'll need to get rid of tables you created. Just be careful
because it's way easier to drop tables than create them.

# The Other Stuff
There's additional concepts like modifying rows, altering columns,
stored procedures, and functions, but those start getting into the realm
of Database Administration, and sides by the time you get here anyway
you'll be strong enough with SQL to figure out what you need.

# Getting started
Don't let this list intimidate you, you can get a lot of value from just
the top 5 items. The others will come naturally as you figure out you need them
and hopefully this list will help you figure out the terms to google once
you get there.
