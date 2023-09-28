from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    pq = PriorityQueue()
    pq.enqueue({"qtd_linhas": 10})
    pq.enqueue({"qtd_linhas": 3})
    pq.enqueue({"qtd_linhas": 2})
    assert pq.dequeue() == {"qtd_linhas": 3}
    assert pq.search(1) == {"qtd_linhas": 10}
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        pq.search(100)
