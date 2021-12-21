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