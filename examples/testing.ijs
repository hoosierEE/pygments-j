#!/usr/bin/jconsole

NB. A comment followed by some valid J

1 2 3
NB. Here is another comment

Note 'can have a string'
this is a comment
)

'after the Note closes this should be a string'

a =. this should be an invalid line
echo a
b =. this should be an invalid line
echo b

if. a = 2 then. a = 1 end.

wordz =. 'hi, I''m a string with an embedded single quote'
echo wordz

    echo 1 2 3
  echo +/ % # (i.7)
echo 'hello world'

 i.20

 explicitNoun =: 0 :0
  The following lines will become a noun, but discarded,
  which is practically the same as a comment.
)

exit''
