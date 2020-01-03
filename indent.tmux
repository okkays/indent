#!/usr/bin/env bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
##tmux bind-key -Tcopy-mode-vi 'S' send -X copy-pipe-and-cancel "$CURRENT_DIR/indent.py | tmux load-buffer -b indented - \; display-message 'hi'"

tmux bind -Tcopy-mode-vi 'S' send-keys -X copy-pipe-and-cancel "$CURRENT_DIR/indent.py | tmux load-buffer -bindent -; tmux wait -S indent" \\\; wait indent \\\; show-buffer -bindent
