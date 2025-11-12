#!/bin/bash

# This script searches for lines in output.json that match a dynamic pattern
# constructed from command-line arguments, highlighting the matches in red.

# Check if arguments are provided
if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <pattern1> [pattern2] [pattern3] ..."
    exit 1
fi

# 1. Build the dynamic grep pattern:
#    - We need to join all arguments with '":|"'
#    - Example: "arg1", "arg2" -> "arg1":|"arg2":

# Format arguments: Escape dots and other regex special characters if needed,
# then append the required ':'. Join them with '|'.
# Note: Since the pattern is enclosed in '("..."|"":)', we only need to build the middle part.

# Append '":' to each argument and join with '|'
# printf handles multi-argument formatting efficiently
INNER_PATTERN=$(printf '%s":|' "$@" | sed 's/|$//')

# The final pattern, including the fixed parts '("', '|"":)'
FINAL_PATTERN='("'"$INNER_PATTERN"'|"":)'

# 2. Execute the command:
#    - Use `grep -E` for extended regex.
#    - Use `--color=always` to force coloring of matches even when piped.
#    - Pipe through `cat` to ensure coloring persists (or use `grep --color=auto` if not piping).
#    - Setting GREP_COLORS='mt=1;31' explicitly sets the match color to bright red (31).
#      (The default often uses red, but this guarantees it).

GREP_COLORS='mt=1;31' cat output.json | grep -E --color=always "$FINAL_PATTERN"