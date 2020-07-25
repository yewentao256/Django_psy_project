var login_vue = new Vue({
	el: '.middle',
	data: {
		username: '',
		password: ''
	},
	methods: {
		login: function() {
			if (this.username.length == 0 || this.password.length == 0) {
				alert('用户名或密码不能为空！');
				return;
			}
			var formdata = new FormData();
			formdata.append('username', this.username);
			formdata.append('password', this.password);
			postData('user/login/', formdata).then(res => {
				if (res.code != 1)
					alert(res.msg);
				else {
					setSessionCookie(res.data);
					window.location.href = 'index.html';
				}
			})
		}

	}
})
