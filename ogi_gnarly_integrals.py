from sympy import *

s, t = symbols('s t')
u0, u1 = symbols('u0 u1')
v00, v10, v01, v11 = symbols('v00 v10 v01 v11')
sp = u0 + s*(u1-u0)
tp = v00 + s*(v10-v00)+t*(v01-v00)+s*t*(v11-v01-v10+v00)
m0 = 1-sp-tp+sp*tp
m1 = tp-sp*tp
m2 = sp-sp*tp
m3 = sp*tp
left = v01-v00+s*(v11-v01-v10+v00)
Q11 = integrate( left*integrate( m0*m0, (t,0,1) ), (s,0,1) )
Q12 = integrate( left*integrate( m0*m1, (t,0,1) ), (s,0,1) )
Q13 = integrate( left*integrate( m0*m2, (t,0,1) ), (s,0,1) )
Q14 = integrate( left*integrate( m0*m3, (t,0,1) ), (s,0,1) )
Q22 = integrate( left*integrate( m1*m1, (t,0,1) ), (s,0,1) )
Q23 = integrate( left*integrate( m1*m2, (t,0,1) ), (s,0,1) )
Q24 = integrate( left*integrate( m1*m3, (t,0,1) ), (s,0,1) )
Q33 = integrate( left*integrate( m2*m2, (t,0,1) ), (s,0,1) )
Q34 = integrate( left*integrate( m2*m3, (t,0,1) ), (s,0,1) )
Q44 = integrate( left*integrate( m3*m3, (t,0,1) ), (s,0,1) )
p00, p01, p10, p11 = symbols('p00 p01 p10 p11')
Δ = p00 + s*(p10-p00) + t*(p01-p00) + s*t*(p11 - p01 - p10 + p00)
T1 = integrate( left*integrate( m0*Δ, (t,0,1) ), (s,0,1) )
T2 = integrate( left*integrate( m1*Δ, (t,0,1) ), (s,0,1) )
T3 = integrate( left*integrate( m2*Δ, (t,0,1) ), (s,0,1) )
T4 = integrate( left*integrate( m3*Δ, (t,0,1) ), (s,0,1) )
print( "# Q11" )
print( Q11 )
print( "# Q12" )
print( Q12 )
print( "# Q13" )
print( Q12 )
print( "# Q14" )
print( Q14 )
print( "# Q22" )
print( Q22 )
print( "# Q23" )
print( Q23 )
print( "# Q24" )
print( Q24 )
print( "# Q33" )
print( Q33 )
print( "# Q34" )
print( Q34 )
print( "# Q44" )
print( Q44 )
print( "# T1" )
print( T1 )
print( "# T2" )
print( T2 )
print( "# T3" )
print( T3 )
print( "# T4" )
print( T4 )
