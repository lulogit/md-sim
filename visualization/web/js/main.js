// 
// create map
//
mapboxgl.accessToken = 'pk.eyJ1IjoibHVsb21hcGJveCIsImEiOiJjanhhaml5M2owNDhoM3JwYmdvcXd5eTl0In0.NxWh1gIXWBB-fUkIvljLJA';

var map = new mapboxgl.Map({
    container: 'map', // container id
    style: 'mapbox://styles/lulomapbox/cjxajl3ba0c0h1cmpil1pezef', //hosted style id
    center: [9.190, 45.477], // starting position [lng,lat], milano
    zoom: 11.79 // starting zoom
});

//
// Init simulation
//
map.on('load', function() {
	// some constants for vehicles
	let tv = 0;
	let scale = 3;
	// load all images, then create map layers
	Promise.all(loadImages())
		.then(createMapLayers);
		//.then(getRoutes)
		/*.then(sleeper(2000*scale))
		.then( () => { //routes => { 
			// van routes
			driveRoute(tv,routes[0],10*scale,1*scale)
			.then(sleeper(3000*scale))
			.then(() => driveRoute(tv,routes[6],7*scale,1*scale));
			// bike route
			[5327,13123,3172,7610,10755].map(t => t*scale)
			.forEach((t,i) => {
				sleeper(t)(true)
				.then(() => driveRoute(5-i,routes[5-i],4*scale,0.5*scale));
			});
			// bike's second route
			sleeper(19000*scale+3047*scale)().then(() => driveRoute(3,routes[8],4*scale,0.5*scale));
			sleeper(19000*scale+5942*scale)().then(() => driveRoute(1,routes[7],4*scale,0.5*scale));
			sleeper(19000*scale+8230*scale)().then(() => driveRoute(4,routes[9],4*scale,0.5*scale));
			
			// animate points
			requestAnimationFrame(animationLoop);
		});*/
});
