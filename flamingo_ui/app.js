const API_ENDPOINT_PLAYER_REGISTRATION = 'https://m97t449xz5.execute-api.us-west-2.amazonaws.com/dev/playerRegistration';
const API_ENDPOINT_GET_CARD = 'https://m97t449xz5.execute-api.us-west-2.amazonaws.com/dev/getCard';
const API_ENDPOINT_FLAMINGO_SIGHTING = 'https://m97t449xz5.execute-api.us-west-2.amazonaws.com/dev/flamingoSightingSubmission';
const API_KEY = 'dummy_key';

document.addEventListener('DOMContentLoaded', function() {
    const registrationForm = document.getElementById('registrationForm');
    if (registrationForm) {
        registrationForm.addEventListener('submit', handleFormSubmission);
    }

    const gameContainer = document.getElementById('gameContainer');
    if (gameContainer) {
        gameContainer.addEventListener('click', handleCardItemClick);
    }

    initializeGame();
});

function handleFormSubmission(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const userName = document.getElementById('name').value;
    const dataSource = document.getElementById('dataSource').value;

    if (dataSource === 'mock') {
        redirectToGamePage(email, 'mock');
    } else {
        registerPlayer(email, userName);
    }
}

function handleCardItemClick(event) {
    if (event.target.classList.contains('cardItem')) {
        const selectedText = event.target.textContent;
        if (selectedText !== 'Free') {
            triggerFlamingoSighting(selectedText);
        }
    }
}

function initializeGame() {
    const dataSource = document.getElementById('dataSource');
    const queryParams = new URLSearchParams(window.location.search);
    const email = queryParams.get('email');
    const dataSourceValue = queryParams.get('dataSource') || 'mock';
    dataSource.value = dataSourceValue;

    fetchAndDisplayData(dataSourceValue, email);
}

function registerPlayer(email, userName) {
    const requestBody = {
        email_id: email,
        name: userName
    };

    const fetchOptions = {
        method: 'POST',
        headers: {
            'x-api-key': API_KEY,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
    };

    fetch(API_ENDPOINT_PLAYER_REGISTRATION, fetchOptions)
        .then(response => {
            if (!response.ok) {
                if (response.status === 409) {
                    alert('Player already exists. Please try with a different email or username.');
                } else {
                    alert('Please try again');
                }
            }
            return response.json();
        })
        .then(data => {
            redirectToGamePage(email, 'customer');
        })
        .catch(error => {
            console.error('Registration failed:', error);
        });
}

function redirectToGamePage(email, dataSource) {
    window.location.href = `game.html?email=${encodeURIComponent(email)}&dataSource=${dataSource}`;
}

function fetchAndDisplayData(source, email) {
    if (source === 'mock') {
        const response = getMockData();
        displayData(response);
    } else {
        const urlWithParams = `${API_ENDPOINT_GET_CARD}?email=${encodeURIComponent(email)}`;

        fetch(urlWithParams, {
            method: 'GET',
            headers: {
                'x-api-key': API_KEY,
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Data fetched successfully:', data);
            displayData(data);
        })
        .catch(error => {
            console.error('Failed to fetch data:', error);
        });
    }
}

function getMockData() {
    return  {
        card: [
            "South America",
            "Gulf of Mexico",
            "West Africa",
            null,
            "South Africa",
            "Mediterranean",
            "East Asia",
            "Arabian Sea",
            null
        ],
        completions: [false, true, false, false, false, false, false, false, false],
        email: "bingo@InspiringApps.com",
        name: "Inspired Bingo"
    };
}

function displayData(data) {
    const gameContainer = document.getElementById('gameContainer');
    const bingoCardDiv = gameContainer.querySelector('.bingoCard');
    bingoCardDiv.innerHTML = '';

    data.card.forEach((item, index) => {
        const cardItem = document.createElement('div');
        cardItem.classList.add('cardItem');
        if (item === null) {
            cardItem.textContent = 'Free';
            cardItem.classList.add('selected');
        } else {
            cardItem.textContent = item;
            if (data.completions[index]) cardItem.classList.add('selected');
        }
        bingoCardDiv.appendChild(cardItem);
    });
}

function triggerFlamingoSighting(selectedText) {
    const requestBody = {
        region: selectedText
    };

    const fetchOptions = {
        method: 'POST',
        headers: {
            'x-api-key': API_KEY,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
    };

    fetch(API_ENDPOINT_FLAMINGO_SIGHTING, fetchOptions)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('API call successful:', data);
            markRegionAsFilled(selectedText);
            alert('Region marked as filled successfully!');
        })
        .catch(error => {
            console.error('API call failed:', error);
        });
}

function markRegionAsFilled(selectedText) {
    const cardItems = document.querySelectorAll('.cardItem');
    cardItems.forEach(cardItem => {
        if (cardItem.textContent === selectedText) {
            cardItem.classList.add('selected');
        }
    });
}
