//Manipulación dinámica de elementos del nav
const nav = document.getElementById('nav');

nav.addEventListener('click', (e)=>{
if(e.target.classList.contains('nav__block')) {
        e.target.parentElement.classList.toggle('scale');
        e.target.children[1].classList.toggle('rotate180');
    }
    else if(e.target.classList.contains('nav__option')) {
        e.target.parentElement.parentElement.classList.toggle('scale');
        e.target.nextElementSibling.classList.toggle('rotate180');
    }
    else if(e.target.classList.contains('fa-chevron-down')) {
        e.target.parentElement.parentElement.classList.toggle('scale');
        e.target.classList.toggle('rotate180');
    }
})