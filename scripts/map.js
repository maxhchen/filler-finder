let API_KEY = 'AIzaSyADULoh4vZX2MsZs4SAgpTgOaXPbjsCNBA';
let geocoder;
let map;
//Custom Marker image(s)
let icon = "/images/Water_Droplet_Pin.png";
//SF Location: {lat: 37.403619, lng: -122.031625};

function initMap() {
  geocoder = new google.maps.Geocoder();
  //Initial location
  let location = {lat: 37.7749, lng: -122.4194};

  //The map
  map = new google.maps.Map(document.querySelector('#map'), {
      zoom: 12,
      center: location,
      url: '/description',
    });

  //Give the button an event listener so that when clicked it will run codeAddress()
  document.querySelector('#enterAddress').addEventListener('click', e=> {
    codeAddress(geocoder, map);
  });

  //Enter button and does the same as above
  document.querySelector('#address').addEventListener('keypress', e=>{
    if (e.key == 'Enter'){
      codeAddress(geocoder, map);
    }
  });

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
        map.setZoom(16);
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

// Places correct marker based on filler datastore values
function placeMarker(geocoder, map, address, marker_key) {
  console.log("placeMarker " + address);
  geocoder.geocode( {'address' : address}, function(results, status) {
    console.log("placeMarker geocoder result: ", results);
      marker = new google.maps.Marker ({
        map: map,
        icon: icon,
        position: results[0].geometry.location,
      });
      marker.addListener("click", function() {
        window.location.href=marker_key;
      });
  });
}
