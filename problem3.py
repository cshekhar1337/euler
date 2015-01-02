#Copyright (c) 2014 Chandra Shekhar
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in
#the Software without restriction, including without limitation the rights to
#use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
#the Software, and to permit persons to whom the Software is furnished to do so,
#subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
#FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
#COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
#IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


primes=[]

def calcPrimes():
    global primes
    primes=[]
    p=[]
    maxNum = 10**7+1
    for i in xrange(maxNum):
        p.append(1)
    p[0]=0
    p[1]=0
    for i in xrange(2,maxNum):
        if p[i] == 1:
            primes.append(i)
            for j in xrange(i*2,maxNum,i):
                p[j]=0



def isPrime(n):
    global primes
    if len(primes) == 0:
        calcPrimes()
    for i in primes:
        if n==i: 
            return True
        if n%i == 0:
            return False


    return True


def prob3():
    num=600851475143
    i=1
    mxPrime=0
    while i*i <=num:        
        if num%i == 0:
            if isPrime(i):
                mxPrime=max(mxPrime,i)
            if isPrime(num/i):
                mxPrime=max(mxPrime,num/i)
        i+=1
    print mxPrime

prob3()
