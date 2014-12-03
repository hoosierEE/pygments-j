#!/usr/bin/jconsole

Note 'about this script'
This script makes some key assumptions about term and interest rate and spits out a monthly payment.
)

about =. 0 :0
Extra Simple Mortgage Calculator
================================
Input: House Cost in dollars
Output: Monthly payment to fully amortize the loan, with the following assumptions:
1. Down payment: $10k
2. Annual interest rate: 5%
3. Loan term: 15 years
)

downPayment =. 6000
monthlyRate =. 0.05 % 12
loanMonths  =. 15 * 12
houseAmount =. ".>}.}.ARGV NB. get the input arguments
loanAmount  =. houseAmount - downPayment
insurance   =. 75
taxes       =. houseAmount * 0.01 % 12
NB. pmi         =. NB. TODO this

explanation =. 0 :0
Monthly Payment Formula
=======================
P = L((c(1 + c)^n) / (1 + c)^n - 1)
where
P = monthly payment
L = loan amount
c = monthly interest (i.e. APR divided by 12)
n = number of payments (same as number of months)
)

NB. the naive calculation:
monthlyPayment =. loanAmount * ((monthlyRate * (1 + monthlyRate)^loanMonths) % ((1 + monthlyRate)^loanMonths) - 1)
monthlyPayment =. monthlyPayment + insurance + taxes

Note 'slightly refactored but still not idiomatic'
mildly refacored:
termInterest =. (1 + monthlyRate)^loanMonths
monthlyPayment =. loanAmount * ((monthlyRate * termInterest) % (termInterest - 1))
)

echo monthlyPayment
exit''
