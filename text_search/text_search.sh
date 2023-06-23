#!/bin/sh

# text_search - simple script to recreate function of the ADDRSS and SCHEDL 
#          programs on the Tandy 100/102/200 computers.
# 
# Ray Lopez (rl@well.com)
#
# Install
# To use this script place it in your $PATH. Then make the following symbolic
# links to this script:
#   ln -s ./text_search ./addrss
#   ln -s ./text_search ./schedl
# When the script is called as addrss, it will search through the file ADRS.DO
# by default. When it is called as schedl, it will search through the file
# NOTE.DO by default.   
# 
# By default the configuration file for text_search is found at 
# $HOME/.text_search/config. 
#
# The data files ADRS.DO and NOTE.DO are also located at $HOME/.text_search.
#
# ADRS.DO and NOTE.DO are text files with one line entry per record.  Here is an
# example of a couple of ADRS.DO entries:
#
#    Albert Einstein, 201-555-1234, Princeton NJ
#    Pope Francis, pope@vatican.va, Vatican City
#
# Here is an example of a couple of NOTE.DO entries:
#
#    Jan 1, Doctor appt, 9:00 AM
#    Jan 17, Staff meeting, 10:00 AM, large conf room
#    Todo, buy milk
#    Todo, URGENT, pay bills 
#
# The script doesn't care what you have on each line.  All it does is to recursively
# search (using grep) the file for each of the strings you type in.

# Function to diplay error messages
err_msg () {
	echo ""
	echo $1
	printf '\a'
	read -n1 -r -p "Press space bar to continue" key
	echo ""

}

# Function to exit script
exit_script () {
	exit 0
}

# Function to get user input and respond to queries
get_user_input () {
	USER_INPUT=""
	SEARCH=""	
	while [[ "$SEARCH" != "menuquit" ]]; do
		read -p "$USER_PROMPT" USER_INPUT
		INPUT_ARRAY=($USER_INPUT)
		case ${INPUT_ARRAY[0]} in
			find)
				INPUT_ARRAY_LENGTH=${#INPUT_ARRAY[@]}
				ELEMENT_COUNTER=1
				GREP_FIND_TARGET_CMD=""
				while [ $ELEMENT_COUNTER -lt $INPUT_ARRAY_LENGTH ]
				do
					BASE_SEARCH_TERM="$GREP_CMD -i ${INPUT_ARRAY[$ELEMENT_COUNTER]}"
					if [ $ELEMENT_COUNTER = 1 ]; then
						BASE_SEARCH_TERM="$BASE_SEARCH_TERM $DATAPATH"
					else
						BASE_SEARCH_TERM=" | $BASE_SEARCH_TERM"
					fi
					GREP_FIND_TARGET_CMD="$GREP_FIND_TARGET_CMD$BASE_SEARCH_TERM"
					let ELEMENT_COUNTER+=1
				done
				eval $GREP_FIND_TARGET_CMD
				;;
			edit)
				$EDITOR $DATAPATH
				;;

			menu | quit)
				SEARCH="menuquit"	
				;;
			*)
				echo "Usage: find <search string>"
				echo "       edit (to edit data file)"
				echo "       menu or quit (exits program)"
				;;
		esac	
	done
}

# Check for and read config file
CONFIG_FILE=$HOME/.text_search/config
if [ -f "$CONFIG_FILE" ]; then
        . $CONFIG_FILE
else
        err_msg "CONFIG not found. "
        exit_script
fi

# Decide if I am going to run as addrss or schedl
if [[ "$0" =~ .*"addrss".* ]]; then
	USER_PROMPT="Adrs: "
	DATAPATH=$ADRS_DATA
elif [[ "$0" =~ .*"schedl".* ]]; then
	USER_PROMPT="Schd: "
	DATAPATH=$SCHDL_DATA
else
	err_msg "Script must be run as addrss or schedl"
	exit_script
fi

# Check for data file and then go get user input
if [ -f "$DATAPATH" ]; then
	get_user_input
else
        err_msg "$DATAPATH not found"
fi

# Bye bye
exit_script
