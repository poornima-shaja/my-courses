document.addEventListener("DOMContentLoaded", () => {

  console.log("main.js loaded");

  /* 🔹 NAVBAR (ignore for now) */
  const hamburger = document.getElementById("hamburger");
  const navbar = document.querySelector(".navbar");

  hamburger.addEventListener("click", () => {
    navbar.classList.toggle("active");
  });

  const sareeContainer = document.getElementById("saree-container");
  const collectionContainer = document.getElementById("collection-container");

  let allSareesData = []; // store data once

  db.collection("sarees")
    .orderBy("createdAt", "desc")
    .onSnapshot(snapshot => {

      sareeContainer.innerHTML = "";
      collectionContainer.innerHTML = "";
      allSareesData = [];

      snapshot.forEach(doc => {
        const saree = doc.data();
        allSareesData.push(saree);

        /* 🔹 ALL SAREES SECTION (NO FILTER) */
        const allCard = createSareeCard(saree);
        sareeContainer.appendChild(allCard);

        /* 🔹 COLLECTION SECTION (DEFAULT: ALL) */
        const collectionCard = createSareeCard(saree);
        collectionContainer.appendChild(collectionCard);
      });
    });

  /* 🔹 FILTER BUTTONS (COLLECTION ONLY) */
  const filterButtons = document.querySelectorAll(".filter-buttons button");

  filterButtons.forEach(button => {
    button.addEventListener("click", () => {
      const selectedCategory = button.dataset.category;

      collectionContainer.innerHTML = "";

      allSareesData.forEach(saree => {
        if (
          selectedCategory === "All" ||
          saree.category === selectedCategory
        ) {
          const card = createSareeCard(saree);
          collectionContainer.appendChild(card);
        }
      });
    });
  });

});

/* 🔹 CARD CREATOR FUNCTION */
function createSareeCard(saree) {
  const card = document.createElement("div");
  card.classList.add("saree-card");

  card.innerHTML = `
    <img src="${saree.imageUrl}" alt="${saree.name}">
    <h3>${saree.name}</h3>
    <p>Category: ${saree.category}</p>
    <p class="price">₹${saree.price}</p>
    <a class="btn-enquire"
       target="_blank"
       href="https://wa.me/919653149781?text=Hello, I am interested in saree code ${saree.code}">
       Enquire on WhatsApp
    </a>
  `;

  return card;
}
