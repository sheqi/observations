from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.tucker import tucker


def test_tucker():
  """Test module tucker.py by downloading
   tucker.csv and testing shape of
   extracted data has 9 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = tucker(test_path)
  try:
    assert x_train.shape == (9, 9)
  except:
    shutil.rmtree(test_path)
    raise()
