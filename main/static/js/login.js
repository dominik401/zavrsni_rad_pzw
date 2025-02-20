document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const usernameField = document.querySelector("#id_username");
    const passwordField = document.querySelector("#id_password");

    form.addEventListener("submit", function (event) {
        if (usernameField.value.trim() === "" || passwordField.value.trim() === "") {
            event.preventDefault();
            alert("Korisničko ime i lozinka ne mogu biti prazni.");
        }
    });
});
