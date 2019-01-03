import py_vollib.black_scholes_merton.implied_volatility as BSvol
import py_vollib.black_scholes_merton.greeks.analytical as BSgreeks

t = 10/365
price = 0.56
S = 233.2
K = 235
flag = 'c'
r = .02
q = .0224

iv = BSvol.implied_volatility(price, S, K, t, r,q, flag)
td = BSgreeks.theta(flag,S,K,t,r,iv,q)
print(round(iv,3))
print (round(td,3))