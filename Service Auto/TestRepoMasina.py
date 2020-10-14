from Domain.Masina import Masina
from Repository.RepositoryGeneric import Repository


def test_repo_masina():

    r = Repository('testMas.pkl')
    mas = Masina(1, 'model', 12, 54, True)
    mas2 = Masina(2, 'model2', 54, 23, False)
    r.add_element(mas)
    r.add_element(mas2)
    assert len(r.get_elements()) == 2
    c3 = (Masina(2, 'model434', 333, 222, False))
    r.update_element(c3)
    updated = r.get_elements()[1]
    assert updated == c3
    r.remove_element(mas)
    assert len(r.get_elements()) == 1

test_repo_masina()