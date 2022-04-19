#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Toggle desktop items
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖
# @raycast.packageName Hide/Show Desktop Items

# Documentation:
# @raycast.author natlus

import subprocess
import re

# Current value of the plist setting
current = subprocess.run(["defaults", "read", "com.apple.finder", "CreateDesktop"], capture_output=True).stdout.decode('utf-8').strip()

if current == 'true':
  # Hide icons
  print('Hidden')
  subprocess.run(["defaults", "write", "com.apple.finder", "CreateDesktop", "false"])
  subprocess.run(['Killall', 'Finder'])
else:
  # Show icons
  print('Shown')
  subprocess.run(["defaults", "write", "com.apple.finder", "CreateDesktop", "true"])

# Restart Finder.app
subprocess.run(['Killall', 'Finder'])
