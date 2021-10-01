Title: Why a Statically Generated Site
Date: 2016-7-10 
Category: Programming
Tags: Programming
Slug: WhyIChoseaSSG 
Authors: Ravin Kumar
javascripts: 
Stylesheets: 
Status: Published 


Initially when I decided to start this blog I started with what I already
had a WordPress blog. Wordpress had served me well in the past, especially
when I had a more limited programming background. Given the needs of this blog
however, a Statically Generated Site, turned out to be a better choice.


##Syntax Highlighting
Wordpress syntax highlighting was ok, but not the best. Given that there 
would be a lot of code on this blog this was a huge knock against the WordPress
environment

##Difficulty in supporting Javascript/D3
There is a plugin to support d3 in Wordpress but its docs only list
3.3, and given that 3.5 has been around for a while, and that 4.0 just got released,
it was evident that trying to embedded visualizations or javascript programs
into the blog wouldn't be straightforward

##Latex support is limited
It seems that in WordPress all Latex equations have to be rendered as images
in formats such as png or svg. While this is fine for displaying the equation
it would be a pain for any reader that is trying to copy the content of the page.
While this limitation wasn't a dealbreaker it compounded my WordPress dislike.

##Lots and lots of overhead (Mentally and Computationally)
WordPress is built on PHP and MySql and lots of HTML and CSS. It requires a 
backend to function. Even after all the setup it becomes cumbersome to modify
extensively, and to write posts I would have to go into a WebGUI and figure out
what buttons do what. When adding additional plugins to do syntax highlighting
and additional javascript it would become even more difficult to modify layouts
and figure out how to make things work

Additionally, it would be a lot more work if I moved hosting services
and always be worried about updates and security

##I already have enough to learn
Given that I'm trying to learn more about Data Science, it just made
more sense to pick a SSG using a Python based generator. 
This means I could stay in the same software stack I use for Data Science 
and continually learn about those things, rather than have to struggle with 
learning how WordPress works

Briefly listed here are the tools used to maintain this blog now 

* vim/Text Editor - All the content is written in text files  
* Python - Generates HTML from the text files  
* HTML/CSS - Layouts and styles the site  
* git - Helps maintains versions and publishes the site 

#SSGs just make sense for a DS focused blog
In summary due to the programming/stat it just made sense to work with
something that had minimal overhead of use, used the same toolsets, and 
could render all the visualizations, math, and code nicely

#Others opinions
In part I made my final choice based on the positive experiences of others
as well. Here are some links to their opinions

<http://bdadam.com/blog/why-i-chose-a-statically-generated-website.html>  
<http://duncanlock.net/blog/2013/05/17/how-i-built-this-website-using-pelican-part-1-setup/>  
<https://www.smashingmagazine.com/2015/11/modern-static-website-generators-next-big-thing/>
