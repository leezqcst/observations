from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from observations.util import maybe_download_and_extract


def wikitext2(path):
  """Load the Wikitext-2 data set (Merity et al., 2016). The dataset
  is preprocessed and has a vocabulary of 33,278 words. There are
  2,088k training, 217k validation, and 245k test tokens.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `wikitext-2/`.

  Returns:
    Tuple of str `x_train, x_valid, x_test`.
  """
  path = os.path.expanduser(path)
  directory = 'wikitext-2'
  if not os.path.exists(os.path.join(path, directory)):
    url = 'https://s3.amazonaws.com/research.metamind.io/wikitext/wikitext-2-v1.zip'
    maybe_download_and_extract(path, url)

  path = os.path.join(path, directory)
  with open(os.path.join(path, 'wiki.train.tokens')) as f:
    x_train = f.read().decode("utf-8")
  with open(os.path.join(path, 'wiki.test.tokens')) as f:
    x_test = f.read().decode("utf-8")
  with open(os.path.join(path, 'wiki.valid.tokens')) as f:
    x_valid = f.read().decode("utf-8")
  return x_train, x_test, x_valid
