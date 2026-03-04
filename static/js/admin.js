function togglemenu() {
    const links = document.getElementById("navlinks");
    links.classList.toggle("active");
    console.log("toggled")
}

function showWhiteBox() {
    const box = document.querySelector('.white-box');
    box.classList.toggle('show');
}

document.getElementById("loginForm").addEventListener("submit", function(e) {
      e.preventDefault();

      const empId = document.getElementById("empId").value.trim();
      const password = document.getElementById("password").value.trim();
      const errorMsg = document.getElementById("error-msg");

      const validEmpId = "rinl123";
      const validPassword = "pass123";

      if (empId === validEmpId && password === validPassword) {
       
        localStorage.setItem("loggedIn", "true");
        localStorage.setItem("employeeId", empId);
       
        window.location.href = "";
      } else {
        errorMsg.style.display = "block";
      }
});

 document.getElementById("adminLoginForm").addEventListener("submit", async function(e) {
    e.preventDefault();
    const username = this.username.value;
    const password = this.password.value;

    const res = await fetch("http://127.0.0.1:4000/admin/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    const result = await res.json();
    alert(result.message || result.error);

    if (res.ok) {
        // Redirect to dashboard
        window.location.href = "dashboard.html";
    }
});
