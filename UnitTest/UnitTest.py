import pytest
from LinkList import Node, LinkList
from FactoryMethod import Factory, FactoryA, FactoryB


class TestLinkList:
    def test_node(self):
        value = 10
        n = Node(value)
        n.print()
        assert value == n.val
        assert n.next is None

    def test_link_list(self):
        lst = LinkList()
        a = (3, 35, -5, 7, 10)
        lst.create(a)
        lst.head.print()
        p = lst.head
        for b in a:
            assert b == p.val
            p = p.next
        new = 55
        lst.insert(1, new)
        p = lst.head
        p = p.next
        assert new == p.val


class TestFactoryMethod:
    def test_factory_method(self):
        factory = FactoryA()
        p = factory.create_product()
        p.action()
        factory = FactoryB()
        p = factory.create_product()
        p.action()


if __name__ == '__main__':
    pytest.main(["-s", "UnitTest.py"])
