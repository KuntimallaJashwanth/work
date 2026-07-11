# app.py
# This is a test commit to see how github actions work's
# Retrying after changing the py file loaction in the actions file, 2nd change, 3rd change,4th,5th
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
