function check() {

		var psw = ""

		while ( btoa(psw) != "Z2hxcw==") { //设置密码

			psw = prompt("口令")	
			if(psw){ 
				//点击的是“确定” 
				//继续循环判断
				continue;		
			}else if(psw === ""){
				//输入为空 
				//继续循环判断
				continue;		
			}else{ 
				//点击的是“取消” 
				return false;
			}

		}
		return psw;

}

//jq支持监听所有的ajax请求
$( document ).ajaxSend(function( event, jqxhr, settings ) {
	// alert(settings.url);
	// 检测“/blog/letter” 调用loop加访问控制
	if(settings.url.indexOf('/blog/letter') != -1){
		var ret = check();
		if (!ret) {
			jqxhr.abort();  //点击取消则终止跳转
		}

	}
  
});
// //#锚点变化的监听器，不支持整个url变化的检测
// if( ('onhashchange' in window) && ((typeof document.documentMode==='undefined') || document.documentMode==8)) {
//     // 浏览器支持onhashchange事件
//     window.onhashchange = check;  // TODO，对应新的hash执行的操作函数
// } else {
//     // 不支持则用定时器检测的办法
//     setInterval(function() {
//         // 检测hash值或其中某一段是否更改的函数， 在低版本的iE浏览器中通过window.location.hash取出的指和其它的浏览器不同，要注意
//         var ischanged = isHashChanged();
//         if(ischanged) {
//             check();  // TODO，对应新的hash执行的操作函数
//             console.log('not support onhashchange; check executed')
//         }
//     }, 150);
// }



