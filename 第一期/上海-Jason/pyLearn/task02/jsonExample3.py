# _*_ coding : utf-8 _*_
__author__ = "Jason"

import json

if __name__ == "__main__":
    print("Json高级示例")

    json_demo = '''
        {
        "biz_content":{
        "name":"中国平安控股金融公司",
        "alias_name":"49Online公司",
        "service_phone":"0571-82338668",
        "mcc":"1520",
        "bank_pid":"2088001969784501",
        "unique_id_by_bank":"2018201801161101",
        "isv_pid":"2088301248032348",
        "unique_id_by_isv":"2017201801161101",
        "business_license":"100000011234563",
        "business_license_type":"NATIONAL_LEGAL",
        "contact_info":[{
            "name":"诸葛孔明",
            "phone":"0571-85022088",
            "mobile":"15012341234",
            "email":"123@163.com",
            "tag":["06"],
            "type":"LEGAL_PERSON",
            "id_card_no":"61011219900602128X"}],
        "address_info":[{
            "city_code":"371000",
            "district_code":"371002",
            "address":"万塘路18号黄龙时代广场B座",
            "province_code":"370000",
            "longitude":"120.760001",
            "latitude":"60.270001",
            "type":"BUSINESS_ADDRESS"}],
        "bankcard_info":[{
            "card_no":"6228480402637874213",
            "card_name":"诸葛孔明"}],
        "site_info":[{
            "site_type":"01",
            "site_url":"www.test.com",
            "site_name":"test网站",
            "account":"测试账号",
            "password":"测试密码"}],
        "pay_code_info":["https://apires.test.alipay.com"],
        "logon_id":["12340@hlbtest.com"],
        "sign_bank_time":"2017-03-03 21:12:17",
        "memo":"备注信息"
            }
          }
    '''
    print(type(json_demo))#<class 'str'>

    #将JSON对象转换为字典
    json_dict = json.loads(json_demo)
    print(type(json_dict),json_dict)
    print('-'*100)

    #遍历字典
    for (k,v) in json_dict.items():
        #输出第一层级
        print(type(v),k,":",v)
        print('-'*50)

        #输出第二层级
        for (k1,v1) in v.items():
            print(type(v1),k1,":",v1)

            if type(v1) == list:
                for list_data in v1:
                    print(type(list_data),list_data)