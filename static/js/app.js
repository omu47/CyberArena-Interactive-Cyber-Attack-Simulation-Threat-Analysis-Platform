const logs = [
    "[INFO] Monitoring incoming traffic...",
    "[WARNING] Encoded payload detected...",
    "[ALERT] Suspicious authentication request...",
    "[INFO] Scanning uploaded image...",
    "[CRITICAL] Phishing pattern identified...",
    "[INFO] RSA weak cipher analysis running...",
    "[WARNING] Possible social engineering attempt..."
];

const logContainer = document.getElementById("logs");

let index = 0;

setInterval(() => {

    const newLog = document.createElement("p");

    newLog.textContent = logs[index];

    logContainer.appendChild(newLog);

    logContainer.scrollTop = logContainer.scrollHeight;

    index++;

    if (index >= logs.length) {
        index = 0;
    }

}, 2000);