#!/bin/env python

"""
Module for approximating sqrt
"""


def sqrt(x,debug=False):
   """
   Module implementing newton's method for approximating sqrt
   """
   from numpy import nan

   if x == 0.:
       return 0.
   elif x<0:
       print "***Error, x must be positive"
       return nan
   assert x>0, "Should not get here!"
   s = 1.
   kmax = 100
   tol = 1.e-14

   for k in range(kmax):
       if debug:
           print "Before iteration {}, s = {:20.15f}".format(k,s)
       s0 = s
       s = 0.5 * ( s + x/s )
       delta_s = s - s0
       if abs(delta_s/x) < tol:
           break
   if debug:
       print "After {} iterations, s = {:20.15f}".format(k+1,s)
   return s

