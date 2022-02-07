import pytest
import allure


class TestAllure(object):
    @allure.story("加入购物车")
    def test_add_goods_cart(self):
        login("crisimple", "123456")

        with allure.step("浏览商品"):
            allure.attach("商品1", "C")
            allure.attach("商品2", "C")

        with allure.step("加入商品"):
            allure.attach("商品1", 2)
            allure.attach("商品2", 3)

        with allure.step("校验商品"):
            allure.attach("商品1加入成功", "共2个")
            allure.attach("商品2加入失败", "共0个")

    @allure.story("继续购物")
    def test_continue_shopping_cart(self):
        login("crisimple", "123456")
        allure.attach("商品3", 4)
        print("继续购物成功")

    @allure.story("减少商品失败")
    def test_edit_shopping_cart(self):
        login("crisimple", "123456")
        print()

    @pytest.mark.skip(reason="删除购物车不执行")
    @allure.story("删除购物车")
    def test_delete_shopping_cart(self):
        login("crisimple", "123456")
        print()


def login(user, passwd):
    if user == "crisimple" and passwd == "123456":
        print(user, passwd)
        print("登录成功")
    else:
        print(user, passwd)
        print("登录失败， 请重新尝试")

