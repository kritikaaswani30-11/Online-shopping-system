let cart = [];
let total = 0;

function showSection(sectionId) {
    let sections = document.querySelectorAll('.section');
    sections.forEach(section => section.style.display = 'none');
    document.getElementById(sectionId).style.display = 'block';
}

function addToCart(productName, price) {
    cart.push({ name: productName, price: price });
    total += price;
    alert(productName + " added to cart");
    updateCart();
}

function updateCart() {
    let cartItems = document.getElementById('cartItems');
    cartItems.innerHTML = "";

    cart.forEach(item => {
        let li = document.createElement('li');
        li.textContent = item.name + " - ₹" + item.price;
        cartItems.appendChild(li);
    });

    document.getElementById('totalPrice').innerText = "Total: ₹" + total;
}

function placeOrder() {
    if (cart.length === 0) {
        alert("Cart is empty");
    } else {
        alert("Order placed successfully!");
        cart = [];
        total = 0;
        updateCart();
    }
}
