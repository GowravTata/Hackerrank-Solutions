<<QUESTION
Given a text which consists of consecutive duplicates, write the shell scripts so that it eliminates the consecutive duplicates and returns only the unique values using unique command
QUESTION

# 1st Approach
uniq < /dev/stdin

# 2nd Approach
cat /dev/stdin > file.txt
uniq file.txt