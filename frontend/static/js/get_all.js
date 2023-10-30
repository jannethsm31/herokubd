function getAll(){
    var request = new XMLHttpRequest;
    request.open('GET', "https://8000-jannethsm31-herokubd-3uydt42hlvc.ws-us105.gitpod.io/contactos");
    request.send();

    request.onload = (e) => {
        const response = request.responseText;
        const json = JSON.parse(response);
        console.log("response" + response);
        console.log("json: " + json);
        console.log("status_code: " + request.status);

        console.log("Email: " + json[0]["email"]);
        console.log("Nombre: " + json[1]["nombre"]);
        console.log("Telefono: " + json[2]["telefono"]);

        const tbody_contactos = document.getElementById("tbody_contactos");
        var tr = document.createElement("tr");
        var td_email = document.createElement("td");
        var td_nombre = document.createElement("td");
        var td_telefono = document.createElement("td")
        
        td_email.innerHTML = json[1]["email"];
        td_nombre.innerHTML = json[1]["nombre"];
        td_telefono.innerHTML = json[1]["telefono"];

        tr.appendChild(td_email);
        tr.appendChild(td_nombre);
        tr.appendChild(td_telefono);

        tbody_contactos.appendChild(tr);
    };
};