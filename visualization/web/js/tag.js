//	currentMH = null;
//	clusters = {};

map.on('click','microhubs', e => {
	var mhId = e.features[0].properties.id;
	currentMH = mhId;
	clusters[currentMH] = clusters[currentMH] || [];
	clusters[currentMH].push([e.features[0].geometry.coordinates]);
});
map.on('click','deliveries', e => {
	var f = e.features[0];
	var dlvLoc = f.geometry.coordinates;
	var id = f.properties.id;
	dlvs.features = dlvs.features.map(f => {
		if (f.properties.id == id){
			f.properties.clustered = currentMH;
		}
		return f;
	});
	map.getSource("deliveries").setData(dlvs);
	clst = clusters[currentMH];
	clst[clst.length-1].push(dlvLoc);
});
