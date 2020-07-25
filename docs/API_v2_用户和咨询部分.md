**基础说明**
___
- 基础URL: "https://.."**暂无**
- 参数和返回均为**JSON**格式
- ***VERSION:1 ***
___

# 文件

## 文件上传

- url     
> /xinlizixun/file/upload_file

-   参数
```
    上传使用post方式提交 提交文件需要键值
    参数          说明
    file	 文件对象(FormData("file",file))
   
```

-  	返回示例
```json
  {
    "code": 1,
    "msg": "操作成功",
    "data": "http://.." //..返回文件在服务器的绝对地址
}
```



# 用户

## 用户登录


- 请求方式
> POST

- 参数
```json
{
    "username":"test",      //..用户名
    "password":"123456"     //..密码
}
```

- 返回示例
```json
{
    "code": 1,
    "msg": "登录成功!",
    "data": "0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5"  //..token
}
```



## 用户注册

- URL
> /xinlizixun/login/register 

- 请求方式
> POST

- 参数
```json
{
    "username":"jack",      //..注册手机号
    "password":"123456",    //..密码
    "repassword":"123456"   //..确认密码
}
```

- 返回示例
```json
{
    "code": 1,
    "msg": "注册成功!"
}
```

## 修改密码

- URL
> /xinlizixun/login/updatePass

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5",
    "password":"123456",        //..旧密码
    "newpassword":"123456",     //..新密码
    "repassword":"123456",      //..重复密码
    }   
```

- 返回
```json
{
    "code": 1,
    "msg": "密码修改成功！"
}
```


## 获取用户资料

- URL
> /xinlizixun/user/getUserInfo

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5"
}
```

- 返回
```json
{
    "code": 1,
    "msg": "查询成功",
    "data": {
        "id": 1,                               //..用户ID
        "sex": 0,                              //..性别：0:保密,1:男,2:女,
        "birthday": 1588165052,                //..生日：时间戳
        "create_time": 1588165052,              //..创号时间
        "user_nickname": "小王",                 //..昵称
        "user_email": "123456789@qq.com",       //..邮箱
        "avatar": "http://****/******/***.jpg", //..头像服务器中绝对路径
        "signature": "我是*****",               //..个性签名
        "mobile": 13200000000,                //..电话号码
        "address":"湖北省武汉市****",              //..家庭住址
        "user_status":0                         //..用户状态：0:未验证,1:已验证普通用户,2:咨询师
    }
}
```


## 编辑用户资料

- URL
> /xinlizixun/user/editUserInfo

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5",
    "sex": 0,                              //..性别：0:保密,1:男,2:女,
    "birthday": 1588165052,                //..生日：时间戳
    "user_nickname": "小王",                 //..昵称
    "user_email": "123456789@qq.com",       //..邮箱
    "avatar": "http://****/******/***.jpg", //..头像服务器中绝对路径
    "signature": "我是*****",               //..个性签名
    "mobile": 13200000000,                //..电话号码
    "address":"湖北省武汉市****"              //..家庭住址
}
```

- 返回
```json
{
    "code": 1,
    "msg": "操作成功"
}
```

##	用户验证

- URL
> /xinlizixun/user/verifyUser

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5",
    "name":"王小明",                                 //..真实姓名
    "sex":0,                                        //..性别:0:男,1:女
    "mobile":13200000000,                           //..手机号码
    "idcard":440102198001021230,                    //..身份证号码
    "idcard_img1":"http://****/******/***.jpg",     //..身份证正面(国徽面)
    "idcard_img2":"http://****/******/***.jpg"      //..身份证反面(人像面)
}
```

- 返回
```json
{
    "code": 1,
    "msg": "操作成功"
}
```

# 三方保密协定

##	获取三方保密协定

- URL
> /xinlizixun/agreement/getAgreement

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5"
}
```

- 返回
```json
{
    "code": 1,
    "msg": "",
    "data":{
        "content":""    //..保密协议内容
    }
}
```

##	签订三方保密协定(普通用户和咨询师)

- URL
> /xinlizixun/agreement/signAgreement

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5"
}
```

- 返回
```json
{
    "code": 1,
    "msg": ""
}
```

# 心理测试

##	提示心理测试(普通用户和咨询师)

