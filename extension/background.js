function handleMessage(request) {
    alert(request.key);
    
    data = "key="+request.key+"&page="+request.page;
    //var xhr = new XMLHttpRequest();
    //xhr.onload = function() {
    //    alert(this.responseText);
    //}

    //xhr.open("POST","http://http://127.0.0.1:5000/",true);
    //xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
    //xhr.send(data);
}

chrome.runtime.onMessage.addListener(handleMessage)