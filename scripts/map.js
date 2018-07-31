//API key = AIzaSyADULoh4vZX2MsZs4SAgpTgOaXPbjsCNBA
let API_KEY = 'AIzaSyADULoh4vZX2MsZs4SAgpTgOaXPbjsCNBA';
let geocoder;
let map;
//{lat: 37.403619, lng: -122.031625};

https://maps.googleapis.com/maps/api/directions/json?&mode=transit&origin=frontera+el+hierro&destination=la+restinga+el+hierro&departure_time=1399995076&key=AIzaSyADULoh4vZX2MsZs4SAgpTgOaXPbjsCNBA

function initMap() {
  geocoder = new google.maps.Geocoder();
  //Initial location
  let location = {lat: 37.7749, lng: -122.4194};

  //The map
  map = new google.maps.Map(document.querySelector('#map'), {
      zoom: 16,
      center: location,
      url: '/description',
    });

  //Custom Marker image(s)
  let icon = "/images/Water_Droplet_Pin.png";

  //Generate list of marker coordinates
  let location_list = [
    {
      position: new google.maps.LatLng(37.403619, -122.031625),
      type: 'info',
    },
  ]

  //Create markers using location_list
  location_list.forEach(function(feature) {
    let marker = new google.maps.Marker({
      position: feature.position,
      icon: icon,
      map: map,
    });
    marker.addListener("click", function() {
      window.location.replace("/description?key={{filler.key.urlsafe()}}");
    });
  });

  //Give the button an event listener so that when clicked it will run codeAddress()
  document.querySelector('#enterAddress').addEventListener('click', e=> {
    codeAddress(geocoder, map);
  });

  //Run the placemarker function
  markerPlacement()

  //On page load attempt to recenter map at user location
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude,
      };
      map.setCenter(pos);
    }, function() {
      handleLocationError(true, infoWindow, map.getCenter());
    });
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
  }
}

//Tries to handle error with finding user location
function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
    'Error: The Geolocation service failed.' :
    'Error: Your browser doesn\'t support geolocation.');
  infoWindow.open(map);
}

//Change click for 'keypress'
//Then also change to an if (e.key == 'Enter'){codeAddress(geocoder, map)}

//Takes the address from the search bar and centers map to that location
function codeAddress(geocoder, map) {
  let address = document.querySelector('#address').value;
  console.log(address)
  geocoder.geocode( { 'address': address}, function(results, status) {
      if (status == 'OK') {
        map.setCenter(results[0].geometry.location);

        //This will place a marker on the address entered
        // let marker = new google.maps.Marker({
        //     map: map,
        //     position: results[0].geometry.location
        // });

      } else {
        alert('Something went wrong: ' + status);
      }
    });
}

//Runs when database is loaded, is called in the home.html
function placeMarker(geocoder, map, address) {

  geocoder.geocode( {'address': address}, function(results, status)
  {
    if (status == 'OK'){
    //Place a marker
    let marker = new google.maps.Marker
    ({
      map: map,
      position: results[0].geometry.location
    });

    //Error
    } else
    {
      //('Boom: ' + status);
    }
  });
}
