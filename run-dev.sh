  #!/bin/bash
  # Create new session
  tmux new-session -d -s homestats

  # First pane - frontend
  tmux send-keys "cd host/frontend && python3 -m http.server 8001" Enter

  # Split and run backend
  tmux split-window -h
  tmux send-keys "source .venv/bin/activate && python3 -m uvicorn host.main:app --reload" Enter

  # Split and run agent
  tmux split-window -v
  tmux send-keys "source .venv/bin/activate && cd agent && python3 agent.py 10" Enter

  # Attach to session
  tmux attach-session -t homestats
