//Switch para activar modo claro y oscuro
let switchTheme = document.getElementById("switch-theme");
const bodyHtml = document.body;

switchTheme.onclick = function() {
    switchTheme.classList.toggle("active")
    bodyHtml.classList.toggle("darkmode")
}