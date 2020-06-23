"""
自定义分类-用例参数
author：郑平
"""


def insert():
    params = [
        {
            'name': 'api_test',
            'state': 0,
            'parentId': ''
        },
        {
            'name': '',
            'state': 1,
            'parentId': ''
        }
    ]
    return params


def delete():
    params = [
        {
            'id': '1'
        }
    ]
    return params


def search():
    params = [
        {
            'page': 1,
            'size': 20
        }
    ]
    return params


def modify():
    params = [
        {

        }
    ]
    return params

