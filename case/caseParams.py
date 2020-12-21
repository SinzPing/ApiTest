"""
接口参数demo
author：郑平
"""

import random

#  case里的test方法会遍历列表的参数，列表中有几个字典就跑几次


def demo():
    params = [
        {
            'param1': '',
            'param2': ''
        },
        {
            'param1': '',
            'param2': ''
        },
        {
            'param1': '',
            'param2': ''
        },
        {
            'param1': '',
            'param2': ''
        }
    ]
    return params


def abnormal():
    params = [
        {
            "studentId": 2812336013313,
            "userId": 2656528105473,
            "inspectionDate": "2020-12-19",
            "type": 1,
            "img": "",
            "isTemperature": 1,
            "temperature": 37.3,
            "isAbnormal": 0,
            "treatment": 3,
            "other": "挂了",
            "otherSymptom": "heiha ",
            "infectiousDisease": 0,
            "isDisease": 0,
            "diseaseName": "麻疹",
            "dictItem": [
                {
                    "dictId": 3,
                    "itemText": "麻疹",
                    "itemValue": 6
                },
                {
                    "dictId": 3,
                    "itemText": "麻风病",
                    "itemValue": 12
                }
            ]
        },
    ]
    return params


def normal():
    params = [
        {
            'isAbnormal': 1,
            'type': 0,
            'inspectionDates': '2020-12-15',
            'isTemperature': 1,
            'temperature': 37.3
        }
    ]
    return params


def insert_data():
    params = [
        {
            'infoTopic': 'API信息标题%s' % (random.randint(0, 999)),
            'infoClassId': 2648321949697,
            'receiveOrgId': 2633063071746,
            'information': 'zheshi neirong zheshi neirong zheshi neirong zheshi neirong '
        }
    ]
    return params


def insert_class():
    params = [
        {
            'className': "托班一班",
            'enterSchoolYear': "2020",
            'gradeId': 5
        },
        {
            'className': "小班一班",
            'enterSchoolYear': "2020",
            'gradeId': 6
        },
        {
            'className': "中班一班",
            'enterSchoolYear': "2020",
            'gradeId': 7
        },
        {
            'className': "大班一班",
            'enterSchoolYear': "2020",
            'gradeId': 8
        },
        {
            'className': "学前班一班",
            'enterSchoolYear': "2020",
            'gradeId': 9
        },
        {
            'className': "学前班二班",
            'enterSchoolYear': "2020",
            'gradeId': 9
        },
        {
            'className': "托班二班",
            'enterSchoolYear': "2020",
            'gradeId': 5
        },
    ]
    return params


def insert_students():
    params = [
        {
            {
                'classId': 1,
                'gradeId': 5,
                'sex': 1,
                'studentName': 'API添加学生%s' % random.randint(0, 999),
                'userInfo': [
                    {
                        'mobile': "1921155%s" % random.randint(1000, 9999),
                        'password': "123456"
                    }
                ]
            },
            {
                'classId': 1,
                'gradeId': 6,
                'sex': 1,
                'studentName': 'API添加学生%s' % random.randint(0, 999),
                'userInfo': [
                    {
                        'mobile': "1921155%s" % random.randint(1000, 9999),
                        'password': "123456"
                    }
                ]
            },
            {
                'classId': 1,
                'gradeId': 7,
                'sex': 1,
                'studentName': 'API添加学生%s' % random.randint(0, 999),
                'userInfo': [
                    {
                        'mobile': "1921155%s" % random.randint(1000, 9999),
                        'password': "123456"
                    }
                ]
            },
            {
                'classId': 1,
                'gradeId': 8,
                'sex': 1,
                'studentName': 'API添加学生%s' % random.randint(0, 999),
                'userInfo': [
                    {
                        'mobile': "1921155%s" % random.randint(1000, 9999),
                        'password': "123456"
                    }
                ]
            },
            {
                'classId': 1,
                'gradeId': 9,
                'sex': 1,
                'studentName': 'API添加学生%s' % random.randint(0, 999),
                'userInfo': [
                    {
                        'mobile': "1921155%s" % random.randint(1000, 9999),
                        'password': "123456"
                    }
                ]
            },
            {
                'classId': 1,
                'gradeId': 9,
                'sex': 1,
                'studentName': 'API添加学生%s' % random.randint(0, 999),
                'userInfo': [
                    {
                        'mobile': "1921155%s" % random.randint(1000, 9999),
                        'password': "123456"
                    }
                ]
            },
            {
                'classId': 1,
                'gradeId': 5,
                'sex': 1,
                'studentName': 'API添加学生%s' % random.randint(0, 999),
                'userInfo': [
                    {
                        'mobile': "1921155%s" % random.randint(1000, 9999),
                        'password': "123456"
                    }
                ]
            },
        }
    ]
    return params