- URL
> /xinlizixun/psychologicalTest/remindTest

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5"
}
```

- 返回
```json
{
    "code": 1,
    "msg": "",
    "data":{
        "needRemind":0,             //..是否提醒做心理测试:0:否, 1:是
        "status":1,                 //..用户类型:0:普通用户, 1:咨询师
        "list":[                    //..需要提醒的患者列表
            {
                "patient_name":"王小明"
            },
            {
                "patient_name":"李小红"
            }
        ]
    }
}
```


## 心理测试题目

- URL
> /xinlizixun/psychologicalTest/getTestQuestions

- 请求方式
> GET

- 参数
```
无
```

- 返回
```json
{
    "code": 1,
    "msg": "操作成功",
    "data":{
        "question_quantity":40,             //..题目数量
        "question_list":[
            {
                "topic_id": 1,                  //..题目id
                "topic": "XXXXXX",              //..题目
                "options":[                     //..选项
                    {
                        "option_id":1,         //..选项id
                        "content":"XX"         //..选项内容
                    },
                    {
                        "option_id":1,         //..选项id
                        "content":"XX"         //..选项内容
                    },
                    {
                        "option_id":1,         //..选项id
                        "content":"XX"         //..选项内容
                    },
                    {
                        "option_id":1,         //..选项id
                        "content":"XX"         //..选项内容
                    }
                ]
                
            },
            {
                "topic_id": 2,              //..题目id
                "topic": "XXXXXX",          //..题目
                "options":[]                //..选项
                
            }
        ]
    }
}
```

## 上传心理测试

- URL
> /xinlizixun/psychologicalTest/uploadTest

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5",
    "data":[
        {
            "topic_id": 1,      //..题目id
            "option_id":1       //..选项id
        },
        {
            "topic_id": 2,      //..题目id
            "option_id":3       //..选项id
        },
    ]
}
```

- 返回
```json
{
    "code": 1,
    "msg": "操作成功",
}
```

## 获取心理测试结果

- URL
> /xinlizixun/psychologicalTest/getTestResult

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5"
}
```

- 返回
```json
{
    "code": 1,
    "msg": "操作成功",
    "data":{
        "content":"",           //..测试结果内容
        "test_time":1582700606  //..测试时间
    }
}
```

# 咨询


## 推荐咨询师列表

- URL
> /xinlizixun/consultation/consultantList

- 请求方式
> GET

- 参数
```json
{
    "current_page":1,   //..当前访问第几页
}
```

- 返回
```json
{
    "code": 1,
    "msg":"",
    "data": {
        "total":2,              //..一共有多少项
        "per_page": 15,         //..每页最多多少项
        "current_page": 1,      //..当前第几页
        "total_page": 1,        //..一共多少页
        "list":[
            {
                "id": 1,
                "name":"张三教授",
                "grade":"二级心理咨询师",           //..咨询师等级
                "address":"北京市",                //..地址
                "mobile":13200000000,            //..电话
                "expertise":"善于处理青少年问题……",  //..专长
                "training":"中科院心理所医学与心理咨询治疗专业硕士研究生",  //..专业培训
                "avatar":"http://****/******/***.jpg", //..绝对路径
                "qq":"123456"                     //..QQ
            },
            {
                "id": 2,
                "name":"张三教授",
                "grade":"二级心理咨询师",           //..咨询师等级
                "address":"北京市",                //..地址
                "mobile":13200000000,             //..电话
                "expertise":"善于处理青少年问题……",  //..专长
                "training":"中科院心理所医学与心理咨询治疗专业硕士研究生",  //..专业培训
                "avatar":"http://****/******/***.jpg", //..绝对路径
                "qq":"123456"                     //..QQ
            }
        ]
    }
}
```

## 预约咨询师

- URL
> /xinlizixun/consultation/makeAppointment

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5",
    "id":1,                         //..咨询师id
    "appointment_time":1582700606,  //..预约时间
    "mobile":13200000000            //..预留电话

}
```

- 返回成功示例
```json
{
    "code": 1,
    "msg":""
}
```

## 删除预约

- URL
> /xinlizixun/consultation/deleteAppointment

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5",
    "id":1,              //..预约id
}
```

- 返回成功示例
```json
{
    "code": 1,
    "msg":""
}
```

## 获取预约

- URL
> /xinlizixun/consultation/getAppointment

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5",
    "id":1,              //..预约id
}
```

- 返回成功示例
```json
{
    "code": 1,
    "msg":"",
    "data":{
        "id":1,                             //..预约id
        "appointment_time":1582700606,      //..预约时间
        "name":"王小明",                     //..对方名字
        "mobile":13200000000                //..对方联系方式
    }
}
```

## 修改预约

- URL
> /xinlizixun/consultation/updateAppointment

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5",
    "id":1,                         //..预约id
    "appointment_time":1582700606,  //..预约时间
    "mobile":13200000000            //..预留电话
}
```

- 返回成功示例
```json
{
    "code": 1,
    "msg":""
}
```


## 我的预约列表(普通用户和咨询师)

- URL
> /xinlizixun/consultation/appointmentList

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5",
    "current_page":1,   //..当前访问第几页

}
```

