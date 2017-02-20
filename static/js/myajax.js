 function change_nav(obj_url,method,data,sync) {
  var xmlHttpReg = null;
  var result={};
  console.log(sync);
  if (window.ActiveXObject) {
      xmlHttpReg = new ActiveXObject("Microsoft.XMLHTTP");
  } else if (window.XMLHttpRequest) {
      xmlHttpReg = new XMLHttpRequest();
  }
  if (xmlHttpReg != null){
        var url = obj_url;
        if(method == "get"){
            xmlHttpReg.open("get",url,false);
            xmlHttpReg.send()
        }else if(method == "post"){
            xmlHttpReg.open("post",url,false);
            xmlHttpReg.setRequestHeader("Content-type","application/x-www-form-urlencoded");
            xmlHttpReg.send(data)
        }
        xmlHttpReg.onreadystatechange = doResult;
        function doResult(){
            if (xmlHttpReg.readyState == 4) {
                if (xmlHttpReg.status == 200) {
                  var content =  xmlHttpReg.responseText;
                  var con = JSON.parse(content);
                  result = con;
          }
    }}
  }
  return result
}

function changeNav(url,type,data,async,success,error){
    //url 请求的地址
    //type 请求的类型 post get
    //data 请求的内容
    //beforeSend 在发送之前
    //async 是否异步
    //success ajax 请求成功之后返回的回调函数
    //error ajax 请求失败，发生错误之后返回的回调函数
    $.ajax(
        {
        url:url,
        type: type,
        data: data,
        beforeSend:function () {
            
        },
        async:async,
        success: success,
        error:error,
    }
    )
}