const username_input = document.querySelector("#id_username");
const email_input = document.querySelector('#id_email');
const username_error_area = document.querySelector(".username-errors");
const email_error_area = document.querySelector(".email-errors");
const password1_input = document.querySelector("#id_password1");
const password2_input = document.querySelector("#id_password2");
const passwords_error_area = document.querySelector(".password-errors");

/* Username validation */
username_input.addEventListener('keyup', (e) => {
    const usernameValue = e.target.value;
    if (usernameValue.length > 0){
        fetch("/accounts/validateUsername", {
            body: JSON.stringify({ username: usernameValue }),
            method: "POST",
        })
            .then((res)=>res.json())
            .then((data) => {
            if(data.username_error){
                username_input.classList.add("invalid");
                username_error_area.style.display = 'block';
                username_error_area.innerHTML = `<p>${data.username_error}</p>`
            }else {
                username_input.classList.remove('invalid')
                username_error_area.style.display = 'none';
            }
        });
    }
});

/* Email Validation */
email_input.addEventListener('keyup', (e) => {
    const emailValue = e.target.value;
    if (emailValue.length > 0){
        fetch("/accounts/validateEmail", {
            body: JSON.stringify({ email: emailValue }),
            method: "POST",
        })
            .then((res)=>res.json())
            .then((data) => {
            if(data.email_error){
                email_input.classList.add("invalid");
                email_error_area.style.display = 'block';
                email_error_area.innerHTML = `<p>${data.email_error}</p>`
            }else {
                email_input.classList.remove('invalid')
                email_error_area.style.display = 'none';
            }
        });
    }
});

/* Passwords validation */
password2_input.addEventListener('keyup', (e) => {
    const password2Value = e.target.value;
    const password1Value = password1_input.value;
    if (password2Value.length > 0){
        fetch("/accounts/validatePassword", {
            body: JSON.stringify({ password1: password1Value, password2: password2Value }),
            method: "POST",
        })
            .then((res)=>res.json())
            .then((data) => {
            if(data.password_error){
                password2_input.classList.add("invalid");
                passwords_error_area.style.display = 'block';
                passwords_error_area.innerHTML = `<p>${data.password_error}</p>`
            }else{
                password2_input.classList.remove('invalid')
                passwords_error_area.style.display = 'none';
            }
        });
    }
});
