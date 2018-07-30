//API key = AIzaSyADULoh4vZX2MsZs4SAgpTgOaXPbjsCNBA
let API_KEY = 'AIzaSyADULoh4vZX2MsZs4SAgpTgOaXPbjsCNBA';

function initMap() {
  let location = {lat: 37.403619, lng: -122.031625};
  let map = new google.maps.Map(document.getElementById('map'), {
      zoom: 16,
      center: location,
    });
}
