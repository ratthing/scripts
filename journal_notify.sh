#!/bin/sh
OUTPUT=$(/usr/bin/cat /home/rlopez/Nextcloud/Notes/jrn/journal.md)
SUMMARY="Journal Reminder"
/usr/bin/notify-send -a "Journal Reminder" -i /usr/share/icons/gnome/48x48/emblems/emblem-urgent.png -u critical "$SUMMARY" "$OUTPUT"
exit 0
