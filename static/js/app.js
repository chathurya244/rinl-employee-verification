// =============================
// TOGGLE NAVBAR MENU (MOBILE)
// =============================
function togglemenu() {
    const links = document.getElementById("navlinks");
    links.classList.toggle("active");
}


// =============================
// SHOW / HIDE VERIFICATION INFO
// =============================
function showWhiteBox() {
    const box = document.querySelector('.white-box');
    box.classList.toggle('show');
}