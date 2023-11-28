const usernameField = document.querySelector('#usernameField');
const feedBackArea = document.querySelector('.invalid_feedback');

const emailField = document.querySelector('#emailField');
const emailfeedBackArea = document.querySelector('.emailfeedBackArea');

const usernameSuccessOutput = document.querySelector('.usernameSuccessOutput');

const showPasswordToggle = document.querySelector('.showPasswordToggle');
const passwordField = document.querySelector('#passwordField');

const submitBtn = document.querySelector('.submit-btn');

const handleToggleInput = (e) => {
    if(showPasswordToggle.textContent==='SHOW'){
        showPasswordToggle.textContent = "HIDE";

        passwordField.setAttribute("type", "text");
    }else {
        showPasswordToggle.textContent = "SHOW";

        passwordField.setAttribute("type", "password");
    }
}

showPasswordToggle.addEventListener("click", handleToggleInput);


emailField.addEventListener("keyup", (e) => {
    const emailVal = e.target.value;

    emailField.classList.remove("is-invalid");
    emailfeedBackArea.style.display = "none";

    if (emailVal.length > 0) {
        fetch ("/authentication/validate-email", {
            method: "POST",
            body: JSON.stringify({email : emailVal}),
        })
        .then((res) => res.json())
        .then((data) => {console.log("data", data);
        if (data.email_error) {
            emailField.classList.add("is-invalid");
            emailfeedBackArea.style.display = "block";
            emailfeedBackArea.innerHTML = `<p>${data.email_error}</p>`
            submitBtn.disabled = true;
        }else{
            submitBtn.removeAttribute("disabled");
        }
    })
    };
});



usernameField.addEventListener("keyup", (e) => {
    console.log('22222', 22222);

    const usernameVal = e.target.value;

    usernameSuccessOutput.style.display = "block";

    usernameSuccessOutput.textContent = `${usernameVal}`;

    usernameField.classList.remove("is-invalid");
    feedBackArea.style.display = "none";

    if (usernameVal.length > 0) {
        fetch ("/authentication/validate-username", {
            method: "POST",
            body: JSON.stringify({username : usernameVal}),
        })
        .then((res) => res.json())
        .then((data) => {console.log("data", data);
        usernameSuccessOutput.style.display = "none";

        if (data.username_error) {
            usernameField.classList.add("is-invalid");
            feedBackArea.style.display = "block";
            feedBackArea.innerHTML = `<p>${data.username_error}</p>`
            submitBtn.disabled = true;
        }else{
            submitBtn.removeAttribute("disabled");
        }
    })
    };
});