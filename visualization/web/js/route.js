// Here you'll specify all the parameters necessary for requesting a response from the Optimization API
function navigationURL(coords, vehicle){
	return 'https://api.mapbox.com/optimized-trips/v1/mapbox/'
		+(vehicle=="bike"?"cycling":"driving")+'/'
		+coords.join(';')
		+'?overview=full&steps=false&geometries=geojson&source=first&access_token='
		+mapboxgl.accessToken;
}

function getTrip(coords, vehicle) {
	  // Make a request to the Optimization API
	  return $.ajax({method: 'GET',url: navigationURL(coords, vehicle)});
}

function getRoutes(){

	var routesCoords = [
		// 0: first van trip
		["van",[
			truckLocation,
			clusters[0][0][0],
			clusters[1][0][0],
			clusters[2][0][0],
			clusters[3][0][0],
			clusters[4][0][0] 
		]],
		// 1-5: bikes' first trips
		["bike",clusters[0][0]],
		["bike",clusters[1][0]],
		["bike",clusters[2][0]],
		["bike",clusters[3][0]],
		["bike",clusters[4][0]],
		// 6: second van trip
		["van",[
			truckLocation,
			clusters[0][0][0],
			clusters[2][0][0],
			clusters[3][0][0] 
		]],
		// 7-9: bikes' second trips
		["bike",clusters[0][1]],
		["bike",clusters[2][1]],
		["bike",clusters[3][1]]
	];
	
	var trips = Promise.all(routesCoords.map(([vehicle,rc]) => getTrip(rc,vehicle))).then(results => results.map(data => data.trips[0]));
	
	return trips;
}
