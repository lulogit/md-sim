function createMapLayers(){
	//
	// data sources for layers
	//
	[
		["microhubs", mhs],
		["customers",dlvs],
		["vehicles", vehicles]
	].forEach(([name,data]) => {
		map.addSource(name, {type: 'geojson', data: data});
		map.addLayer({id: name,type: 'symbol',source: name,layout: {
		    'icon-image': ['get','img'],
		    'icon-size': ['get','scale'],
		    'icon-allow-overlap': true,
		    'icon-ignore-placement': true
		  },
		},"wharehouses");
	});
	//
	// update wharehouse image
	//
	map.setLayoutProperty("wharehouses","icon-size",1);
	map.setLayoutProperty("wharehouses","icon-image","warehouse");
}

function loadImages(){
	return ["customer","hub","van","warehouse","bike"].map(name => new Promise((resolve,reject) => {
		map.loadImage(`img/${name}.svg.png`, (e,img) => {
			if (e) reject(e);
			map.addImage(name,img); 
			resolve(name);
		});
	}));
}
