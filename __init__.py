# -*- coding: utf-8 -*-
'''
This file is part of the Python Mapper package, an open source tool
for exploration, analysis and visualization of data.

Copyright 2011–2013 by the authors:
    Daniel Müllner, http://math.stanford.edu/~muellner
    Aravindakshan Babu, anounceofpractice@hotmail.com

Python Mapper is distributed under the GPLv3 license. See the project home page

    http://math.stanford.edu/~muellner/mapper

for more information.
'''
__version__ = '0.1.0'

import sys
if sys.hexversion < 0x02060000:
  raise ImportError('Python Mapper requires at least Python version 2.6.')

def cmappertoolserror(name):
    def f(*args, **kwargs):
        raise ImportError("please install the 'cmappertools' module "
        "for the '{}' function".format(name))
    return f

from mapper._mapper import *
from mapper.draw_mapper_output import *
from mapper.scale_graph import *

from mapper import tools
from mapper import shapes
from mapper import metric
from mapper import filters
from mapper import cover
from mapper import cutoff