- 返回成功示例
```json
{
    "code": 1,
    "msg":"",
    "data": {
        "total":2,              //..一共有多少项
        "per_page": 15,         //..每页最多多少项
        "current_page": 1,      //..当前第几页
        "total_page": 1,        //..一共多少页
        "list":[
            {
                "id":1,                             //..预约id
                "appointment_time":1582700606,      //..预约时间
                "name":"王小明",                     //..对方名字
                "mobile":13200000000                //..对方联系方式
            },
            {
                "id":2,                             //..预约id
                "appointment_time":1582700606,      //..预约时间
                "name":"王小明",                     //..对方名字
                "mobile":13200000000                //..对方联系方式
            }
        ]
    }
}
```

## 我的咨询师列表

- URL
> /xinlizixun/consultation/myConsultantList

- 请求方式
> GET

- 参数
```json
{
    "current_page":1,   //..当前访问第几页
}
```

- 返回
```json
{
    "code": 1,
    "msg":"",
    "data": {
        "total":1,              //..一共有多少项
        "per_page": 15,         //..每页最多多少项
        "current_page": 1,      //..当前第几页
        "total_page": 1,        //..一共多少页
        "list":[
            {
                "id": 1,
                "name":"张三教授",
                "grade":"二级心理咨询师",           //..咨询师等级
                "address":"北京市",                //..地址
                "mobile":13200000000,            //..电话
                "expertise":"善于处理青少年问题……",  //..专长
                "training":"中科院心理所医学与心理咨询治疗专业硕士研究生",  //..专业培训
                "avatar":"http://****/******/***.jpg", //..绝对路径
                "qq":"123456",                     //..QQ
                "rehabilitation_id":1            //..康复计划id
            }
        ]
    }
}
```


# 患者

## 我的患者列表

- URL
> /xinlizixun/patient/myPatientList

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5",
    "current_page":1,   //..当前访问第几页
}
```

- 返回
```json
{
    "code": 1,
    "msg":"",
    "data": {
        "total":1,              //..一共有多少项
        "per_page": 15,         //..每页最多多少项
        "current_page": 1,      //..当前第几页
        "total_page": 1,        //..一共多少页
        "list":[
            {
                "id": 1,                         //..患者用户id
                "name":"王小明",
                "sex": 0,                        //..性别：0:保密,1:男,2:女,
                "nation":"汉族",                  //..民族
                "birthday":1582700606,           //..出生日期
                "archive_id":1,                  //..心理档案id
                "rehabilitation_id":1            //..康复计划id
            }
        ]
    }
}
```



# 心理档案

## 心理档案详情

- URL
> /xinlizixun/archive/archiveDetails

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5",
    "id":1,   //..心里档案id
}
```

- 返回
```json
{
    "code": 1,
    "msg":"",
    "data": {
        "id": 1,                         //..心理档案id
        "name":"王小明",
        "sex": 0,                        //..性别：0:保密,1:男,2:女,
        "nation":"汉族",                  //..民族
        "birthday":1582700606,           //..出生日期
        "health":"健康",                  //..健康状况
        "history":"无",                  //..个人病史
        "defect":"失明",                 //..生理缺陷
        "description":"头疼",            //..主要症状描述
        "start_time":"2020年春",         //..开始时间
        "duration":"三个月",               //..持续时间
        "othercontent":"其他内容"         //..其他

    }
}
```

## 修改心理档案

- URL
> /xinlizixun/archive/updateArchive

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5",
    "id":1,   //..档案id
    "name":"王小明",
    "sex": 0,                        //..性别：0:保密,1:男,2:女,
    "nation":"汉族",                  //..民族
    "birthday":1582700606,           //..出生日期
    "health":"健康",                  //..健康状况
    "history":"无",                  //..个人病史
    "defect":"失明",                 //..生理缺陷
    "description":"头疼",            //..主要症状描述
    "start_time":"2020年春",         //..开始时间
    "duration":"三个月",               //..持续时间
    "othercontent":"其他内容"         //..其他
}
```

- 返回
```json
{
    "code": 1,
    "msg":""
}
```

# 康复计划

## 康复计划详情

- URL
> /xinlizixun/rehabilitation/rehabilitationDetails

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5",
    "id":1,   //..康复计划id
}
```

- 返回
```json
{
    "code": 1,
    "msg":"",
    "data": {
        "id": 1,                           //..康复计划id
        "total_duration":"",                //..总时长
        "content":"治疗阶段数量、每阶段时长、每阶段康复计划。",          //..计划内容
    }
}
```


## 修改康复计划

- URL
> /xinlizixun/rehabilitation/updateRehabilitation

- 请求方式
> POST

- 参数
```json
{
    "token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5",
    "id":1,   //..康复计划id
    "total_duration":"",                //..总时长
    "content":"总时长、治疗阶段数量、每阶段时长、每阶段康复计划。",          //..计划内容
}
```

- 返回
```json
{
    "code": 1,
    "msg":""
}
```
