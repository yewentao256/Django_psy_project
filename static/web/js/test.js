var test_vue = new Vue({
	el: '.middle',
	data: {
		questions: [],
		answers: []
	},
	created() {
		var formdata = new FormData();
		formdata.append('number', 10);
		postData('psytest/getTestQuestions/', formdata).then(res => {
			if (res.code == 1) {
				this.questions = res.data;

				for (i = 0; i < this.questions.length; i++)
					this.answers[i] = {
						"topic_id": this.questions[i].topic_id,
						"tend": this.questions[i].tend,
						"option_id": ''
					};
			}
		})
	},
	methods: {
		uploadTest() {


			for (i = 0; i < this.answers.length; i++) {
				if (this.answers[i].option_id == "") {
					alert('还有题目没做出选择！请仔细检查！')
					return;
				}
			}
			var str = JSON.stringify(this.answers)
			//console.log(str);
			var formdata = new FormData();
			formdata.append('data', str);
			postData('psytest/uploadTest/', formdata).then(res => {
				if (res.code == 1) {
					window.location.href = 'testResult.html';
				}
			})
		}
	}
})
