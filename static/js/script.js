// Global Variables
let closealert = document.querySelector('.close-btn')
let messages = document.querySelector('.messages')
let searchForm = document.querySelector('#searchForm');
let pageBtn = document.querySelectorAll('.page-btn');

// Code to close to message boxes automatically and allow you to close them manually
if (closealert) {
    messages.style.display = 'block'
    closealert.addEventListener('click', () =>
        messages.style.display = 'none')
    setTimeout(() => {
        messages.style.display = 'none'
    }, 3000);
}

// Code to link search form and pagination together
if (searchForm) {
    for (let i = 0; pageBtn.length > i; i++) {
    pageBtn[i].addEventListener('click', function (event) {
        event.preventDefault()
        console.log('still here')
        let page = this.dataset.page
        console.log(page)
        searchForm.innerHTML += `<input value=${page} name="page" hidden/>`
        searchForm.submit()
    })
}
}