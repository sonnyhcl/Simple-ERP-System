#!bin/bash
while :
 	do
	    if [ $(ps -ef | grep "wxrobot"| grep -v "grep" |  wc -l) -eq 1 ];then
	        kill $(ps -ef|grep "wxrobot"| grep -v "grep"|awk '{print $2}')
	        echo "kill and restart"
	    else
	     	echo "not found"
	    fi
	    python wxrobot.py &
	    sleep 500
 	done 