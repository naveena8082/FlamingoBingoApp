document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registrationForm');
    if (form) {
        form.addEventListener('submit', handleFormSubmission);
    }
    
});

function handleFormSubmission(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const userName = document.getElementById('name').value;
    const dataSource = document.getElementById('dataSource').value;

    if (dataSource === 'mock') {
        // Redirect with mock data source
        redirectToGamePage(email, 'mock');
    } else {
        // Actual call to register API
        console.log(`Registering user with email: ${email} and name: ${userName}`);
        
        // API Gateway endpoint
        const apiEndpoint = 'https://your-api-gateway-endpoint/endpoint';
        
        // Request body
        const requestBody = {
            email: email,
            name: userName  
        };
        
        // Fetch options
        const fetchOptions = {
            method: 'POST',
            headers: {
                'x-api-key': apiKey,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        };
        
        // Performing the fetch request
        fetch(apiEndpoint, fetchOptions)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log('Registration successful:', data);
                // On success, redirect to game page with customer data source
                redirectToGamePage(email, 'customer');
            })
            .catch(error => {
                console.error('Registration failed:', error);
                // Handle registration failure, e.g., show an error message to the user
            });
    }
}


function redirectToGamePage(email, dataSource) {
    window.location.href = `game.html?email=${encodeURIComponent(email)}&dataSource=${dataSource}`;
}

document.addEventListener('DOMContentLoaded', function() {
    const dataSource = document.getElementById('dataSource');
    const gameContainer = document.getElementById('gameContainer');

    // Initialize game based on query parameters or default to mock
    const queryParams = new URLSearchParams(window.location.search);
    const email = queryParams.get('email');
    const dataSourceValue = queryParams.get('dataSource') || 'mock';
    dataSource.value = dataSourceValue;

    // Fetch and display data based on the selected data source
    fetchAndDisplayData(dataSourceValue, email);



   
});

function fetchAndDisplayData(source, email) {
    if (source === 'mock') {
        const response = getMockData();
        displayData(response);
    } else {
        // Define your API Gateway endpoint and API key
        const apiEndpoint = 'https://m97t449xz5.execute-api.us-west-2.amazonaws.com/dev/getCard';
        const apiKey = 'dummy_api_key';
        
        const urlWithParams = `${apiEndpoint}?email=${encodeURIComponent(email)}`;

        // const urlWithParams = 'https://e62zz2leyg.execute-api.us-east-1.amazonaws.com/foo/card/bingo@inspiringapps.com'
        const acceptHeader = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7';

        fetch(urlWithParams, {
            method: 'GET',
            headers: {
                'x-api-key': apiKey,
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
    // Mock data structure, similar to the provided example
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

function submitSelection(source, email) {
    console.log('Submitting selection for', email);
    // For the mock path, just simulate an action like refreshing the displayed data
    if (source === 'mock') {
        alert('Mock submission complete.');
    }
}
