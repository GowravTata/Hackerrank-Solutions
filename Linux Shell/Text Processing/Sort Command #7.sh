<<QUESTION
Given a text file which is delimited by tab, return the text with second column sorted in descending order
QUESTION
sort -t$'|' -nr -k2 /dev/stdin