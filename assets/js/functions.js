/* Botón para volver a la página anterior */
function previousPage() {
    window.history.back();
}

const backButton = document.getElementById('back_btn');

backButton.addEventListener("click", previousPage);