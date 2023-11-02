function handleMessage(request) {
    data = "key="+request.key+"&page="+request.page;
    fetch("http://127.0.0.1:5000/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: data
    })
    .then(response => response.text())
    .then(responseText => {
        console.log("Response: " + responseText);
    })
    .catch(error => {
        console.error("Error: " + error);
    });
}

chrome.runtime.onMessage.addListener(handleMessage)