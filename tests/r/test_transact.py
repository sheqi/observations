from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.transact import transact


def test_transact():
  """Test module transact.py by downloading
   transact.csv and testing shape of
   extracted data has 261 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = transact(test_path)
  try:
    assert x_train.shape == (261, 3)
  except:
    shutil.rmtree(test_path)
    raise()
