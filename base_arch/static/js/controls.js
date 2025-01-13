class PitchControl {
    onAdd(map) {
        this.map = map;
        this.container = document.createElement('div');
        this.container.className = 'mapboxgl-ctrl mapboxgl-ctrl-group';
        this.button = document.createElement('button');
        this.button.className = 'mapboxgl-ctrl-icon';
        this.button.type = 'button';
        this.button.title = 'Adjust pitch';
        this.button.innerHTML = '↕';
        this.button.onclick = () => {
            const currentPitch = this.map.getPitch();
            const newPitch = currentPitch === 60 ? 0 : 60;
            this.map.easeTo({ pitch: newPitch });
        };
        this.container.appendChild(this.button);
        return this.container;
    }

    onRemove() {
        this.container.parentNode.removeChild(this.container);
        this.map = undefined;
    }
}

class BearingControl {
    onAdd(map) {
        this.map = map;
        this.container = document.createElement('div');
        this.container.className = 'mapboxgl-ctrl mapboxgl-ctrl-group';
        this.button = document.createElement('button');
        this.button.className = 'mapboxgl-ctrl-icon';
        this.button.type = 'button';
        this.button.title = 'Adjust bearing';
        this.button.innerHTML = '⤵';
        this.button.onclick = () => {
            const currentBearing = this.map.getBearing();
            const newBearing = currentBearing === 0 ? 180 : 0;
            this.map.easeTo({ bearing: newBearing });
        };
        this.container.appendChild(this.button);
        return this.container;
    }

    onRemove() {
        this.container.parentNode.removeChild(this.container);
        this.map = undefined;
    }
}

class ZoomControls {
    onAdd(map) {
        this.map = map;
        this.container = document.createElement('div');
        this.container.className = 'mapboxgl-ctrl mapboxgl-ctrl-group';
        this.zoomInButton = document.createElement('button');
        this.zoomInButton.className = 'mapboxgl-ctrl-icon';
        this.zoomInButton.type = 'button';
        this.zoomInButton.title = 'Zoom in';
        this.zoomInButton.innerHTML = '+';
        this.zoomInButton.onclick = () => this.map.zoomIn();
        this.zoomOutButton = document.createElement('button');
        this.zoomOutButton.className = 'mapboxgl-ctrl-icon';
        this.zoomOutButton.type = 'button';
        this.zoomOutButton.title = 'Zoom out';
        this.zoomOutButton.innerHTML = '−';
        this.zoomOutButton.onclick = () => this.map.zoomOut();
        this.container.appendChild(this.zoomInButton);
        this.container.appendChild(this.zoomOutButton);
        return this.container;
    }

    onRemove() {
        this.container.parentNode.removeChild(this.container);
        this.map = undefined;
    }
}

// Add time of day buttons
function addTimeOfDayButtons() {
    const timeOfDayContainer = document.createElement('div');
    timeOfDayContainer.className = 'mapboxgl-ctrl mapboxgl-ctrl-group time-of-day-buttons';

    const dawnButton = createTimeOfDayButton('dawn', '☀️');
    dawnButton.onclick = () => map.setConfigProperty('basemap', 'lightPreset', 'dawn');
    
    const dayButton = createTimeOfDayButton('day', '🌞');
    dayButton.onclick = () => map.setConfigProperty('basemap', 'lightPreset', 'day');
    
    const duskButton = createTimeOfDayButton('dusk', '🌅');
    duskButton.onclick = () => map.setConfigProperty('basemap', 'lightPreset', 'dusk');
    
    const nightButton = createTimeOfDayButton('night', '🌜');
    nightButton.onclick = () => map.setConfigProperty('basemap', 'lightPreset', 'night');

    timeOfDayContainer.appendChild(dawnButton);
    timeOfDayContainer.appendChild(dayButton);
    timeOfDayContainer.appendChild(duskButton);
    timeOfDayContainer.appendChild(nightButton);

    map.addControl({
        onAdd: () => {
            return timeOfDayContainer;
        },
        onRemove: () => {
            timeOfDayContainer.parentNode.removeChild(timeOfDayContainer);
        }
    }, 'bottom-left');
}

function createTimeOfDayButton(id, text) {
    const button = document.createElement('button');
    button.className = 'mapboxgl-ctrl-icon time-of-day-button';
    button.type = 'button';
    button.id = id;
    button.innerText = text;
    return button;
}
