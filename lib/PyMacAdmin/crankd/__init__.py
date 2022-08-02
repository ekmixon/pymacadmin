#!/usr/bin/env python
# encoding: utf-8

import sys

def not_implemented(*args, **kwargs):
    """A dummy function which exists only to catch configuration errors"""
    # TODO: Is there a better way to report the caller's location?
    import inspect
    stack = inspect.stack()
    my_name = stack[0][3]
    caller  = stack[1][3]
    raise NotImplementedError(
        f'{my_name} should have been overridden. Called by {caller} as: {my_name}({", ".join(map(repr, args) + [f"{k}={repr(v)}" for k,v in kwargs.items()])})'
    )

from . import handlers
sys.modules[handlers.__name__] = handlers