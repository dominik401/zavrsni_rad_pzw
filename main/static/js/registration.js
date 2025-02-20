document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const passwordField = document.querySelector("#id_password1");
    const confirmPasswordField = document.querySelector("#id_password2");

    form.addEventListener("submit", function (event) {
        let errors = [];

        if (passwordField.value.length < 8) {
            errors.push("Lozinka mora imati najmanje 8 znakova.");
        }
        if (!/[A-Z]/.test(passwordField.value)) {
            errors.push("Lozinka mora sadržavati barem jedno veliko slovo.");
        }
        if (!/\d/.test(passwordField.value)) {
            errors.push("Lozinka mora sadržavati barem jedan broj.");
        }
        if (!/[!@#$%^&*]/.test(passwordField.value)) {
            errors.push("Lozinka mora sadržavati barem jedan posebni znak (!@#$%^&*).");
        }
        if (passwordField.value !== confirmPasswordField.value) {
            errors.push("Lozinke se ne podudaraju.");
        }

        if (errors.length > 0) {
            event.preventDefault();
            alert(errors.join("\n"));
        }
    });
});
