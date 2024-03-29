#!/bin/bash

# Generate a random number and send it on a random display.

CTRL_CHRs=("[" "]" "(" ")" "{" "}" ";" ":")

while true; do
  RND_NUM_LST=$(shuf -i 0-7 -n1)
  RND_NUM=$(shuf -i 0-10999 -n1)
  printf "Sent: %s\r\n" "${CTRL_CHRs[RND_NUM_LST]}${RND_NUM}"
  echo -ne "${CTRL_CHRs[RND_NUM_LST]}${RND_NUM}\r\n" >/dev/pts/6
  sleep 0.05
done
