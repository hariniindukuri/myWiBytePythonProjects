#!/bin/bash

# Poll internal VNC (5901) and web desktop (6080) sockets
until (echo > /dev/tcp/127.0.0.1/5901) 2>/dev/null && (echo > /dev/tcp/127.0.0.1/6080) 2>/dev/null; do
  sleep 1
done

# Wipe command clutter and display clean ready message
clear
echo -e "\n\033[1;32m For Turtle/Tkinter, wait for port 6080 (See Ports tab) -- may take a few seconds -- and then run the project.\033[0m\n"
