import algoritmos

def test_distancia1():
    assert algoritmos.distancia_euclidiana(7, 5, 4, 1) == 5.0

def test_distancia2():
    assert algoritmos.distancia_euclidiana(100, 200, 200, 1) == 222.71281956816046

def test_distancia3():
    assert algoritmos.distancia_euclidiana(500, 500, 200, 200) == 424.26406871192853