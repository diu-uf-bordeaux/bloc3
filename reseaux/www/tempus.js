function doDate() {
    var now = new Date();
    str = now.toLocaleDateString("fr") + ", " + now.toLocaleTimeString("fr");
    document.getElementById("today").innerHTML = str;
}

setInterval(doDate, 1000); // every seconds


