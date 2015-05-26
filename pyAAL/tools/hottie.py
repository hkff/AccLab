"""
Hot swaping module written by Maciej Konieczny

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
from __future__ import absolute_import, division
__author__ = 'walid'
from collections import defaultdict
from functools import wraps
from inspect import isclass, isfunction
from os.path import exists, getmtime
import sys
from time import sleep
from weakref import WeakSet

functions = {}
classes = {}
instances = defaultdict(WeakSet)
module_mtimes = {}


def identity(obj):
    """
    Identity function
    :param obj: an object
    :return: the given object
    """
    return obj


def class_decorator(cls, key):
    classes[key] = cls
    reload_instances(key)

    old_init = cls.__init__

    @wraps(old_init)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        instances[key].add(self)

    cls.__init__ = new_init

    return cls


def function_decorator(func, key):
    functions[key] = func

    @wraps(func)
    def wrapper(*args, **kwargs):
        return functions[key](*args, **kwargs)

    return wrapper


def hot(obj):
    if isclass(obj):
        decorator = class_decorator
    elif isfunction(obj):
        decorator = function_decorator
    else:
        raise TypeError('@hot decorator can be used only on classes '
                        'and functions.')

    module = sys.modules[obj.__module__]
    remember_mtime(module)

    key = '.'.join([obj.__module__, obj.__name__])

    return decorator(obj, key)


def reload_instances(key):
    cls = classes[key]
    for obj in instances[key]:
        obj.__class__ = cls


def get_mtime(path):
    if not exists(path):
        sleep(0.1)

    return getmtime(path)


def remember_mtime(module, mtime=None):
    module_mtimes[module] = mtime or get_mtime(module.__file__)


def smartreload():
    for module, old_mtime in module_mtimes.iteritems():
        # get path to a .py file
        path = module.__file__
        if path.endswith('.pyc'):
            path = path[:-1]

        # get mtime and reload if it's changed
        new_mtime = get_mtime(path)
        if new_mtime > old_mtime:
            remember_mtime(module, new_mtime)
            reload(module)
