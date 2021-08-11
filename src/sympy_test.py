from sympy import *
import polynomial

init_printing(use_unicode=True) 

x = Symbol('x', commutative=False)
y = Symbol('y', commutative=False)
E31 = Symbol('E31', commutative=False)
E21 = Symbol('E21', commutative=False)
E32 = Symbol('E32', commutative=False)
E23 = Symbol('E23', commutative=False)
E12 = Symbol('E12', commutative=False)
E13 = Symbol('E13', commutative=False)
H12 = Symbol('H12', commutative=False)
H23 = Symbol('H23', commutative=False)


pprint(polynomial.replace_monomial(x*y*x, ([x, y], {x*y: y*y})))
pprint(polynomial.replace_monomial(x*x*y, ([x, y], {x*y: y*y})))

sl3_c = {
    E13*E12: E12*E13,
    E13*E23: E23*E13,
    E13*H23: H23*E13-2*E13,
    E13*H12: H12*E13-E13,
    E13*E32: E32*E13+E12,
    E13*E21: E21*E13-E23,
    E13*E31: E31*E13+H23,
    E12*E23: E23*E12+E13,
    E12*H23: H23*E12-E12,
    E12*H12: H12*E12-2*E12,
    E12*E32: E32*E12,
    E12*E21: E21*E12+H12,
    E12*E31: E31*E12-E32,

    E23*H23: H23*E23-E23,
    E23*H12: H12*E23+E23,
    E23*E32: E32*E23+H12+H23,
    E23*E21: E21*E23,
    E23*E31: E31*E23+E21,

    H23*H12: H12*H23,
    H23*E32: E32*H23-E32,
    H23*E21: E21*H23-E21,
    H23*E31: E31*H23-2*E31,

    H12*E32: E32*H12+E32,
    H12*E21: E21*H12-2*E21,
    H12*E31: E31*H12-E31,

    E32*E21: E21*E32+E31,
    E32*E31: E31*E32,

    E21*E31: E31*E21
    }
pprint(polynomial.continuous_replacement_polynomial(E32*E21*E21, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint(polynomial.continuous_replacement_polynomial(E32*E32*E21, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint(polynomial.continuous_replacement_polynomial(E32*E21*E21*E21, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint(polynomial.continuous_replacement_polynomial(E32*E32*E21*E21, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint(polynomial.continuous_replacement_polynomial(E32*E32*E32*E21, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))

pprint(polynomial.continuous_replacement_polynomial(H12*E21*E21, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint(polynomial.continuous_replacement_polynomial(H12*H12*E21, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint(polynomial.continuous_replacement_polynomial(H12*E21*E21*E21, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint(polynomial.continuous_replacement_polynomial(H12*H12*E21*E21, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint(polynomial.continuous_replacement_polynomial(H12*H12*H12*E21, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))

pprint(polynomial.continuous_replacement_polynomial(E23*E32*E32, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint(polynomial.continuous_replacement_polynomial(E23*E23*E32, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint(polynomial.continuous_replacement_polynomial(E23*E32*E32*E32, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint(polynomial.continuous_replacement_polynomial(E23*E23*E32*E32, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint(polynomial.continuous_replacement_polynomial(E23*E23*E23*E32, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))

pprint(polynomial.continuous_replacement_polynomial(H23*H12*E31, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint(polynomial.continuous_replacement_polynomial(H23*H12*E31*E31, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint(polynomial.continuous_replacement_polynomial(H23*H12*H12*E31, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint(polynomial.continuous_replacement_polynomial(H23*H23*H12*E31, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))

pprint('=============================')
pprint(polynomial.continuous_replacement_polynomial(Pow(H23,2)*Pow(H12,2)*Pow(E31,2), ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint('=============================')
pprint(polynomial.continuous_replacement_polynomial(Pow(H23,3)*Pow(H12,3)*Pow(E31,3), ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint('=============================')
pprint(polynomial.continuous_replacement_polynomial(Pow(H23,4)*Pow(H12,4)*Pow(E31,4), ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint('=============================')
pprint(polynomial.continuous_replacement_polynomial(Pow(H23,8)*Pow(H12,3)*Pow(E31,3), ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
pprint('=============================')
pprint(polynomial.continuous_replacement_polynomial(Pow(H23,8)*Pow(H12,5)*Pow(E31,5), ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c)))
