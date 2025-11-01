function loadPage(page) {
    var iframe = document.getElementById("content-frame");
    iframe.src = page;
}

function init() {
    const hash = window.location.hash;

    if (hash) {
        if (hash === "#home") {
            loadPage('home.html');
        } else if (hash === "#services") {
            loadPage('services.html');
        } else if (hash === "#doctors") {
            loadPage('doctors.html');
        } else if (hash === "#contact") {
            loadPage('contactus.html')
        }
    } else {
        loadPage('home.html');
    }
}

window.onload = init;