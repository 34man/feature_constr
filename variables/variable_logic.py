# ！/usr/bin/env/python
# coding: utf-8

"""
@File       :variable_logic.py
@Copyright  :sx
@Date       :2019/4/28
@Desc       :存储变量名和逻辑（变量名字组成的顺序）
"""


def get_logic(key):
    """
    获取变量命名规则
    :return:返回变量命名规则以及变量的分类
    """
    logic = {
        'order': ['perfix', 'cal_way', "object", "dur_time", "status", "total_size", "fee", "net_way", "start_time",
                  "total_time", "total_traffic", "business_name"],
        'class': {
            'perfix': ["net_1"],
            "cal_way": ["c", "m", "l", "a", "v", "s", "d"],
            "object": ["ts"],
            "dur_time": ['00', '1d', '3d', '7d', "1m", "2m", "3m", "4m", "6m", "ww", 'em'],
            "status": ["d", "e", "h"],
            'total_size': ['500t', '1000t', '1500t', '2000t', '3000t', '4000t'],
            "fee": ['1Y', '3Y', '5Y', '10Y', '50Y', '50YS'],
            "net_way": ['4G', '3G', '2G', 'aim'],
            "start_time": ['1', '2', '3', '4', '5'],
            "total_time": ['1/2h', '1h', '3/2h', '2h', '2hs'],
            "total_traffic": ['2mb', '4mb', '10mb', '10mbs'],
            "business_name": ['1', '2', '3', '4', '5']
        }
    }
    return logic.get(key)
