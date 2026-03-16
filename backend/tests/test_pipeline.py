import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from preprocessing.tokenizer import clean_text

def test_clean_text_removes_html():
    result = clean_text("<br />Great movie!")
    assert "<" not in result
    assert "br" not in result

def test_clean_text_removes_stopwords():
    result = clean_text("this is a very good film")
    assert "this" not in result
    assert "is" not in result

def test_clean_text_lowercases():
    result = clean_text("BRILLIANT Film")
    assert result == result.lower()

def test_clean_text_removes_punctuation():
    result = clean_text("Amazing!!! Truly, great.")
    assert "!" not in result
    assert "," not in result