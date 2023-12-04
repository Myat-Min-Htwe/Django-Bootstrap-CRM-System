const taskMarkBtn = document.querySelector('#taskMarkBtn');
const taskChangeField = document.querySelector('#taskChange');

console.log("hello")

taskMarkBtn.addEventListener("click", (e) => {
    e.preventDefault();

    taskChangeField.classList.add("text-decoration-line-through");
})