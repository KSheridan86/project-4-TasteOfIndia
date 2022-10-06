// Global Variables
let closealert = document.querySelector('.close-btn')
let messages = document.querySelector('.messages')

// Code to close to message boxes automatically and allow you to close them manually
if (closealert) {
    messages.style.display = 'block'
    closealert.addEventListener('click', () =>
        messages.style.display = 'none')
    setTimeout(() => {
        messages.style.display = 'none'
    }, 3000);
}