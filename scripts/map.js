//API key = AIzaSyADULoh4vZX2MsZs4SAgpTgOaXPbjsCNBA
let API_KEY = 'AIzaSyADULoh4vZX2MsZs4SAgpTgOaXPbjsCNBA';

function initMap() {

  //Locations
  let location = {lat: 37.403619, lng: -122.031625};

  //The Map
  let map = new google.maps.Map(document.querySelector('#map'), {
      zoom: 16,
      center: location,
      url: '/description',
    });

  //Markers
  let testMarker = new google.maps.Marker({position: location, map: map});

// Add way to find user's current location
// https://developers.google.com/maps/documentation/javascript/geolocation
// Implement filtering for locations
// https://appendto.com/2016/09/advanced-google-maps-with-javascript-filtering-and-displaying-information/



}
