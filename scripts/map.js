//API key = AIzaSyADULoh4vZX2MsZs4SAgpTgOaXPbjsCNBA
let API_KEY = 'AIzaSyADULoh4vZX2MsZs4SAgpTgOaXPbjsCNBA';
let geocoder;



function initMap() {
  geocoder = new google.maps.Geocoder();
  //Locations
  let location = {lat: 37.403619, lng: -122.031625};

  //The Map
  let map = new google.maps.Map(document.querySelector('#map'), {
      zoom: 16,
      center: location,
      url: '/description',
    });

  //Custom Marker images
  let icon = "/images/test_droplet.png";

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
    window.location.href = "/description?key={{ person.key.urlsafe() }}";
  });

});

//Give the button an event listener so that when clicked it will run codeAddress()
document.querySelector('#enterAddress').addEventListener('click', e=> {
  codeAddress(geocoder, map);
  });
}

//Takes the address from the search bar and centers map to that location
function codeAddress(geocoder, map) {
  let address = document.querySelector('#address').value;
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
