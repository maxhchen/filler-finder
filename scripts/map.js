//API key = AIzaSyADULoh4vZX2MsZs4SAgpTgOaXPbjsCNBA
let API_KEY = 'AIzaSyADULoh4vZX2MsZs4SAgpTgOaXPbjsCNBA';

function initMap() {
  let location = {lat: -200, lng: 200};

  let map = new google.maps.Map(document.getElementById('map'), {
      zoom: 4,
      center: location,
    });
}
