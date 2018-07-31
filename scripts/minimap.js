let API_KEY = 'AIzaSyADULoh4vZX2MsZs4SAgpTgOaXPbjsCNBA';
let geocoder;

function initMap() {
  geocoder = new google.maps.Geocoder();
  //Initial location
  let location = {lat: 37.7749, lng: -122.4194};

  //The map
  let map = new google.maps.Map(document.querySelector('#minimap'), {
      zoom: 18,
      center: location,
    });

//console.log(filler.location);

  geocoder.geocode( { 'address': {{ filler.location }} }, function(results, status) {
        map.setCenter(results[0].geometry.location);
    });

  //Custom Marker image(s)
  let icon = "/images/Water_Droplet_Pin.png";

  //Create markers using location_list
    let marker = new google.maps.Marker({
      position: feature.position,
      icon: icon,
      map: map,
    });
}

function codeAddress(geocoder, map) {
  geocoder.geocode( { 'address': filler.location}, function(results, status) {
        map.setCenter(results[0].geometry.location);
    });
}
