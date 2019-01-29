import os
import tempfile

import pyslices_ipynb_conversion as pic

f = os.path.join(os.path.dirname(__file__), '../data/sample.pyslices')
outf = os.path.join(tempfile.gettempdir(), 'test.ipynb')

pic.write_ipynb_from_pyslices(f, outf)

print(pic.make_pyslices_from_ipynb(outf))

# Round-tripping works but inserts input in front of every output and
# insists that the last line is a blank (file ends in '\n')
