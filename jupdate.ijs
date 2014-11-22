#!/usr/bin/jconsole

NB. updateLexer script, J translation

0 : 0
Original script:

#!/bin/bash
pygmentsDir=site-packages/pygments/lexers
if [[ $(uname) = "Darwin" ]]; then
    sudo cp j.py /Library/Python/2.7/"$pygmentsDir"/
else
    sudo cp j.py /usr/lib/python2.7/"$pygmentsDir"/
fi
pygmentize -f html -O full -o output/test.html mortgage.ijs
)

pygmentsDir=.'site-packages/pygments/lexers'

uname=.{.;:2!:0'uname'
osx=.uname=<'Darwin'

condEcho =. 3 : 0
if. y do. echo 'this is OSX' else. echo 'pygmentsDir' end.
)

condEcho osx

NB. echo uname,<osx

exit''

