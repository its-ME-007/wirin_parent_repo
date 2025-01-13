function getRoute() {
    if (!startCoordinates || !endCoordinates) {
        alert("Please enter both a starting location and a destination.");
        return;
    }

    fetch(`/api/directions?start=${startCoordinates.join(',')}&end=${endCoordinates.join(',')}`)
        .then(response => response.json())
        .then(data => {
            const route = data.route;
            addRouteToMap(route);
            fitRouteToBounds(route);

            // Calculate the midpoint
            const midpoint = [
                (startCoordinates[0] + endCoordinates[0]) / 2,
                (startCoordinates[1] + endCoordinates[1]) / 2
            ];

            // Perform animations
            setTimeout(() => {
                
                const zoom = map.getZoom() *0.98;

                map.flyTo({
                    center: midpoint,
                    zoom: zoom,
                    pitch: 60,
                    bearing: 0,
                    essential: true,
                    speed: 1.2
                });

                // Rotate the bearing 360 degrees
                setTimeout(() => {
                    let bearing = 0;
                    const rotationInterval = setInterval(() => {
                        bearing += 10;
                        if (bearing >= 360) {
                            clearInterval(rotationInterval);

                            // After rotation, fly back to user's location
                            setTimeout(() => {
                                map.flyTo({
                                    center: startCoordinates,
                                    zoom: 17,
                                    pitch: 60,
                                    essential: true
                                });
                            }, 1000);
                        } else {
                            map.rotateTo(bearing, { duration: 100 });
                        }
                    }, 100);
                }, 2000);
            }, 1000);
        })
        .catch(error => {
            console.error('Error fetching directions:', error);
            alert("Error fetching directions. Please try again.");
        });
}


function addRouteToMap(route) {
    if (map.getSource('route')) {
        map.getSource('route').setData(route);
    } else {
        map.addLayer({
            id: 'route',
            type: 'line',
            source: {
                type: 'geojson',
                data: route
            },
            layout: {
                'line-join': 'round',
                'line-cap': 'round'
            },
            paint: {
                'line-color': '#3887be',
                'line-width': 10,
                'line-opacity': 0.75
            }
        });
    }
}

function fitRouteToBounds(route) {
    const bounds = new mapboxgl.LngLatBounds();
    route.coordinates.forEach(coord => {
        bounds.extend(coord);
    });
    map.fitBounds(bounds, {
        padding: { top: 50, bottom: 50, left: 50, right: 50 },
        pitch: 0
    });
}

