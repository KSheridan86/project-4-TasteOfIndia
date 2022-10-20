// Global Variables
let closealert = document.querySelector('.close-btn');
let messages = document.querySelector('.messages');
let searchForm = document.querySelector('#searchForm');
let pageBtn = document.querySelectorAll('.page-btn');
let topBtn = document.querySelector('.back-to-top');

// Code to close the message boxes automatically and allow you to close them manually
if (closealert) {
    messages.style.display = 'block';
    closealert.addEventListener('click', () =>
        messages.style.display = 'none');
    setTimeout(() => {
        messages.style.display = 'none';
    }, 2500);
}

// Code to link search form and pagination together
if (searchForm) {
    for (let i = 0; pageBtn.length > i; i++) {
    pageBtn[i].addEventListener('click', function (event) {
        event.preventDefault();
        let page = this.dataset.page;
        searchForm.innerHTML += `<input value=${page} name="page" hidden/>`;
        searchForm.submit();
    });
}
}

// Code to hide the back to top button until the user scrolls down
function backToTop() {
    if (document.body.scrollTop > 400 || document.documentElement.scrollTop > 400) {
        topBtn.style.display = "block";
        } else {
        topBtn.style.display = "none";
        }
}

window.onscroll = function() {backToTop();};