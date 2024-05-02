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

function updateGame() {
    const alphabet = 'ABCDEFGHIJ';
    fetch('/data').then(response => response.json()).then(data => {
        document.getElementById('playerMove').innerText = data['playerMove'];
        document.getElementById('winner').innerText = data['winner'];

        for (let i = 0; i < 10; i++) {
            for (let j = 0; j < 10; j++) {
                let cellId = '#' + alphabet[i] + (j + 1);

                if (data['field1'][i][j] == -1) {
                    document.querySelector('.container #field1 ' + cellId).style.backgroundColor = 'red';
                } else if (data['field1'][i][j] == 0) {
                    document.querySelector('.container #field1 ' + cellId).style.backgroundColor = 'white';
                } else {
                    document.querySelector('.container #field1 ' + cellId).style.backgroundColor = 'green';
                }

                if (data['field2'][i][j] == -1) {
                    document.querySelector('.container #field2 ' + cellId).style.backgroundColor = 'red';
                } else if (data['field2'][i][j] == 0) {
                    document.querySelector('.container #field2 ' + cellId).style.backgroundColor = 'white';
                } else {
                    document.querySelector('.container #field2 ' + cellId).style.backgroundColor = 'green';
                }
            }
        }
    });
}
setInterval(updateGame, 10);
