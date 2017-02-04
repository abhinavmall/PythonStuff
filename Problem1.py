# This program claculates minimum fixed monthly amount to pay over the year against credit card balance. Rounds off to nearest cent.
# Uses bisection algorithm for efficient calculation.
# Formula is given below

#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly payment lower bound = Balance / 12
#Monthly payment upper bound = (Balance x (1 + Monthly interest rate)**12) / 12.0

#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal

balance = 320000
annualInterestRate = 0.2

mir = annualInterestRate/12.0
lb = float("{0:.2f}".format(balance/12.0))
ub = float("{0:.2f}".format((balance * (1 + mir)**12)/12.0))

def cb(balance, fmp):
    b = balance
    for i in range(12):
        mub = b - fmp
        b = mub + (mir * mub)
    return float("{0:.2f}".format(b))

fmp = 0
while lb <= ub:
    mid = float("{0:.2f}".format((lb+ub)/2,0))
    balanceLow = cb(balance, fmp=lb)
    balanceMid = cb(balance, fmp=mid)
    balnceHigh = cb(balance, fmp=ub)

    if balanceMid == 0 or mid-lb<0.01 or ub-mid<0.01:
        fmp = mid
        break
    elif balanceMid > 0:
        lb = mid
    else:
        ub = mid

print(fmp)
