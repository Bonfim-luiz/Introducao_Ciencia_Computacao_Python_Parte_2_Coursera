def fatorial(n):
    if n < 1:
        return 1
    else:
        return n*fatorial(n-1)

import pytest

@pytest.mark.parametrize("entrada,esperado",[
    (0, 1),
    (1, 1),
    (-10, 1),
    (4, 24),
    (5, 120)
    ])

def test_fatorial(entrada,esperado):
    assert fatorial(entrada) == esperado
