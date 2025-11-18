function showSection(id) {
  document.querySelectorAll("section").forEach(sec => sec.classList.remove("active"));
  document.getElementById(id).classList.add("active");
}

const members = document.querySelectorAll(".member");
members.forEach(member => {
  member.addEventListener("mouseenter", () => member.style.boxShadow = "0 0 20px #ba68c8");
  member.addEventListener("mouseleave", () => member.style.boxShadow = "0 2px 8px rgba(0,0,0,0.2)");
});

document.querySelectorAll(".ticket-info a").forEach(btn => {
  btn.addEventListener("click", (e) => { e.preventDefault(); document.getElementById("paymentModal").style.display = "flex"; });
});

document.querySelectorAll(".merch-item a").forEach(btn => {
  btn.addEventListener("click", (e) => { e.preventDefault(); document.getElementById("paymentModal").style.display = "flex"; });
});

function closePayment() {
  document.getElementById("paymentModal").style.display = "none";
}

function payTicket() {
  alert("Төлем жасалды! Сізге билет электрондық поштаға жіберіледі.");
  closePayment();
}