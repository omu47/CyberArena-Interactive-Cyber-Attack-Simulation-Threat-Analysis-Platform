const map = L.map('map').setView([20, 0], 2);

L.tileLayer(
    'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    {
        attribution: 'CyberArena Threat Intelligence'
    }
).addTo(map);

/* ATTACK DATA */

const attacks = [

    {
        origin: [55.7558, 37.6173],
        target: [40.7128, -74.0060],
        type: "Ransomware Attack"
    },

    {
        origin: [28.6139, 77.2090],
        target: [51.5074, -0.1278],
        type: "Phishing Campaign"
    },

    {
        origin: [39.9042, 116.4074],
        target: [35.6895, 139.6917],
        type: "Botnet Traffic"
    },

    {
        origin: [52.5200, 13.4050],
        target: [19.0760, 72.8777],
        type: "Credential Harvesting"
    }
];

function createAttack(attack) {

    const line = L.polyline(
        [attack.origin, attack.target],
        {
            color: '#00ff9f',
            weight: 2
        }
    ).addTo(map);

    const marker = L.circleMarker(
        attack.target,
        {
            radius: 8,
            color: 'red'
        }
    ).addTo(map);

    marker.bindPopup(
        `<b>${attack.type}</b>`
    );
}

/* Animate attacks */

let index = 0;

setInterval(() => {

    createAttack(attacks[index]);

    index++;

    if (index >= attacks.length) {
        index = 0;
    }

}, 2000);