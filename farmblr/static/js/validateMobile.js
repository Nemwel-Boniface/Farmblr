const phone_number_input = document.querySelector("#id_mobile");
const phone_number_error_area = document.querySelector(".mobile-errors");

/* Phone Number validation */
phone_number_input.addEventListener('keyup', (e) => {
    const phoneNumberValue = e.target.value;
    if (phoneNumberValue.length > 0){
        fetch("/accounts/validateMobile", {
            body: JSON.stringify({ mobile: phoneNumberValue }),
            method: "POST",
        })
            .then((res)=>res.json())
            .then((data) => {
            if(data.mobile_error){
                phone_number_input.classList.add("invalid");
                phone_number_error_area.style.display = 'block';
                phone_number_error_area.innerHTML = `<p>${data.mobile_error}</p>`
            }else {
                phone_number_input.classList.remove('invalid')
                phone_number_error_area.style.display = 'none';
            }
        });
    }
});
