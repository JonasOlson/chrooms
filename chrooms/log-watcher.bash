#!/bin/bash

###
# Note that this script assumes that the console log is written to
# /var/log/srcds/tf2.log. In order to make this happen invoke srcds
# with the -consolelog /var/log/srcds/tf2.log argument.
###

cd "$( dirname "${BASH_SOURCE[0]}" )"

tail --retry -F /var/log/srcds/tf2.log |\
	while read line; do
		if echo "$line" | grep -E -q '>" joined team "(Red|Blue)"'; then
		    IFS=$'\t' read player team < <(echo $line | perl -pe's@L \d\d/\d\d/\d\d\d\d - \d\d:\d\d:\d\d: "(.+)<\d+><\[U:\d:\d+\]><.+>" joined team "(Red|Blue)"@$1\t$2@')
		    python3 ./move_user.py "$player" "$team"
		fi
	done
