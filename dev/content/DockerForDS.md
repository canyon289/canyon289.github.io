Title: Better Data Science CI with Docker
Date: 2019-01-09
Category: Programming, MachineLearning
Tags: 
Slug: DockerforDS
Authors: Ravin Kumar
Status: Draft


Know the feeling when you use a tool that "just works" and instead of
frustration and time list, you end up being more productive?  

ArviZ should be for Bayesian practioners. 
Bayesian practioners should be able to use their inference library of choice,
and be able to visualize their results, with no pain and no time taken awayi
from the the real work, interpreting results.

In turn the Arviz Devs had the same expecations for Continous Integration pipeline
It should "just work", so we can focus on writing new functionality for users ,
not waste time feeling frustrated with our flaky infrastructure.

But this was not the case, our Continous Integration (CI) experience **was**,
frustrating, not just for us, but especially for volunteer contributors
that were submitting great code, only to have the CI process abort with
an obscure failure message. At ArviZ we need our CI process to be smooth,
partly because we want the code to be tested and verified, but moreso 
to avoid wasting contributors time, and ensure they have a great experience.
After all, the most finite resource is people's willpower, time, and enthusiasm.

In other words
![Arviz Develop Experience]({static}/images/DockerForDataScience/MarieKondo.png)

To keep developers joyful we've moved to a docker based
Continous Integration (CI) system. In this post I'll 
the issues we were having with CI, why we started
using Docker in our CI, general instructions on how it all works,
and a grab bag of tips.


## The tale of 5 deep learning frameworks, a local machine, and a remote virtual machine
Installing one deep learning framework can be a challenging experience,
installing five at the same time can be perilous. To ensure
ArviZ runs seamlesly on widely used Bayesian learning libraries, we 
need to test against all of them, which means we need to install all of them.

In the event of issues, debugging locally is painful enough, but when
an error appears in the CI process, the developer has little access
to see what went wrong. Debugging amounts to lots of print statements, git commits
and waiting 15 minutes to see what happens. It's especially maddening
when local testing passes, but only the CI virtual machine is failing.

This is the situation we were facing with plain TravisCI. Code that worked
great locally, suddenly was failing when contributors made PRs. This is
no way was TravisCI's fault, TravisCI is a great tool that we're still using,
but it was a fault somewhere between the operation system, the five 
C level libraries, and ArviZ.

After a couple months of this we switched to docker based testing on 
TravisCI for one simple reason, **the developers local environment would
be an exact replica of the CI environment.** This meant that any CI
issue was now locally reproducible, and locally solvable.

## Docker CI Details
Alright, enough with the talk, on with the details, how is it done?

1. Create a Dockerfile for your CI environment
2. Configure Continous Integration service to build and test in your defined container
3. Fix any integrations that may have broken


### Step 1: Dockerfile

### Step 2: Configure your CI service

### Step 3: Fix any integrations that may have broken

## Miscellaneous tips
