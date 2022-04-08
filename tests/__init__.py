from __future__ import absolute_import

import os
import sys

path_to_import = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, path_to_import)

import pt_at_qr_code
