Title: State Space Model Book Club
Date: 2022-12-26
Category: Data Science
Tags: Community
Slug: ssm-book-club
Authors: Ravin Kumar
Status: Published

Our [causal inference book club]({filename}BookClub2022.md) was a success.
Over 300 people took part and every session was well attended
So we're going to do this again.
This time we'll focus State Space Models, and specifically on Dynamax
a new library that makes these simple to use in a modern data stack.


<img src="https://raw.githubusercontent.com/probml/dynamax/main/logo/logo.gif" alt="Dynmax" style="width:400px"> 

Just like our causal inference bookclub.
Live sessions will get posted to my [Youtube Channel](https://www.youtube.com/channel/UCX78cJQ_6JZVUWw8cj-f0uA/featured)
and community discussions will occur on the [Intuitive Bayes Discourse](https://community.intuitivebayes.com/).
If you're already convinced you can sign up for the mailing list here.
Updates will be sent shortly after the new year.

<!-- MailerLite State Space Model Book Club -->
<div class="ml-form-embed"
  data-account="3479153:h8h4b4n7u8"
  data-form="5842164:w6l8b2">
</div>


Otherwise, read on for why we picked this topic 
and the details of this next phase of our book club.

## A focus on explainable data and models
Informing big multimillion dollar decisions the is core of my work.
This is different from making millions of small predictions.
Due to this explainable structured inference is more useful to me than tuning black box models across SpaceX, Sweetgreen, and now Google

In our last book club we studied Causal Inference, a field that explains the effect of large decisions, such as government drug policy changes using carefully structured analyses and models.
We're going to continue with that theme by studying state space models.

## State Space Models

<img src="https://probml.github.io/dynamax/_images/LDS-UZY.png" alt="State Space Diagram" style="width:200px"> 
State space models are a flexible model architecture with a wide variety of use cases.
They were used for the moon landing in the 1960s, and they're the same models used to launch rockets at SpaceX!
Besides orbital dynamics they have applications across forecasting, inference, biology, mechanical engineering.
They also can be used for causal inference.
Recent computational developments have also made them more interesting
which brings me to my next point.

## Dynamax, Jax, and new texts on Probabilistic Machine Learning
<img src="https://probml.github.io/pml-book/cover1.jpg" alt="State Space Diagram" style="width:200px"> 

Dynamax is a library for probabilistic state space models that has recently been released.
The library is based on JAX which is another great tool to learn in the statistics space.
And Kevin Murphy has released his [new books](https://probml.github.io/pml-book/book1.html) which complement the library, 
and he also is one of the authors of Dynamax.
With so many learning resources and practical tools between
Dynamax, JAX, and newly released textbooks this was an easy choice!

## State Space Book Club Structure
We're going to stretch the meaning of book to mean Jupyter notebooks. 
Our primary material of study will be the notebooks in the [Dynamax documentation](https://probml.github.io/dynamax/).
Our focus will be on learning the examples and models implemented there thoroughly,
such as Hidden Markov Models, Linear Gaussian, Non-Linear Gaussian, and Generalized Gaussian State space models.
We'll use many secondary references such as Kevin's book and others.
At the end we'll understand the theory of State Space Models and how to use them in practice with Dynamax.


## How to join
This book club will follow the same structure as the previous one.
Every couple of weeks we'll work through a block of material together.
Synchronous session will happen over livestream, to get both a live community discussion and also ensured sessions are recorded for folks to watch later.
We'll use the [Intuitive Bayes discourse](https://community.intuitivebayes.com) for asynchronous discussions 


We will be starting this book club in late January after our [final causal inference session](https://community.intuitivebayes.com/t/interview-with-scott-on-jan-15th-post-your-questions-here/647/2).


Subscribing to the mailing list will get you an invite link
to the Discourse and ensure you get all future updates.

<!-- MailerLite Universal -->
<!-- MailerLite Universal -->
<script>
(function(m,a,i,l,e,r){ m['MailerLiteObject']=e;function f(){
var c={ a:arguments,q:[]};var r=this.push(c);return "number"!=typeof r?r:f.bind(c.q);}
f.q=f.q||[];m[e]=m[e]||f.bind(f.q);m[e].q=m[e].q||f.q;r=a.createElement(i);
var _=a.getElementsByTagName(i)[0];r.async=1;r.src=l+'?v'+(~~(new Date().getTime()/1000000));
_.parentNode.insertBefore(r,_);})(window, document, 'script', 'https://static.mailerlite.com/js/universal.js', 'ml');

var ml_account = ml('accounts', '3479153', 'h8h4b4n7u8', 'load');
</script>
<!-- End MailerLite Universal -->

<!-- End MailerLite Universal -->
