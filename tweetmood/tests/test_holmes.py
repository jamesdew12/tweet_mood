from django.test import TestCase
import unittest
from unittest import mock
from unittest.mock import patch, Mock
from ..holmes import Holmes, feelings
import nltk
nltk.download('punkt')

class HolmesUnitTests(TestCase):

    def test_feeling_supremely_positive(self):
        assert feelings(75) == "supremely positive"

    def test_feeling_generally_positive(self):
        assert feelings(60) == "generally positive"

    def test_feeling_ambivalent(self):
        assert feelings(50) == "ambivalent"

    def test_feeling_rather_negative(self):
        assert feelings(40) == "rather negative"

    def test_feeling_overwhelmingly_negative(self):
        assert feelings(20) == "overwhelmingly negative"

    def test_classify(self):
        mock_prob = Mock()
        mock_prob.prob = Mock(return_value=0.50)
        mock_NBC = Mock()
        mock_NBC.prob_classify = Mock(return_value=mock_prob)
        holmes = Holmes(mock_NBC)
        assert holmes.holmes_classify('test') == {"pos": 50, "neg": 50, "pwid": 25, "nwid": 25, "feeling": "ambivalent"}
