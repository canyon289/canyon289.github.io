Title: Migrating from TravisCI to Azure Pipelines
Date: 2019-06-02
Category: Programming 
Tags: 
Slug:  AzurePipelines
Authors: Ravin Kumar
Status: published



I'm in the process of testing out Azure Pipelines
with [ArviZ](https://arviz-devs.github.io/arviz/), and in
the process have learned more about the platform. I'll share
my motivation as well as some tips.

Note that this is a live blog post that I'll continue to
update as a I learn more.

# Motivation
Many Open Source projects on free tiers of services quite heavily.
TravisCI was one of those vendors which provided a free tier for 
open source but after its acquisition its future is uncertain.

At the same time Microsoft seems to be heavily investing in open
source, through acquisitions like GitHub and by open sourcing projects
like VScode.

Practically speaking Microsoft is also offering more parallel builds and longer runtime
than TravisCI. PyMC3 recently ran into TravisCI's 50 minute build limit and we had to do some hacky
stuff to get around it. Having 6 hours of build time in Azure is very convenient.

Due to these reasons we are trying both services in parallel to see which is a better
fit for ArviZ given current circumstances.

## Tips
This section is a grab bag of tips from my ramp up to Azure. I'll be
updating it as I learn more.

## Skip the main docs initially
One upside of Azure is that it's more flexible than TravisCI, but it's
also more complicated and the docs aren't great. I would advise skipping
to the [migration](https://docs.microsoft.com/en-us/azure/devops/pipelines/migrate/from-travis?view=azure-devops)
section of the docs so you can start from known ground, before working
into Azure's complexity.

I also found this blog post from [Hynek Schlawack](https://hynek.me/articles/simple-python-azure-pipelines/)
to be quite helpful.

## Read others implementations
It's a lot easier to see the functionality if you look for other people's code.
I referenced [PyJanitor's](https://github.com/ericmjl/pyjanitor/tree/dev/.azure-pipelines)
implementation as a reference for mine.

For your aid here's both our [TravisCI yaml file](https://github.com/arviz-devs/arviz/blob/master/.travis.yml)
and our [Azure Pipelines](https://github.com/arviz-devs/arviz/pull/688/files)
PR for a one to one comparison.

## Docs exist for most major languages
Specific documentation exists for common workflows in common languages.
For example this [python](https://docs.microsoft.com/en-us/azure/devops/pipelines/languages/python?view=azure-devops)
doc was particularly helpful as ArviZ is written in Python. 

## Azure Pipelines has built in code coverage and test stats
Coveralls, codecov, and other provide great free tiers for their services
but integration isn't always straightforward. In ArviZ's case Coveralls
doesn't have an "out of the box" solution for Azure Pipelines yet.

Luckily Azure Pipelines has a bunch of these services built in as tasks.
Having things in one place is convenient should mean a lesser chance 
of coverage or testing tools breaking.

## Tasks are like functions
I found the docs for tasks to be particularly confusing and it took me a while
to latch onto the central concept, so in attempt to help here's my two liner.   

*Tasks are like functions, they take inputs and then they "do a thing".
You can add tasks to your CI pipeline by copying a task block into your 
YAML file*

Here's an example of the [Code Coverage task](https://github.com/arviz-devs/arviz/blob/cb2a43d3882cbe1fd084d0a863be7bdaeb0a7ab5/azure-pipelines.yml#L85) from ArviZ in context. The official documentation
shows [some screenshots](https://docs.microsoft.com/en-us/azure/devops/pipelines/tasks/index?view=azure-devops)
, but after hours of clicking around I never found it and ended up realizing
that that WebGUI was not needed.

## What's next
We're going to trial both CI pipelines with ArviZ to see which one we should
move forward with. When we know I'll update this blog post. Happy CIing.
