import pytest
from utils import arrs


@pytest.fixture
def coll0():
    return []


@pytest.fixture
def coll3():
    return [1, 2, 3]


@pytest.fixture
def coll4():
    return [1, 2, 3, 4]


def test_get(coll0, coll3, coll4):
    assert arrs.get(coll4, 3, "test") == 4
    assert arrs.get(coll3, 1, "test") == 2
    assert arrs.get(coll0, 0, "test") == "test"


def test_slice(coll0, coll3, coll4):
    assert arrs.my_slice(coll4, 1, 3) == [2, 3]
    assert arrs.my_slice(coll3, 1) == [2, 3]
    assert arrs.my_slice(coll0, 1) == []
    assert arrs.my_slice(coll3) == [1, 2, 3]
