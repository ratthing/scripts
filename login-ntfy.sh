#!/bin/sh
/usr/bin/curl -H "Title: Login to $HOSTNAME" -H "Priority: urgent" -H "Tags: computer" -d "$USER login to $HOSTNAME SSH_CONNECTION=$SSH_CONNECTION" salsa.net:8099/login-ntfy >/dev/null 2>&1
exit 0

