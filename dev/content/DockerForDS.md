Title: Better Data Science CI with Docker
Date: 2019-01-09
Category: Programming, MachineLearning
Tags: 
Slug: DockerforDS
Authors: Ravin Kumar
Status: Published


Know the feeling when you use a tool that "just works" and instead of
frustration and time list, you end up being more productive?  

ArviZ should be for Bayesian practitioners. 
Bayesian practitioners should be able to use their inference library of choice,
and be able to visualize their results, with no pain and no time taken away
from the real work, interpreting results.

In turn the ArviZ Devs had the same expectations for Continuous Integration pipeline
It should "just work", so we can focus on writing new functionality for users ,
not waste time feeling frustrated with our flaky infrastructure.

But this was not the case, our Continuous Integration (CI) experience **was**,
frustrating, not just for us, but especially for volunteer contributors
that were submitting great code, only to have the CI process abort with
an obscure failure message. At ArviZ we need our CI process to be smooth,
partly because we want the code to be tested and verified, but moreso 
to avoid wasting contributors time, and ensure they have a great experience.
After all, the most finite resource is people's willpower, time, and enthusiasm.

In other words
![Arviz Developer Experience]({static}/images/DockerForDataScience/MarieKondo.png)

To keep developers joyful we've moved to a docker based
Continuous Integration system. In this post I'll 
the issues we were having with CI, why we started
using Docker in our CI, general instructions on how it all works,
and a grab bag of tips.


## The tale of 5 deep learning frameworks, a local machine, and a remote virtual machine
Installing one deep learning framework can be a challenging experience,
installing five at the same time can be perilous. To ensure
ArviZ runs seamlessly on widely used Bayesian learning libraries, we 
need to test against all of them, which means we need to install all of them.

In the event of issues, debugging locally is painful enough, but when
an error appears in the CI process, the developer has little access
to see what went wrong. Debugging amounts to lots of print statements, git commits
and waiting 15 minutes to see what happens. It's especially maddening
when local testing passes, but only the CI virtual machine is failing.

This is the situation we were facing with plain TravisCI. Code that worked
great locally, suddenly was failing when contributors made pull requests. This is
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
2. Configure Continuous Integration service to build and test in your defined container
3. Fix any integrations that may have broken

Let's talk through each step one by one

### Step 1: Dockerfile
The first step is deciding what you want your environment to contain. In
general you'll want your container to have all the tools needed to build
and test your code, and ideally be as minimal as possible. We'll use the
[ArviZ dockerfile](https://github.com/arviz-devs/arviz/blob/master/scripts/Dockerfile)
as an example.

The first line is the base image.

```
FROM conda/miniconda3
```
While it's typically recommended to start with a minimal image, like
alpine, at ArviZ we found it much simpler to start with an environment
that already had some things setup, and just work from there. This meant
the image isn't as minimal as it could be, but we're not shipping containers
"at scale" so this tradeoff was worth it.  


Next we setup arguments and environmental variables
```
ARG SRC_DIR
ARG PYTHON_VERSION
ARG PYSTAN_VERSION
ARG PYRO_VERSION

ENV PYTHON_VERSION=${PYTHON_VERSION}
ENV PYSTAN_VERSION=${PYSTAN_VERSION}
ENV PYRO_VERSION=${PYRO_VERSION}
ENV DOCKER_BUILD=true

# For Sphinx documentation builds
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
```
The choices here were to allow some flexibility in what gets installed
in each image. For ArviZ we test against different versions of libraries
and we didn't want to create a dockerfile for each. By setting the 
ENV variables here through command line arguments we afford some flexibility


After this we actually start installing things

```
RUN apt-get update && apt-get install -y git build-essential pandoc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and environment installation scripts
COPY $SRC_DIR/requirements.txt  opt/arviz/
COPY $SRC_DIR/requirements-dev.txt  opt/arviz/
COPY $SRC_DIR/scripts/ opt/arviz/scripts

WORKDIR /opt/arviz

# Create conda environment. Defaults to Python 3.6
RUN ./scripts/create_testenv.sh
```
Installations happen at two levels, some are at the container level,
and the rest are in the Python environment. We choose to have a separate
`create_testenv.sh` script because this allows users to run it outside
of docker.

The ext section of the file copies the ArviZ code base and
removes any cached files/
```
COPY $SRC_DIR /opt/arviz
```

The last section clears any remaining cache files and sets the default
command of the container to execute tests. There is some weirdness
with the `source /root/.bashrc` which I'll talk more about in
the general tips section.

```
RUN rm -f arviz/tests/saved_models/*.pkl
RUN find -type d -name __pycache__ -exec rm -rf {} +

CMD ["/bin/bash", "-c", "source /root/.bashrc && pytest -vv arviz/tests --cov=arviz/ && echo Finished Testing"]
```


### Step 2: Configure your CI service

The next step is configuring TravisCI. Luckily this is not too hard.
Adding the lines below will install the latest version of docker-ce


```
addons:
  apt:
    packages:
      - docker-ce
```

After that you're able to build an image and run tests, coverage,
documentation generation, or whatever else you'd need.

### Step 3: Fix any integrations that may have broken
One downside of testing in a container is that isolation is great,
until it isn't. We found that some of the tooling that integrates with
TravisCI, such as travis-sphinx, and coveralls, no longer worked.

The trick here was to generate the documentation and coverage files in
the container, but ensure they were available in the TravisCI environment
by using a bind mount. An example can be found in 
[the .travis.yml file](https://github.com/arviz-devs/arviz/blob/6d1b65e0c99bb716ee0ebcbdac8cdc9e1380a472/.travis.yml#L68-L69).

Because the files were present in TravisCI file system, the integrated tools
could then deploy the docs and coverage just as they had in the pa.

Because the files were present in TravisCI file system, the integrated tools
could then deploy the docs and coverage just as they had in the past.

## Miscellaneous tips
There were some gotchas that required some experimentation which I'll document here.

### Formatting in TravisCI yml files
TravisCI is picky about semicolons, spaces, and newlines in its .travis.yml file.
If you're running into odd errors be sure to troubleshoot these first.

### Bash profiles in Non interactive shells
Not all bash shells are interactive, and 
[when they're not they don't invoke](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html)
a `.bashrc` file. This is why you see `source /root/.bashrc` frequently 
in our `.travis.yml` files. This commands loads the `.bashrc. file  before
executing the next command.
While this workaround isn't the most elegant
it did work for our purposes. However if you know of a better solution
please let us know with an issue or a pull request! We would greatly appreciate it.

