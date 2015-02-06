__author__ = 'hkff'

from enum import Enum


class LTLOperators(Enum):
    t_equal = '='
    t_not = '~'
    t_and = '&'
    t_or = '|'
    t_implication = '=>'
    t_equivalence = '<=>'
    t_forall = '!'
    t_exists = '?'
    t_always = 'always'
    t_next = 'next'
    t_sometime = 'sometime'
    t_until = 'until'
    t_unless = 'unless'

    def __str__(self):
        return self.value