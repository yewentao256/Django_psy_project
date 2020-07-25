#----------------------------------------
#Author:Peter Ye
#QQ:1624633892
#Emali:2018302110283@whu.edu.cn
#Date:2019-08-17
#----------------------------------------
import requests
import os 
import json

base_url = 'http://127.0.0.1:8000/'
#base_url = 'http://122.112.156.16:8000/'


register_url = base_url + 'user/register/'
register = {'username':'peter','password':'qwertyuiop','repassword':'qwertyuiop'}
# result = requests.post(register_url, data= register)

login_url = base_url + 'user/login/'
login = {'username':'peter','password':'qwertyuiop'}
# result = requests.post(login_url, data= login)




updatePass_url = base_url + 'user/updatePass/'
updatePass = {'password':'qwertyuiop', 'newpassword':'123', 'repassword':'123',
    'token':'w1EoR1oy9jtdp8U1jqhKbKk2qAxjV0BRAfDZUJWpAhmHFX8O5cyY4rb0qhqR1iIBNkPOweGCmQDVXBFB2qsJ5uZS'}
# result = requests.post(updatePass_url, data= updatePass)

editUserInfo_url = base_url + 'user/editUserInfo/'
editUserInfo = {'token':"w1EoR1oy9jtdp8U1jqhKbKk2qAxjV0BRAfDZUJWpAhmHFX8O5cyY4rb0qhqR1iIBNkPOweGCmQDVXBFB2qsJ5uZS",
    'sex':"1",'birthday':1590582394, 'user_nickname':'弯越红鱼',
    'user_email':'zhyanwentao@126.com', 'avatar':'files/avatar/default.jpg',
    'signature':'无', 'mobile':13850998888,'address':'武汉大学',}
# result = requests.post(editUserInfo_url, data= editUserInfo)


#获取用户信息
userinfo_url = base_url + 'user/getUserInfo/'
userinfo = {'token':'w1EoR1oy9jtdp8U1jqhKbKk2qAxjV0BRAfDZUJWpAhmHFX8O5cyY4rb0qhqR1iIBNkPOweGCmQDVXBFB2qsJ5uZS'}
# result = requests.post(userinfo_url, data=userinfo)

#验证用户
verifyUser_url = base_url + 'user/verifyUser/'
verifyUser = {'token':'w1EoR1oy9jtdp8U1jqhKbKk2qAxjV0BRAfDZUJWpAhmHFX8O5cyY4rb0qhqR1iIBNkPOweGCmQDVXBFB2qsJ5uZS',
    'name':'叶文涛', 'sex':1, 'mobile':13850998277, 'idcard':350725200003208888}
# result = requests.post(verifyUser_url, data=verifyUser)


#咨询师列表
consultantList_url = base_url + 'user/consultantList/'
consultantList = {'current_page':1}
# result = requests.get(consultantList_url, params=consultantList)

#问题列表
getTestQuestions_url = base_url + 'psytest/getTestQuestions/'
getTestQuestions = {'number':2}
# result = requests.post(getTestQuestions_url, data=getTestQuestions)


#上传测试答案并返回结果
uploadTest_url = base_url + 'psytest/uploadTest/'
uploadTest = {'data':str([
        {
            "topic_id": 1,      
            "tend":1,           
            "option_id":0       
        },
        {
            "topic_id": 2,      
            "tend":3,           
            "option_id":1       
        },
    ])}
# result = requests.post(uploadTest_url, data=uploadTest)


mood_message_url = base_url + 'psygarden/mood_message/'
mood_message = {'token':'w1EoR1oy9jtdp8U1jqhKbKk2qAxjV0BRAfDZUJWpAhmHFX8O5cyY4rb0qhqR1iIBNkPOweGCmQDVXBFB2qsJ5uZS',
    'mood':'0', 'content':"今天也是开心的一天", 'type':0, 'anonymity':0}
# result = requests.post(mood_message_url, data=mood_message)


comment_url = base_url + 'psygarden/comment/'
comment = {'token':'w1EoR1oy9jtdp8U1jqhKbKk2qAxjV0BRAfDZUJWpAhmHFX8O5cyY4rb0qhqR1iIBNkPOweGCmQDVXBFB2qsJ5uZS',
    'id':'2', 'content':"评论：今天也是开心的一天", 'anonymity':0}
# result = requests.post(comment_url, data=comment)

psygardenList_url = base_url + 'psygarden/psygardenList/'
psygardenList = {'token':'w1EoR1oy9jtdp8U1jqhKbKk2qAxjV0BRAfDZUJWpAhmHFX8O5cyY4rb0qhqR1iIBNkPOweGCmQDVXBFB2qsJ5uZS',
    'type':1, 'current_page':1}
result = requests.post(psygardenList_url, data=psygardenList)

print(type(result))
print(result)
try:
    print(result.json())
except:
    with open('asd.html', 'w', encoding='utf-8')as f:
        f.writelines(result.text)
        print('发现500错误，已转化为html')
        
