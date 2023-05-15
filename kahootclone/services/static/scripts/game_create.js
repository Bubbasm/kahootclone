function refreshTime() {
    $.ajax({
        // https://stackoverflow.com/a/68650203
        url: JSON.parse(document.getElementById('update_participant_url').textContent),
        success: function (data) {
            //deserializing the data
            data.participants = JSON.parse(data.participants);
            $('#participants_list').empty();

            for (participant of data.participants) {
                let td = document.createElement("td");
                let tr = document.createElement("tr");
                let ii = document.createElement("i");
                
                ii.className = "bi bi-person";
                td.appendChild(ii);

                td.className = "col";
                td.appendChild(document.createTextNode(participant.fields.alias));
                
                tr.className = "row text-center fw-bold fs-5"
                tr.appendChild(td);

                $('#participants_list').append(tr);
            }
        }
    });
    setTimeout(refreshTime, 2000);
}

window.addEventListener("load", () => {
    var qr_url = JSON.parse(document.getElementById('qr_url').textContent);
    var pin = JSON.parse(document.getElementById('pin').textContent);
    var url = new URL(qr_url);
    url.searchParams.append('pin', pin);
    new QRCode(document.getElementById("qrcode"), {
        text: url.toString(),
        width: 2048,
        height: 2048,
        colorDark : '#000',
        colorLight : '#f8f9fa',
        correctLevel : QRCode.CorrectLevel.H
    });
});

$( document ).ready(function () {
    refreshTime();
});
