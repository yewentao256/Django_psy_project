var garden_vue = new Vue({
	el: '.middle',
	data: {
		username: '登录',
		avatar: 'img/user.png',
		type: 0,
		anonymity: 0,
		public_list: [],
		public_total: 0,
		private_list: [],
		private_total: 0,
		pri_current_page: 1,
		pub_current_page: 1,
		pri_total_page: 0,
		pub_total_page: 0,

		private_class: 'seled',
		public_class: 'selno',
		mood: '',
		msg_content: '',
		cmt_content: '',
		cmt_id: '',
		clock: {}
	},
	created() {
		var token = getCookieToken();
		if (token == null) {
			//window.location.href = 'login.html';
			return;
		}
		var formdata = new FormData();
		formdata.append('token', token)
		postData('user/getUserInfo/', formdata).then(res => {
			if (res.code == 1) {
				this.username = res.data.user_nickname;
				this.avatar = base_url + res.data.avatar;
				this.user_status = res.data.user_status;
			}
		})

		this.getMsgList(0, this.pri_current_page);
		this.getMsgList(1, this.pub_current_page);


		var atype = getURLParams(0)
		if (atype == null)
			this.type = 0;
		else
			this.type = atype;

	},
	mounted() {
		addEventListener('scroll', this.handleScroll)
	},
	methods: {
		getMsgList: function(type, current_page) {
			var atoken = getCookieToken();
			if (atoken == null) {
				return;
			}
			var formdata2 = new FormData();
			if (type == 0)
				formdata2.append('token', atoken);
			formdata2.append('current_page', current_page);
			formdata2.append('type', type);
			postData('psygarden/psygardenList/', formdata2).then(res => {
				if (res.code == 1) {
					var data = JSON.parse(res.data)
					if (type == 1) {
						for (i = 0; i < data.list.length; i++)
							this.public_list.push(data.list[i]);
						this.pub_total_page = data.total_page;
						this.public_total = data.total;
					} else {
						for (i = 0; i < data.list.length; i++)
							this.private_list.push(data.list[i]);
						this.pri_total_page = data.total_page;
						this.private_total = data.total;
					}

				}
			})
		},
		handleScroll() {
			var self = this
			if (this.clock) {
				clearTimeout(this.clock);
			}
			this.clock = setTimeout(function() {
				self.getMore()
			}, 100)
		},
		getMore: function() {
			let scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
			let windowHeight = document.documentElement.clientHeight || document.body.clientHeight;
			let scrollHeight = document.documentElement.scrollHeight || document.body.scrollHeight;
			if (scrollTop + windowHeight >= scrollHeight - 10) {
				if (this.type == 0) {
					if (this.pri_current_page >= this.pri_total_page)
						return
					this.pri_current_page++;
					this.getMsgList(0, this.pri_current_page);
				} else {
					if (this.pub_current_page >= this.pub_total_page)
						return
					this.pub_current_page++;
					this.getMsgList(1, this.pub_current_page);
				}

			}
		},

		toPrivate: function() {

			this.type = 0;
		},
		toPublic: function() {
			this.type = 1;
		},
		toggleAnonymity: function() {
			if (this.anonymity == 0)
				this.anonymity = 1;
			else
				this.anonymity = 0;
			console.log(this.anonymity)
		},
		publishMsg: function() {
			var token = getCookieToken();
			if (token == null)
				return;
			var formdata = new FormData();
			if (this.mood == '') {
				alert('请选择心情！');
				return;
			} else if (this.msg_content == '') {
				alert('请输入你的心语～');
				return;
			}
			var formdata = new FormData();
			if (this.type == 0)
				formdata.append('anonymity', 0);
			else
				formdata.append('anonymity', this.anonymity);
			formdata.append('mood', this.mood);
			formdata.append('content', this.msg_content);
			formdata.append('type', this.type);
			formdata.append('token', token);
			console.log(this.anonymity);
			postData('psygarden/mood_message/', formdata).then(res => {
				if (res.code == 1) {
					window.location.href = 'garden.html' + '?type=' + this.type;
				}
			})
		},
		publishCmt: function(e, id) {
			var str = e.currentTarget.parentNode.previousElementSibling.firstElementChild.nextElementSibling.value;
			var token = getCookieToken();
			if (token == null)
				return;
			var formdata = new FormData();
			formdata.append('token', token);
			formdata.append('id', id);
			formdata.append('anonymity', this.anonymity)
			formdata.append('content', str)
			postData('psygarden/comment/', formdata).then(res => {
				if (res.code == 1) {
					window.location.href = 'garden.html' + '?type=' + this.type;
				}
			})
		}

	},
	watch: {
		type(val) {
			if (val == 0) {
				this.anonymity = 0;
				this.private_class = 'seled';
				this.public_class = 'selno';
			} else {

				this.private_class = 'selno';
				this.public_class = 'seled';
			}
		}
	}
})
