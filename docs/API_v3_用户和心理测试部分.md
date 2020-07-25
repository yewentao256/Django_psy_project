**基础说明**
___
- 基础URL: "https://.."**暂无**
- 参数和返回均为**JSON**格式
- ***VERSION:1 ***

- baseurl：http://122.112.156.16:8000/
___
# 文件

## 文件上传

- url     
> /content/upload_file/

-   参数
```json
   {
    "file":file,      //..文件，文件名用户传什么就是什么即可
    "type":"avartar",    //..头像
}
```

-  	返回示例
```json
  {
    "code": 1,
    "msg": "操作成功",
    "data": "files/avatar/default.jpg" // 前端使用加一个baseurl即可，传进后端时不用改这个字段
}
```

# 用户

## 用户登录

- URL
> /user/login/

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
> /user/register/

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
> /user/updatePass/

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
> /user/getUserInfo/

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
> /user/editUserInfo/

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
    "avatar": "http://****/******/***.jpg", //..头像服务器中绝对路径（如果用户没有更改头像则传之前用户的avatar值即可。
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
> /user/verifyUser/

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
}
```

- 返回
```json
{
    "code": 1,
    "msg": "操作成功"
}
```



# 心理测试




## 心理测试题目

- URL
> /psytest/getTestQuestions/

- 请求方式
> POST

- 参数
```json
{
    "number":10,  // 题目数量
}
```

- 返回
```json
{
    "code": 1,
    "msg": "操作成功",
    "data":{
        "question_list":[
            {
                "topic_id": 1,                  //..题目id
                "topic": "XXXXXX",              //..题目
                "tend":0,   //性格倾向，前端记录并返回即可
                "options":[                     //..选项
                    {
                        "option_id":0,         //..选项id
                        "content":"XX"         //..选项内容
                    },
                    {
                        "option_id":1,         //..选项id
                        "content":"XX"         //..选项内容
                    },
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
> /psytest/uploadTest/

- 请求方式
> POST

- 参数
```json
{
    //"token":"0fb995ccbbd4cfe9cfafe0a734086f8234db808f417a310af5f492393a71adb5",
    "data":[
        {
            "topic_id": 1,      //..题目id
            "tend":1,           //性格倾向
            "option_id":0       //..选项id
        },
        {
            "topic_id": 2,      //..题目id
            "tend":3,           //性格倾向
            "option_id":1       //..选项id
        },
    ]  //注意，传进一整个字符串
}
```

- 返回
```json
{
    "code": 1,
    "msg": "操作成功",
    "result": {
        "内向/外向": -3,
        "实感/直觉": 2,
        "思考/情感": 4,
        "判断/知觉": -1
        }   //判别分数
}
```



# 咨询


## 推荐咨询师列表

- URL
> /user/consultantList/

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

