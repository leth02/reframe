import pandas as pd
import pytest
from reframe import Relation

@pytest.fixture
def r1():
    data_real = {"name": ["Jaejoong", "Junsu","Yoochun"], "age": [33, 32, 33], "height": [179, 178, 180]}
    df = pd.DataFrame(data=data_real)
    return Relation(df)
@pytest.fixture
def r2():
    data_real = {"songs": ["Fallen leaves","Love in the ice"]}
    df = pd.DataFrame(data=data_real)
    return Relation(df)



def test_product(r1,r2):
    r = r1.product(r2)
    r_expected = Relation("tests/test_product_expected.csv", sep="|")

    print(r_expected)
    print(r)
    
    assert r.equals(r_expected)

def main():
    my_relation_1 = r1()
    my_relation_2 = r2()
    test_product(my_relation_1, my_relation_2)

if __name__ == "__main__":
    main()