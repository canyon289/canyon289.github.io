# !/bin/sh
# Small script that sets up blogging environment with one command

# Kill open session
tmux kill-session -t blog || true

# Create new session
tmux new-session -d -s blog 

# C-m is carriage return in tmux
tmux send-keys 'conda activate blog && pelican -r -s pelicanconf.py' 'C-m' 

# Start http server
tmux select-window -t blog:0
tmux split-window -v 
tmux send-keys 'cd ../docs && python -m http.server' 'C-m'

# Ready to blog
tmux new-window -n blog_article -c $PWD"/content"
tmux att -t blog
