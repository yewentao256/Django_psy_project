var register_vue = new Vue({
	el: '.content',
	data: {
		username: '',
		password: '',
		repassword: ''
	},
	methods: {
		register: function() {
			if (this.username.length < 6 || this.username.length > 24) {
				alert('用户名错误！');
				return;
			}
			if (this.password.length < 6 || this.password.length > 24) {
				alert('密码长度不正确！');
				return;
			}
			if (this.repassword != this.password) {
				alert('确认密码和密码不一致！请重新输入！');
				return;
			}
			var formdata = new FormData()
			formdata.append("username", this.username)
			formdata.append("password", this.password)
			formdata.append("repassword", this.repassword)
			postData('user/register/', formdata).then(res => {
				if (res.code != 1)
					alert(res.msg);
				else {
					alert('注册成功！请登录');
					window.location.href = 'login.html';
				}
			})
		}
	}
})
