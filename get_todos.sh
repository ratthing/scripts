#!/bin/sh

NB_PATH=$HOME/Nextcloud/Notes/nb
NB_TODO_SUFFIX=todo.md

NB_TODO_FILE_COUNT=$(find $NB_PATH -type f -name *.$NB_TODO_SUFFIX 2> /dev/null | wc -l)
if [ "NB_TODO_FILE_COUNT" != "0" ]; then
    NB_TODO_FILE_NAMES=$(find $NB_PATH -type f -name *.$NB_TODO_SUFFIX -print 2> /dev/null)
    for f in $NB_TODO_FILE_NAMES; 
        do
            cat "$f"
            echo "$f"
        done
fi
