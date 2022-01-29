// console.log("Hello Cart");

const cartButton = document.getElementById("addtocart");

// for (let index = 0; index < cart_button.length; index++) {
//   cart_button[index].addEventListener("click", function () {
//     const productId = this.dataset.product;
//     const action = this.dataset.action;
//     console.log("productId:", productId, "Action:", action);

//     console.log("User:", user);

//     if (user === "AnonymousUser") {
//       console.log("Not Logged In");
//     } else {
//       updateUserCart(productId, action);
//     }
//   });
// }

// function updateUserCart(productId, action) {
//   console.log("Logged In");

//   var url = "./cart/update";

//   fetch(url, {
//     method: "POST",
//     headers: {
//       "Content-type": "application/json",
//       "X-CSRFToken": csrftoken,
//     },
//     body: JSON.stringify({ productId: productId, action: action }),
//   })
//     .then((response) => {
//       return response.json();
//     })

//     .then((data) => {
//       console.log("data:", data);
//     });
// }
