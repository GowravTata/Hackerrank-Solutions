<<QUESTION
Given a text which consists of consecutive duplicates, write the shell scripts so that it eliminates the consecutive duplicates and return it as follows

SAMPLE INPUT
00
00
01
01
00
00
02
02
03
AA
AA
AA

SAMPLE OUTPUT
2 00
2 01
2 02
1 03
3 AA
QUESTION

uniq -c | cut -c7- < test.txt
