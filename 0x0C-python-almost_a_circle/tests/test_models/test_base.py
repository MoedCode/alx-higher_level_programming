import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from models.base  import Base
from models.rectangle  import Rectangle
from models.square  import Square

class TC_Base(unittest.TestCase):
     def