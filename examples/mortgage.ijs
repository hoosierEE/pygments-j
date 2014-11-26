#!/usr/bin/jc

NB. Noun definition. Everything between the 0 :0 and the ) by itself is a string.
0 :0
Extra Simple Mortgage Calculator
================================
Input: House Cost in dollars
Output: Monthly payment to fully amortize the loan, with the following assumptions:
1. Down payment: $10k
2. Annual interest rate: 5%
3. Loan term: 15 years
)

NB. some assigments. =. is local/private, =: is global/public.
downPayment =. 10000
monthlyRate =. 0.05 % 12
loanMonths  =. 15 * 12
houseAmount =. ".>}.}.ARGV NB. get the input arguments
loanAmount  =. houseAmount - downPayment

Note 'a note'
a multiline note should count as a comment
until it reaches a closing ) on a line by itself.
)

  Note 'notes'
can start with whitespace
)


NB. a noun definition may be named
explanation =. 0 : 0
Monthly Payment Formula
=======================
P = L((c(1 + c)^n) / (1 + c)^n - 1)
where
P = monthly payment
L = loan amount
c = monthly interest (i.e. APR divided by 12)
n = number of payments (same as number of months)
)

NB. Ackerman's function; because why not?
Ack =: 4 : 0
NB. Ack =: verb define
if.     x = 0 do. y + 1 NB. a comment at the end
elseif. y = 0 do. (x - 1) Ack 1
NB. a comment in the middle!
elseif. 1     do. (x - 1) Ack (x Ack y - 1)
end.
)
echo 2 Ack 3 NB. 9

NB. Some valid expressions.
i.7
num0 =. 10j4 NB. imaginary
num0 =. 1.0j4
num0 =. 9j_3
num0 =. 38.9j_12.3
num1 =. 10e3 NB. scientific notation
num4 =. _ NB. infinity
num4 =. __ NB. negative infinity
num4 =. _10x
num4 =. 10x
NB. ill-formed numbers and syntax errors
num5 =. 10.3x
num5 =. ___
num5 =. ________


NB. the naive calculation:
monthlyPayment =. loanAmount * ((monthlyRate * (1 + monthlyRate)^loanMonths) % ((1 + monthlyRate)^loanMonths) - 1)

NB. mildly refacored:
NB. termInterest =. (1 + monthlyRate)^loanMonths
NB. monthlyPayment =. loanAmount * ((monthlyRate * termInterest) % (termInterest - 1))

str =. 'hey, I''m a string! With numbers inside: 1 2 3 4 5'

echo monthlyPayment
exit''
