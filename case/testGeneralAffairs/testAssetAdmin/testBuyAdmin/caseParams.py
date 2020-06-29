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
            "enterstate": 0,
            "list": [
                {
                    "category": "物品类别",
                    "categoryid": 2,
                    "contract": "采购合同编号",
                    "cost": 8888.88,
                    "itemtype": "物品型号",
                    "name": "这是zp的物品-1",
                    "num": 1,
                    "owner": "-7077230525745151452",
                    "price": 3.21,
                    "supplier": "供应商",
                    "supplierid": 2,
                    "unit": "个",
                    "unitid": 1
                },
                {
                    "category": "物品类别",
                    "categoryid": 2,
                    "contract": "采购合同编号",
                    "cost": 8888.88,
                    "itemtype": "物品型号",
                    "name": "这是zp的物品-2",
                    "num": 1,
                    "owner": "-7077230525745151452",
                    "price": 3.21,
                    "supplier": "供应商",
                    "supplierid": 2,
                    "unit": "个",
                    "unitid": 1
                }
            ],
            "name": "zp手动测试",
            "purchaseno": "-5534420828292691492",
            "relationid": 0,
            "remark": "这是zptest的备注信息",
            "schoolid": 1,
            "sumcost": 999.99,
            "type": 0,
            "sumnum": 100,
            "estimatecost": 99999,
            "delivertime": "2020-06-30"
        }
    ]
    return params


def addcheckware():
    params = [
        {
            "assetstype": 1,
            "ctype": 0,
            "name": "zp测试验收入库-999",
            "pnum": 1,
            "position": "这是zp的临时存放地址",
            "purchaseno": "1324465464646",
            "quality": 2,
            "relationid": "-5527505149849549080",
            "remark": "这是zp的备注信息",
            "state": 1,
            "storetype": 1,
            "suggest": "这是zp的验证意见",
            "warehouseid": -8855096354382919000,
            "wareno": '917370683743488323',
            "sourcetype": 0
        }
    ]
    return params