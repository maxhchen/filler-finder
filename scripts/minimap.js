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

  let marker_location = "{{ filler.location }}";

  geocoder.geocode( { 'address': marker_location }, function(results, status) {
        map.setCenter(results[0].geometry.location);
    });
  //Custom Marker image(s)
  let icon = "/images/Water_Droplet_Pin.png";
  //Create markers using location_list
    placeMarker(geocoder, map, "{{ filler.location }}", icon);
}
function codeAddress(geocoder, map) {
  geocoder.geocode( { 'address': filler.location}, function(results, status) {
        map.setCenter(results[0].geometry.location);
    });
}

function placeMarker(geocoder, map, address, icon) {
  geocoder.geocode( {'address' : address}, function(results, status) {
      marker = new google.maps.Marker ({
        map: map,
        icon: icon,
        position: results[0].geometry.location,
      });
  });
  //return marker;
}
