//API key = AIzaSyADULoh4vZX2MsZs4SAgpTgOaXPbjsCNBA
let API_KEY = 'AIzaSyADULoh4vZX2MsZs4SAgpTgOaXPbjsCNBA';

function initMap() {
  //Locations
  let location = {lat: 37.403619, lng: -122.031625};

  //The Map
  let map = new google.maps.Map(document.getElementById('map'), {
      zoom: 16,
      center: location,
    });

  //Custom Marker images
  let icon = "/images/test_droplet.png";

  //Generate list of marker coordinates
  let location_list = [
    {
      position: new google.maps.LatLng(37.403619, -122.031625),
      type: 'info'
    },
  ]

  //Create markers using location_list
location_list.forEach(function(feature) {
  let marker = new google.maps.Marker({
    position: feature.position,
    icon: icon,
    map: map,
  });
});
}
