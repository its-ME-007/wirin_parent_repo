let map;
let userLocationMarker;
let startMarker;
let endMarker;
let startCoordinates;
let endCoordinates;

const bangaloreCoordinates = [77.5946, 12.9716];

// Initialize the map
function initializeMap(center = bangaloreCoordinates) {
    map = new mapboxgl.Map({
        container: 'map',
        center: center,
        zoom: 17,
        pitch: 60,
    });

    map.addControl(new mapboxgl.FullscreenControl(), 'top-right');

    const geolocate = new mapboxgl.GeolocateControl({
        positionOptions: {
            enableHighAccuracy: true
        },
        trackUserLocation: true,
        showUserHeading: true
    });

    map.addControl(geolocate, 'top-right');

    map.addControl(new PanToRouteControl(), 'top-right');
    map.addControl(new PitchControl(), 'bottom-right');
    map.addControl(new BearingControl(), 'bottom-right');
    map.addControl(new ZoomControls(), 'bottom-right');

    geolocate.on('geolocate', (e) => {
        const userLocation = [e.coords.longitude, e.coords.latitude];
        if (userLocationMarker) {
            userLocationMarker.setLngLat(userLocation);
        } else {
            userLocationMarker = new mapboxgl.Marker({
                color: 'blue',
                draggable: false
            }).setLngLat(userLocation).addTo(map);
        }
    });
    addTimeOfDayButtons();
}

// Initialize the geocoders
function initializeGeocoders() {
    const bangaloreBounds = [77.3733, 12.7343, 77.8721, 13.1377]; // Approx bounding box for Bangalore
    const karnatakaBounds = [74.0411, 11.5933, 78.5883, 18.4506]; // Approx bounding box for Karnataka
    const indiaBounds = [68.1766, 6.7471, 97.4026, 35.5087]; // Approx bounding box for India

    const geocoderOptions = {
        accessToken: mapboxgl.accessToken,
        mapboxgl: mapboxgl,
        countries: "IN", // Limit results to India
        proximity: { longitude: 77.5946, latitude: 12.9716 }, // Bangalore coordinates for proximity
    };

    const geocoderStart = new MapboxGeocoder({
        ...geocoderOptions,
        bbox: bangaloreBounds, // Bangalore bounding box for first priority
    });

    const geocoderEnd = new MapboxGeocoder({
        ...geocoderOptions,
        bbox: bangaloreBounds, // Bangalore bounding box for first priority
    });

    // Append geocoders to the DOM
    document.getElementById('geocoder-start').appendChild(geocoderStart.onAdd(map));
    document.getElementById('geocoder-end').appendChild(geocoderEnd.onAdd(map));

    // Handle results from the geocoders
    geocoderStart.on('result', (e) => {
        startCoordinates = e.result.geometry.coordinates;
        addStartMarker(startCoordinates);
        panToLocation(startCoordinates);
    });

    geocoderEnd.on('result', (e) => {
        endCoordinates = e.result.geometry.coordinates;
        addEndMarker(endCoordinates);
        panToLocation(endCoordinates);
 });

    // Modify geocoder options to include broader search results
    geocoderStart.on('results', (e) => {
        if (e.features.length < 1) {
            geocoderStart.setBbox(karnatakaBounds); // Extend search to Karnataka if no results in Bangalore
            geocoderStart.query(e.query); // Re-query with the broader bounding box
        } else if (e.features.length < 3) {
            geocoderStart.setBbox(indiaBounds); // Extend search to India if few results in Karnataka
            geocoderStart.query(e.query); // Re-query with the broader bounding box
        }
    });

    geocoderEnd.on('results', (e) => {
        if (e.features.length < 1) {
            geocoderEnd.setBbox(karnatakaBounds); // Extend search to Karnataka if no results in Bangalore
            geocoderEnd.query(e.query); // Re-query with the broader bounding box
        } else if (e.features.length < 3) {
            geocoderEnd.setBbox(indiaBounds); // Extend search to India if few results in Karnataka
            geocoderEnd.query(e.query); // Re-query with the broader bounding box
        }
    });
}

// Add start marker
function addStartMarker(coordinates) {
    if (startMarker) {
        startMarker.setLngLat(coordinates);
    } else {
        startMarker = new mapboxgl.Marker({ color: 'blue' })
            .setLngLat(coordinates)
            .setPopup(new mapboxgl.Popup().setHTML("<h4>Start Location</h4>"))
            .addTo(map);
    }
}

// Add end marker
function addEndMarker(coordinates) {
    if (endMarker) {
        endMarker.setLngLat(coordinates);
    } else {
        endMarker = new mapboxgl.Marker({ color: 'red' })
            .setLngLat(coordinates)
            .setPopup(new mapboxgl.Popup().setHTML("<h4>End Location</h4>"))
            .addTo(map);
    }
}

// Pan to location
function panToLocation(coordinates) {
    map.flyTo({
        center: coordinates,
        essential: true,
        zoom: 17
    });
}

// Use user location as starting location
function useUserLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
            startCoordinates = [position.coords.longitude, position.coords.latitude];
            
            // Remove any previous start marker
            if (startMarker) {
                startMarker.remove();
                startMarker = null;
            }
            
            // Pan to user location without adding a new start marker
            panToLocation(startCoordinates);
            clearGeocoderInput('geocoder-start');
            setGeocoderInput('geocoder-start', startCoordinates);
        }, error => {
            console.error("Error getting user location:", error);
            alert("Unable to retrieve your location. Please try again.");
        });
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}



// Clear geocoder input
function clearGeocoderInput(geocoderId) {
    const geocoderInput = document.querySelector(`#${geocoderId} .mapboxgl-ctrl-geocoder--input`);
    if (geocoderInput) {
        geocoderInput.value = '';
    }
}

// Set geocoder input
function setGeocoderInput(geocoderId, coordinates) {
    const geocoderInput = document.querySelector(`#${geocoderId} .mapboxgl-ctrl-geocoder--input`);
    if (geocoderInput) {
        geocoderInput.value = `${coordinates[1]}, ${coordinates[0]}`;
    }
}

class PanToRouteControl {
    onAdd(map) {
        this.map = map;
        this.container = document.createElement('div');
        this.container.className = 'mapboxgl-ctrl mapboxgl-ctrl-group';
        this.button = document.createElement('button');
        this.button.className = 'mapboxgl-ctrl-icon';
        this.button.type = 'button';
        this.button.title = 'Show entire route';
        this.button.innerHTML = '⤢';
        this.button.onclick = () => {
            const routeSource = this.map.getSource('route');
            if (routeSource) {
                const routeData = routeSource._data;
                fitRouteToBounds(routeData);
            }
        };
        this.container.appendChild(this.button);
        return this.container;
    }

    onRemove() {
        this.container.parentNode.removeChild(this.container);
        this.map = undefined;
    }
}

// Initialize map with user's current location or default location
navigator.geolocation.getCurrentPosition(position => {
    const userLocation = [position.coords.longitude, position.coords.latitude];
    initializeMap(userLocation);
}, error => {
    console.error("Error getting user location:", error);
    initializeMap();
}, {
    enableHighAccuracy: true,
    maximumAge: 0,
    timeout: 27000
});

// Load geocoders independently on page load
document.addEventListener('DOMContentLoaded', () => {
    initializeGeocoders();
});
