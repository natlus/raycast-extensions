#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Toggle autohide dock
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖
# @raycast.packageName Toggle autohide dock

# Documentation:
# @raycast.author natlus

import subprocess
import re

# Current value of the plist setting
current = subprocess.run(["defaults", "read", "com.apple.dock", "autohide"], capture_output=True).stdout.decode('utf-8').strip()

if current == "1":
  print('Shown')
  subprocess.run(["defaults", "write", "com.apple.dock", "autohide", "-bool", "false"])
else:
  print('Hidden')
  subprocess.run(["defaults", "write", "com.apple.dock", "autohide", "-bool", "true"])

# Restart Dock
subprocess.run(['Killall', 'Dock'])
