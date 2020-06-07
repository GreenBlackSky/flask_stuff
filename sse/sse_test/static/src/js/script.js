
function greetingsListener(event) {
    let data = JSON.parse(event.data);
    alert("The server says " + data.message);
}

function errorHandler(event) {
    alert("Failed to connect to event stream.");
}

let source = new EventSource('/stream');
source.addEventListener('messege', greetingsListener, false);
source.addEventListener('error', errorHandler, false);
