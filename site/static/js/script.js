function updateTimer() {
    fetch('/time').then(response => response.text()).then(data => {
        document.getElementById('timer').innerText = data;
    });
}
setInterval(updateTimer, 1000);

function updateClientsCount() {
    fetch('/clients').then(response => response.text()).then(data => {
        document.getElementById('clientsCount').innerText = data;
    });
}
setInterval(updateClientsCount, 500);

// function updateGameInfo() {
//     fetch('/gameInfo').then(response => response.text()).then(data => {
//         document.getElementById('clientsCount').innerText = data;
//     });
// }
// setInterval(updateClientsCount, 10);

// function updateField() {
//     fetch('/field').then(response => response.text()).then(data => {
//         document.getElementById('clientsCount').innerText = data;
//     });
// }
// setInterval(updateClientsCount, 10);