import sys
import os

# srcディレクトリをパスに追加
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from app import hello_world, add_numbers

def test_hello_world():
    result = hello_world()
    assert "Hello, GitHub Actions" in result
    assert "Python 3.10" in result

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0