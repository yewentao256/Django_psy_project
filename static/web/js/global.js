var base_url = "http://122.112.156.16:8000/";

function postData(url, params) {
	var complete_url = base_url + url;
	return new Promise((resolve, reject) => {
		axios.post(complete_url, params).then(res => {
			resolve(res.data);
		}).catch(err => {
			reject(err.data);
		})
	});
}

function getData(url, param) {
	var complete_url = base_url + url;
	return new Promise((resolve, reject) => {
		axios.get(complete_url, {params:param}).then(res => {
			resolve(res.data);
		}).catch(err => {
			reject(err.data);
		})
	});
}

function setSessionCookie(token){
	window.document.cookie = "token" + "=" + token + ";path=/;";
}

function setLongTimeCookie(token){
	var d = new Date;
	d.setTime(d.getTime() + 1000*60*60*24*7);
	window.document.cookie = "token_web" + "=" + token + ";path=/;expires=" + d.toGMTString();
}

function getCookieToken(){
	return document.cookie.split(';')[0].split('=')[1];
}

function getTime(date) {
	var time = new Date(date * 1000); //时间戳为10位需*1000，时间戳为13位的话不需乘1000
	var y = time.getFullYear();
	var m = time.getMonth() < 9 ? '0' + (time.getMonth() + 1) : time.getMonth() + 1;
	var d = time.getDate() < 10 ? '0' + time.getDate() : time.getDate();
	var h = time.getHours() < 10 ? '0' + time.getHours() : time.getHours();
	var mm = time.getMinutes() < 10 ? '0' + time.getMinutes() : time.getMinutes();
	var s = time.getSeconds() < 10 ? '0' + time.getSeconds() : time.getSeconds();
	var timedate = y + '-' + m + '-' + d + ' ' + h + ':' + mm + ':' + s;
	return timedate;
}

function getURLParams(paramNumber){
	var url=location.search;
	if(url.indexOf('?')!=-1){
		var params=url.split('?')[1];
		var param=params.split('&')[paramNumber];
		return param.split('=')[1];
	}
}