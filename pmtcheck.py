# Estimated Paycheck
# Author: Nathan Bellew
#

import sys
import os
from optparse import OptionParser

DISCLAIMER = "pmtcheck.py is is a payment checker based loosely off of equations found on local government sites. It may not be 100% accurate and is only an estimate please be cautious. It currently DOES NOT account for Overtime."
VERSION = "0.1a ALPHA"
def DIS_VER(exit):
    print(VERSION)
    print(DISCLAIMER)
    if exit:
        sys.exit(0)

usage = "Usage: %prog [ -H (Hourly Wage)] [Total Hours] or [ -S (Salary) ] [ Number of Pay Periods]"
parser = OptionParser(usage)
parser.add_option('-H', '--Hourly', dest = "Hourly", help="If -H is used it must be followed by a Number for the hourly wage. If none is provided 11.00 will be assumed.")
parser.add_option('-V', '--Version', dest = "Version", action="store_true", help="Shows Version and Disclaimer.")
parser.add_option('-S','--Salary', dest = "Salary", help=" Similar to -H but with Salary instead.")
(options,args) = parser.parse_args()

if len(args)<1:
    DIS_VER(False)
    parser.print_help()
    sys.exit(0)

def Tax(Total):
    if Total > 0 and Total < 9525:
        return 10
    elif Total > 9525 and Total < 38700:
        return 12
    elif Total > 38700 and Total < 82500:
        return 22
    elif Total > 82500 and Total < 157500:
        return 24
    elif Total > 157500 and Total < 200000:
        return 32
    elif Total > 200000 and Total < 500000:
        return 35
    else:
        return 37

def Hourly():
    TotalHours = float(args[0])
    Rate = float(options.Hourly)
    GrossEarnings = TotalHours*Rate
    FIT = Tax(GrossEarnings)/100
    EstimatedPayment = GrossEarnings-(FIT*GrossEarnings)
    return EstimatedPayment



def Salary():
    print("Salary Does not work. Sorry")

def main():
    if options.Hourly:
        print(Hourly())
    elif options.Salary:
        Salary()
    else:
        pass


if __name__ == "__main__":
    main()
