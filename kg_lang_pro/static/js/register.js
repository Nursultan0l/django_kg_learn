document.getElementById("signupForm").addEventListener("submit", async function(e) {
  e.preventDefault();

  const username = document.getElementById("signup_username").value;
  const email = document.getElementById("signup_email").value;
  const password = document.getElementById("signup_password1").value;
  const password2 = document.getElementById("signup_password2").value;

  const response = await fetch("/register/", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({username, email, password, password2})
  });

  const data = await response.json();

  if (response.ok) {
    // сохраняем токены
    localStorage.setItem("access", data.access);
    localStorage.setItem("refresh", data.refresh);
    alert("Регистрация успешна! Добро пожаловать, " + data.user.username);
  } else {
    document.getElementById("signupErrors").innerHTML = JSON.stringify(data);
  }
});