# -*-coding=utf8-*-
import pytest


def dataList():
    return [1, 2, 3, 4, 5, 6]


class Test_base:

    @pytest.fixture(params=dataList())

    def test01(self, params):
        print("assert:%s：6" % params)
        assert params == 6

    def test02(self):
        print("ok")
        assert "a" == "a"

    def test03(self):
        print("这是1个用例")
        assert 3 == 4

    def test04(self):
        print("这是2个用例")
        assert 4 == 4

    def test05(self):
        print("这是3个用例")
        assert "a" == "b"

    def test06(self):
        print("这是4个用例")
        assert 3 == 4
