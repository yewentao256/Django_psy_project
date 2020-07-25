var consultant_vue = new Vue({
	el: '.middle',
	data: {
		current_page: '1',
		total_page: '0',
		consultant: [],
		clock: {}
	},
	created() {
		this.getList(this.current_page)
	},
	mounted() {
		addEventListener('scroll', this.handleScroll)
	},
	methods: {
		getList: function(page) {
			getData('user/consultantList/', {
				'current_page': page
			}).then(res => {
				if (res.code != 1)
					return;
				var data = JSON.parse(res.data)
				for (i = 0; i < data.list.length; i++) {
					this.consultant.push(data.list[i]);
				}
				this.total_page = data.total_page;
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
				if (this.current_page >= this.total_page)
					return
				console.log(scrollHeight)
				this.current_page++;
				this.getList(this.current_page)
			}
		}
	}
})
