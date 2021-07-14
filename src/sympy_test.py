from sympy import *
from sympy.polys.monomials import itermonomials
from sympy import Poly
from sympy.abc import A, B

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


def relevant_terms(term, list_symbols):
    previous_symbol = None
    previous_power = None
    if term in list_symbols:
        previous_symbol = term
        previous_power = 1
    elif term.func == Pow:
        previous_symbol = term.args[0]
        previous_power = term.args[1]
    return previous_symbol, previous_power


def replace_monomial(expression, replacement, list_symbols):
    if expression.func == Mul:
        previous_term = (None, None)
        for number, term in enumerate(expression.args):
            actual_term = relevant_terms(term, list_symbols)
            if None == actual_term[0]:
                continue
            elif None != previous_term[0]:
                multiplication = previous_term[0] * actual_term[0]
                if multiplication in replacement:
                    before_insertation = list(expression.args[:number - 1])
                    if previous_term[1] != 1:
                        before_insertation.append(Pow(previous_term[0], previous_term[1] - 1))
                    after_insertation = list(expression.args[number + 1:])
                    if actual_term[1] != 1:
                        after_insertation.insert(0, Pow(actual_term[0], actual_term[1] - 1))
                    return Mul(*before_insertation, replacement[multiplication], *after_insertation), True
                else:
                    return expression, False
            previous_term = actual_term
    else:
        print(f"Wrong operator {expression.func}")


def replace_polynomial(expression, replacement, list_symbols):
    expression.expand(mul=True)
    if expression.func == Add:
        new_terms = []
        change = False
        for number, term in enumerate(expression.args):
            placement_term = replace_monomial(term, replacement, list_symbols)
            change |= placement_term[1]
            new_terms.append(placement_term[0])

        return Add(*new_terms).expand(mul=True), change
    else:
        print(f"Wrong operator {expression.func}")

pprint(replace_monomial(x*y*x, {x*y: y*y}, [x, y]))
pprint(replace_monomial(x*x*y, {x*y: y*y}, [x, y]))

sl3_c = {
    E13*E12: E12*E13,
    E13*E23: E23*E13,
    E13*H23: H23*E13-2*E13,
    E13*H12: H12*E13-E13,
    E13*E32: E32*E13+E13,
    E13*E21: E21*E13-E23,
    E13*E31: E31*E13+H23,
    E12*E23: E23*E12+E13,
    E12*H23: H23*E12+E13,
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
    H23*E23: E32*H23-E32,
    H23*E21: E21*H23-E21,
    H23*E31: E31*H23-2*E31,

    H12*E32: E32*H12+E32,
    H12*E21: E21*H12-2*E21,
    H12*E31: E31*H12-E31,

    E32*E21: E21*E32+E31,
    E32*E31: E31*E32,

    E21*E31: E31*E21
    }
pprint(replace_monomial(E31*E31*E32, {E31*E32: E32*E23+H12+H23}, [E31, E32, E21, E13, E12, E23, H12, H23]))
result = replace_monomial(E31*E31*E32, {E31*E32: E32*E23+H12+H23}, [E31, E32, E21, E13, E12, E23, H12, H23])[0].expand(mul=True)
pprint(result)
pprint(replace_polynomial(E31*E31*E32 + 2*E32*E31*E31, {E31*E32: E32*E23+H12+H23}, [E31, E32, E21, E13, E12, E23, H12, H23]))
pprint(replace_polynomial(E31*E31*E32 + 2*E32*E31*E31, sl3_c, [E31, E32, E21, E13, E12, E23, H12, H23]))
pprint(replace_polynomial(H12*E31*H23*E32 + 2*E32*E31*E31, sl3_c, [E31, E32, E21, E13, E12, E23, H12, H23]))
