function submit_numbers() {

    let num_1 = document.getElementById("num1").value;
    let num_2 = document.getElementById("num2").value;

    let entry = {
        num1: num_1,
        num2: num_2
    };

    let response = await fetch(
        `${window.origin}/`,
        {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(entry),
            cache: "no-cache",
            headers: new Headers({"content-type": "application/json"})
        }
    );

    if(response.ok) {
        let result = await response.json()['result'];
        alert(result);
    else {
        alert('HTTP error ' + response.status;
    }

};
