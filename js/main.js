const orderBtn = document.querySelector(".order-btn")
const oderForm = document.querySelector('order-form')

orderBtn.addEventListener("click" , function () {
    oderForm.classList.add(".display-order-from")
    console.log("Class added")
})