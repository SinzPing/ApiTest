"""
采购管理接口参数
author：郑平
"""


def addproapply():
    params = [
        {
            "agentuserid": "-9212958034144377285",
            "applyuserid": "-9148178383622877762",
            "departid": 99859,
            "enterstate": 1,
            "list": [
                {
                    "category": "物品类别",
                    "categoryid": 2,
                    "contract": "采购合同编号",
                    "cost": 100000,
                    "itemtype": "物品型号",
                    "name": "物品1",
                    "num": 1,
                    "owner": "-7077230525745151452",
                    "price": 3.21,
                    "supplier": "供应商",
                    "supplierid": 2,
                    "unit": "张",
                    "unitid": 1
                }
            ],
            "name": "桌子",
            "purchaseno": "-7077230575745151118",
            "relationid": "7077230575745151199",
            "remark": "备注",
            "schoolid": 1,
            "sumcost": 1000,
            "type": 1,
            "sumnum": 144,
            "estimatecost": 3233.2,
            "delivertime": "2020-06-23"
        }
    ]
    return params