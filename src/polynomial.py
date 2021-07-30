from sympy import *

init_printing(use_unicode=True)


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


def replace_monomial(expression, algebra_structure):
    list_symbols, replacement = algebra_structure
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
            previous_term = actual_term
        return expression, False
    elif expression.func == Pow:
        return expression, False
    elif isinstance(expression, Symbol):
        return expression, False
    else:
        raise ValueError(f"Wrong operator {expression.func}")


def replace_polynomial(expression, algebra_structure):
    expression.expand(mul=True)
    if expression.func == Add:
        new_terms = []
        change = False
        for number, term in enumerate(expression.args):
            placement_term = replace_monomial(term, algebra_structure)
            change |= placement_term[1]
            new_terms.append(placement_term[0])

        return Add(*new_terms).expand(mul=True), change
    elif expression.func == Mul:
        # processing monomial
        placement_term = replace_monomial(expression, algebra_structure)

        return (placement_term[0]).expand(mul=True), placement_term[1]
    else:
        print(f"Wrong operator {expression.func}")


def continuous_replacement_polynomial(expression, algebra_structure):
    result = (expression, True)
    while result[1]:
        result = replace_polynomial(result[0], algebra_structure)
    return result[0]


if __name__ == "__main__":
    import unittest

    E31 = Symbol('E31', commutative=False)
    E21 = Symbol('E21', commutative=False)
    E32 = Symbol('E32', commutative=False)
    E23 = Symbol('E23', commutative=False)
    E12 = Symbol('E12', commutative=False)
    E13 = Symbol('E13', commutative=False)
    H12 = Symbol('H12', commutative=False)
    H23 = Symbol('H23', commutative=False)

    sl3_c = {
        E13 * E12: E12 * E13,
        E13 * E23: E23 * E13,
        E13 * H23: H23 * E13 - 2 * E13,
        E13 * H12: H12 * E13 - E13,
        E13 * E32: E32 * E13 + E12,
        E13 * E21: E21 * E13 - E23,
        E13 * E31: E31 * E13 + H23,
        E12 * E23: E23 * E12 + E13,
        E12 * H23: H23 * E12 - E12,
        E12 * H12: H12 * E12 - 2 * E12,
        E12 * E32: E32 * E12,
        E12 * E21: E21 * E12 + H12,
        E12 * E31: E31 * E12 - E32,

        E23 * H23: H23 * E23 - E23,
        E23 * H12: H12 * E23 + E23,
        E23 * E32: E32 * E23 + H12 + H23,
        E23 * E21: E21 * E23,
        E23 * E31: E31 * E23 + E21,

        H23 * H12: H12 * H23,
        H23 * E32: E32 * H23 - E32,
        H23 * E21: E21 * H23 - E21,
        H23 * E31: E31 * H23 - 2 * E31,

        H12 * E32: E32 * H12 + E32,
        H12 * E21: E21 * H12 - 2 * E21,
        H12 * E31: E31 * H12 - E31,

        E32 * E21: E21 * E32 + E31,
        E32 * E31: E31 * E32,

        E21 * E31: E31 * E21
    }

    class Tests(unittest.TestCase):
        def test(self):  # test method
            for key, value in sl3_c.items():
                result = continuous_replacement_polynomial(key, ([E31, E32, E21, E13, E12, E23, H12, H23], sl3_c))
                self.assertEqual(result, value)

    unittest.main()
