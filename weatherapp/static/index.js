const container = document.querySelector('.container');
const search = document.querySelector('.search-box button');
const searchinput = document.querySelector('.search-box input')
const weatherBox = document.querySelector('.weather-box');
const weatherDetails = document.querySelector('.weather-details');
const error404 = document.querySelector('.not-found');

searchinput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        search.click();
    }
});


search.addEventListener('click', () => {
    const city = document.querySelector('.search-box input').value;

    if (city === '')
        return;

    fetch(`/weather?city=${city}`)
        .then(response => response.json())
        .then(json => {
            
            if (json.cod === '404') {
                container.style.height = '400px';
                weatherBox.style.display = 'none';
                weatherDetails.style.display = 'none';
                error404.style.display = 'block';
                error404.classList.add('fadeIn');
                return;
            }

            error404.style.display = 'none';
            error404.classList.remove('fadeIn');

            const image = document.querySelector('.weather-box img');
            const temperature = document.querySelector('.weather-box .temperature');
            const description = document.querySelector('.weather-box .description');
            const humidity = document.querySelector('.weather-details .humidity span');
            const wind = document.querySelector('.weather-details .wind span');

            switch (json.main) {
                case 'Clear':
                    image.src = 'static/images/clear.png';
                    break;

                case 'Rain':
                    image.src = 'static/images/rain.png';
                    break;

                case 'Snow':
                    image.src = 'static/images/snow.png';
                    break;

                case 'Clouds':
                    image.src = 'static/images/cloud.png';
                    break;

                case 'Haze':
                    image.src = 'static/images/mist.png';
                    break;

                case 'Drizzle':
                    image.src = 'static/images/rain.png';
                    break;


                default:
                    image.src = '';
            }

            temperature.innerHTML = `${json.temp}<span>°C</span>`;
            description.innerHTML = `${json.desc}`;
            humidity.innerHTML = `${json.hum}%`;
            wind.innerHTML = `${json.wind}Km/h`;

            weatherBox.style.display = '';
            weatherDetails.style.display = '';
            weatherBox.classList.add('fadeIn');
            weatherDetails.classList.add('fadeIn');
            container.style.height = '590px';


        });


});