#!/usr/bin/env bash

# exit when subcommands return non-zero status
set -e

# This command selects those lines that don't have "### OUTPUT ###"

# p, Print out the pattern space (to the standard output).
# This command is usually only used in conjunction with the -n command-line option.
# -n, don't print out the matching pattern
# , , An address range can be specified by specifying two addresses separated by a comma (",").
#     An address range matches lines starting from where the first address matches,
#     and continues until the second address matches (inclusively).
# ! , Appending the ! character to the end of an address specification negates the sense of the match.
src=$(sed -n -e '/### OUTPUT ###/,$!p' "$1")
# add "# " to each line
# ^, matches any null string at beginning of the pattern space.
output=$(python "$1" | sed 's/^/# /')

# These are done separately to avoid having to insert a newline, which causes
# problems when the text itself has '\n' in strings
echo "$src" > $1
# -e, -e parameter will allow an escaped character,
#     such as an escaped n for newline, to have its special meaning
echo -e "\n### OUTPUT ###" >> $1
echo "$output" >> $1