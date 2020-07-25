var top_vue = new Vue({
	el: '.top',
	data: {
		username: '登录',
		avatar: 'img/user.png',
		user_status: '0',
		user_url:'login.html'
	},
	created() {
		var token = getCookieToken();
		if (token == null)
			return;
		var formdata = new FormData();
		formdata.append('token', token)
		postData('user/getUserInfo/', formdata).then(res => {
			if (res.code == 1) {
				this.username = res.data.user_nickname;
				this.avatar = base_url + res.data.avatar;
				this.user_status = res.data.user_status;
				this.user_url=''
			}
		})
	}
})
