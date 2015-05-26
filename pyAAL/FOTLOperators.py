"""
<one line to give the program's name and a brief idea of what it does.>
Copyright (C) 2014 Walid Benghabrit

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = 'walid'

from enum import Enum


# FOTL operators
class FOTLOperators(Enum):
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
