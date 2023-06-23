#!/bin/sh

# mm - Bash script to enter Memory Mate notes
# Written by Ray Lopez (rl@well.com)
#
# MM_FILE_NAME_FORMAT uses formatting for the
# Unix date command.  

EDITOR_COMMAND="/usr/bin/vim '+normal Go' "
MM_FILE_DIR=$HOME/Nextcloud/Notes/MemoryMate
MM_FILE_NAME_FORMAT=%G-%b-%d-%T-%Z
MM_FILE_NAME_EXT=md
MM_TIME_STAMP_FORMAT="MemoryMate: %G %b %d %T %Z"

#Create the new text file
MM_FILE_NAME_DATE=$(/bin/date +$MM_FILE_NAME_FORMAT)
MM_FILE_NAME=$MM_FILE_DIR'/'$MM_FILE_NAME_DATE'.'$MM_FILE_NAME_EXT
MM_TIME_STAMP=$(/bin/date "+$MM_TIME_STAMP_FORMAT")'\n'
/bin/echo -e $MM_TIME_STAMP > $MM_FILE_NAME

#Launch the text editor with the new text file
CMD="$EDITOR_COMMAND $MM_FILE_NAME"
eval $CMD

#Exit cleanly
exit 0
