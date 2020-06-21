'''
考核方式配置-用例参数
author: 郑平
'''


def change_cycle():
    params = [
        {
            'id': 1,
            'cycletype': 1
        },
        {
            'id': 1,
            'cycletype': 2
        },
        {
            'id': 1,
            'cycletype': 12
        },
    ]
    return params


def way_enable():
    params = [
        {
            'id': 1,
            'isenable': 1
        },
        {
            'id': 1,
            'isenable': 0
        }
    ]
    return params

