Title: Faster blogging with Tmux
Date: 2018-05-18
Category: Programming 
Tags: Programming, Tmux
Slug: TmuxBlogging
Authors: Ravin Kumar
Status: published


Writing blog articles is great, but an aspect of it that is not is getting
running all the scripts to get everything setup. To start a blogging
session in no particular order I need to  

* Traverse to my repository  
* Start an http server  
* Traverse directories again  
* Start pelican  
* Traverse directories more  
* Start vim  
* Start writing

Tmux, a terminal multiplexer, makes it easier to switch between the terminals
running these processes, but starting them manually is a pain

Luckily Tmux supports scripting which makes solving this problem really easy.

# Tmux script
The shell script below runs all the commands needed to start a blogging
environment on my computers.

```shell
# !/bin/sh
# Small script that sets up blogging environment with one command

# Kill open session
tmux kill-session -t blog || true

# Create new session
tmux new-session -d -s blog 

# C-m is carriage return in tmux
tmux send-keys 'source activate blog && pelican -r -s pelicanconf.py' 'C-m' 

# Start http server
tmux select-window -t blog:0
tmux split-window -v 
tmux send-keys 'cd .. && python -m http.server' 'C-m'

# Ready to blog
tmux new-window -n blog_article -c $PWD"/content"
tmux att -t blog
```

Breaking this apart, the first thing to do is ensure that no other tmux session
is already running all the processes I need. This is done by checking
if a session named `blog` is running and if so kills it. 

```shell
# Kill open session
tmux kill-session -t blog || true
```

The next step is creating a ession to group all the windows and panes
that will be running the processes. The first done is starting a session
named blog. Next the pelican process is started. `send-keys` was used
instead of running the command directly because in tmux if process stops
the pane would close, not a behavior that was desired. `C-m` is a carriage
return and instructs tmux to run the command after typing it in, the same
as pressing enter does when manually typing the command.

```shell
# Create new session
tmux new-session -d -s blog 

# C-m is carriage return in tmux
tmux send-keys 'source activate blog && pelican -r -s pelicanconf.py' 'C-m' 
```

With the pelican process ready to generate the site, the next step is to
start a local server to view the blog in a browser

```shell
# Start http server
tmux select-window -t blog:0
tmux split-window -v 
tmux send-keys 'cd .. && python -m http.server' 'C-m'
```

Lastly we start a new window in the directory where the markdown files 
where for this blog are stored. The final command is attaching the tmux
session to the running terminal to start writing.

```shell
# Ready to blog
tmux new-window -n blog_article -c $PWD"/content"
tmux att -t blog
```

And with that were done!

# Why go through the trouble
If the task I want to do is write a blog, every step between is a distraction
and a time waste. This script allows me to bypass all the manual steps
and jump straight into the value add work, writing content to share with you! 
