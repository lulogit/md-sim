var animations = [];
var customersUpdated = false;

function animationLoop(timeStamp){
	//
	// compute the movement of the vehicles
	//
	animations.forEach((anim, i) => {
		let hasFinished = anim.tick(timeStamp - anim.startTime);
		if (hasFinished) {
			anim.resolve();
			animations.splice(i,1);
		}
	});
	// Update the sources with new data.
	map.getSource('vehicles').setData(vehicles);
	if (customersUpdated) {
		map.getSource("customers").setData(dlvs);
		customersUpdated = false;
	}
	// loop this
	if (animations) requestAnimationFrame(animationLoop);
}

function driveRoute(vehicleId, route, duration, stopTime){ // times in seconds
	var coords = route.geometry.coordinates;
	var line = turf.linestring(coords);
	var lineDistance = turf.lineDistance(line, 'kilometers');
	
	// scale times and distances	
	var lincomb = (b,d) => {var k = d/b; return (a => a*k);}
	var reDist = lincomb(route.distance, lineDistance);
	var reTime = lincomb(route.duration, duration*1000 /* s -> ms */);
	
	var legTimes = route.legs.map(l => reTime(l.duration));
	var sum = 0;
	var legTimesCum = legTimes.map(t => sum=sum+t+stopTime*1000 /* s->ms */);

	var legDists = route.legs.map(l => reDist(l.distance));
	sum = 0;
	var legDistsCum = legDists.map(d => sum=sum+d);
	console.log(legTimesCum);

	var findLeg = ts => {
		// return the leg in which the simulation is
		for (var i=0;i<legTimesCum.length;i++){
			if (ts<=legTimesCum[i]){
				return i;
			}
		}
		return legTimesCum.length-1;
	};

	var startTime = performance.now();
	var animTime = duration * 1000; // seconds to millis
	var lastLeg = 0;	
	var safePrev = (arr,index) => (index>0 ? arr[index-1] : 0);

	return new Promise( (resolve,reject) => {
		let animation = {
			tick: (elapsed) => {
				let lId = findLeg(elapsed);
				let dist = Math.min(
					safePrev(legDistsCum,lId) + legDists[lId] * (elapsed-safePrev(legTimesCum,lId)) / legTimes[lId],
					legDistsCum[lId]);
				var updatedPoint = null;
				try {
					// And the distance the point has travelled along the route.
					var updatedPoint = turf.along(line, dist, 'kilometers');
					vehicles.features[vehicleId].geometry = updatedPoint.geometry;
					if (lastLeg!=lId){
						lastLeg = lId;
						serveCustomerAt(updatedPoint.geometry.coordinates);
					}
				} catch(e) {
					console.log(dist);
				}

				// Request the next frame of the animation so long as destination.
				// has not been reached.
				return (elapsed>legTimesCum[legTimesCum.length-1]);
			},
			resolve: resolve,
			startTime: performance.now() 
		};
		animations.push(animation);
	});
}

function sleeper(ms) {
  return x => new Promise(resolve => setTimeout(() => resolve(x), ms));
}

function serveCustomerAt(coords){
	let pos = turf.point(coords);
	customer = turf.nearest(pos,dlvs);
	if (turf.distance(pos,customer)<0.2) {
		dlvs.features.splice(dlvs.features.indexOf(customer),1);
		map.getSource("customers").setData(dlvs);
		//custumersUpdated = true;
	}
}
