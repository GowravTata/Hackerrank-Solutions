<<QUESTION
Given a text file ,sort all the numbers in ascending order for 2nd column, delimited by a tab
QUESTION
sort -t$'\t' -n -k2 /dev/stdin