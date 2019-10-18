import pandas as pd
import pytest
from reframe import Relation

@pytest.fixture
def r():
    data_real = {"name": ["Changmin", "Jaejoong", "Junsu","Yoochun","Yunho"], "age": [31, 33, 32, 33, 33], "height": [186, 179, 178, 180, 184]}
    df = pd.DataFrame(data=data_real)
    return Relation(df)

def test_select(r):
    r = r.select("name == 'Changmin'")
    data_expected = {"name": ["Changmin"], "age": [31], "height": [186] }
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)
    assert r.equals(r_expected)

def test_select_2(r):
    r = r.select("height > 180")
    data_expected = {"name":["Changmin","Yunho"], "age":[31,33], "height": [186,184]}
    df_expected_2 = pd.DataFrame(data = data_expected)
    r_expected_2 = Relation("tests/test_select_expected_1.csv", sep="|")
    
    assert r.equals(r_expected_2)

def main():
    my_relation = r()
    test_select(my_relation)
    test_select_2(my_relation)

if __name__ == "__main__":
    main()