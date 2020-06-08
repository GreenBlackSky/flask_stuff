let input = document.getElementById("input");
let output = document.getElementById("output");

function inputHandler() {
    let message = input.value;
    input.value = "";
    fetch(
        `${window.origin}/input`,
        {
            method: "POST",
            credentials: "include",
            headers: new Headers({"content-type": "application/json"}),
            cache: "no-cache",
            body: JSON.stringify({"message": message})
        }
    );
}

function messageListener(event) {
    let data = JSON.parse(event.data);
    output.value += '\n' + data.message;
}

function errorHandler(event) {
    alert("Failed to connect to event stream.");
}

function keyHandler(event) {
    if(event.key === 'Enter') {
        inputHandler();
    }
}

let source = new EventSource('/stream');
source.addEventListener('message', messageListener, false);
source.addEventListener('error', errorHandler, false);
