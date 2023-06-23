#!/bin/sh
PU_ARRAY=( home ibm koc personal utsa )
for PU_PREFIX in "${PU_ARRAY[@]}"
do
    PICKUPFILE=$(ls /home/rlopez/Downloads/$PU_PREFIX--* 2> /dev/null | wc -l)
    if [ "$PICKUPFILE" != "0" ]; then
        FILE_LIST=$(ls /home/rlopez/Downloads/$PU_PREFIX--*)
	echo "$FILE_LIST" | while IFS= read -r f;
            do
		    MOVE_TARGET="$PU_PREFIX:/ \"$f\""
		    NB_MOVE_CMD=$("/home/rlopez/bin/nb import move $MOVE_TARGET")
		   echo $NB_MOVE_CMD 
            done
    fi
done
exit 0
