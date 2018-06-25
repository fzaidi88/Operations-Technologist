#!/bin/sh

curl http://s3.amazonaws.com/istreet-assets/H3aRjT7S377CbiZsDoPjwg/app.log --output /Users/aashib/Desktop/fatima_test/tmp.log


cat /Users/aashib/Desktop/fatima_test/tmp.log | awk -F, '{ if ($1>"2018-03-26T09:00:00.000" && $1<"2018-03-26T10:00:00.000") print }' > /Users/Desktop/tmp/9am.log

cat /Users/Desktop/tmp/9am.log | grep -i "DEBUG/BleWrapper.connection: BleWrapper: connection state change: disconnected with status:" > /Users/Desktop/tmp/disconnect_temp.log

cat /Users/Desktop/tmp/disconnect_temp.log | grep -v "status: 22" > //Users/Desktop/tmp/disconnections.log

grep -c "status: 22" /Users/Desktop/tmp/disconnections.log > /Users/Desktop/tmp/twenty-twos.log
