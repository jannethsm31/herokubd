function getAll(){
    var request = new XMLHttpRequest;
    request.open('GET', "https://8000-jannethsm31-herokubd-3uydt42hlvc.ws-us105.gitpod.io/contactos");
    request.send();

    request.onload = (e) => {
        const response = request.responseText;
        const json = JSON.parse(response);
        console.log("response" + json.response);
    };
};