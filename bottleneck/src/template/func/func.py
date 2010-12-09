
from bottleneck.src.template.template import make

from nanmin import nanmin
from median import median

funcs = {}
funcs['nanmin'] = nanmin
funcs['median'] = median

def build(funcs=funcs):
    for func in funcs:
        make(funcs[func])
