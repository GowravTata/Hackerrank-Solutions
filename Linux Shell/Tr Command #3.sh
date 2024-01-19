<<QUESTION
Given a text , replace all sequences of multiple spaces with just one space
Input:
He  llo
Wor  ld
how  are  you

Output:
He llo
Wor ld
how are you
QUESTION

cat sample.txt | tr '   ' ' '

