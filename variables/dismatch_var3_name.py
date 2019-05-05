# ！/usr/bin/env/python
# coding: utf-8

"""
@File       :dismatch_var_name.py
@auth       :sx
@Date       :2019/4/30
@Desc       : 拆分变量名的方法存放在这里,第一批第二批拆分的方法在variable.py中,不动了这里是第三批的方法
"""


def dismatch_var3_name(name):
    """
    参数是第三批变量的变量名,这个方法把变量名拆分成可以处理的{name:[时间维度, 上网方式, top几, 分组对象, 列]}
    :param name:
    :return:
    """
    import re
    group = re.search('^top_([3m|1m]*)([4G|3G|2G]*)([top5|top10|top15]*)([1-6])(.*)$', name)
    if group:
        dur_time = group.group(1)
        net_way = group.group(2)
        top = group.group(3)[3:]
        start_time = group.group(4)
        column = group.group(5)
    return {name: [dur_time, net_way, top, start_time, column]}
