import pytest
from inventory import Inventory


def test_low_stock_items_all_above_threshold():
    """กรณีที่ 1: สินค้าทุกรายการมีจำนวนมากกว่า threshold -> คืน list ว่าง"""
    inv = Inventory()
    inv.add_item("Apple", 10, 15.0)
    inv.add_item("Banana", 20, 10.0)
    assert inv.low_stock_items(5) == []


def test_low_stock_items_exact_threshold():
    """กรณีที่ 2: มีสินค้าที่จำนวนเท่ากับ threshold พอดี -> ต้องถูกนับรวมด้วย"""
    inv = Inventory()
    inv.add_item("Apple", 5, 15.0)
    inv.add_item("Banana", 10, 10.0)
    assert inv.low_stock_items(5) == ["Apple"]


def test_low_stock_items_multiple_items_sorted_by_name():
    """กรณีที่ 3: มีสินค้าเข้าเกณฑ์หลายรายการ -> ผลลัพธ์เรียงตามชื่อ ไม่ใช่ตามลำดับที่เพิ่ม"""
    inv = Inventory()
    inv.add_item("Zebra", 2, 50.0)
    inv.add_item("Apple", 3, 15.0)
    inv.add_item("Mango", 1, 25.0)
    inv.add_item("Orange", 10, 20.0)  # รายการนี้เกิน threshold ไม่ควรติดมา
    assert inv.low_stock_items(5) == ["Apple", "Mango", "Zebra"]


def test_low_stock_items_empty_inventory():
    """กรณีที่ 4: คลังว่าง -> คืน list ว่าง ไม่ใช่ error"""
    inv = Inventory()
    assert inv.low_stock_items(10) == []


def test_low_stock_items_threshold_zero():
    """กรณีที่ 5: threshold เป็น 0 -> คืนเฉพาะสินค้าที่เหลือ 0"""
    inv = Inventory()
    inv.add_item("ZeroItem", 0, 10.0)
    inv.add_item("SomeItem", 1, 10.0)
    assert inv.low_stock_items(0) == ["ZeroItem"]


def test_low_stock_items_threshold_negative():
    """กรณีที่ 6: threshold ติดลบ -> คืน list ว่าง เนื่องจากจำนวนสินค้าไม่สามารถติดลบได้"""
    inv = Inventory()
    inv.add_item("ZeroItem", 0, 10.0)
    inv.add_item("SomeItem", 5, 10.0)
    assert inv.low_stock_items(-1) == []
