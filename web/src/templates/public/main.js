let carts = document.querySelectorAll('.add-cart');

let products = [
  {
    name: 'DS03-Frameless Bypass Door',
    tag: 'DS03-Frameless-Bypass-Door-Shower-Door',
    price: 620,
    incart: 0
  },
  {
    name: 'SS01-Headerless Sliding Door 4876',
    tag: 'SS01-Headerless-Sliding-Door-4876-Shower-Door',
    price: 800,
    incart: 0
  },
  {
    name: 'SS01-Headerless Sliding Door 6076',
    tag: 'SS01-Headerless-Sliding-Door-6076-Shower-Door',
    price: 850,
    incart: 0
  },
  {
    name: 'SS01-Headerless Sliding Door 7176',
    tag: 'SS01-Headerless-Sliding-Door-7176-Shower-Door',
    price: 960,
    incart: 0
  },
  {
    name: 'Spadet Tiolet',
    tag: 'Spadet-Tiolet',
    price: 850,
    incart: 0
  },
  {
    name: 'Laguna II Tiolet',
    tag: 'Laguna-II-Tiolet',
    price: 110,
    incart: 0
  },
  {
    name: 'Brooks Sink',
    tag: 'Brooks-Sink',
    price: 65,
    incart: 0
  }
]

for(let i = 0; i < carts.length; i++){
   carts[i].addEventListener('click', () => {
    
      cartNumbers(products[i]);
      totalCost(products[i]);
   }
)}

function onLoadCartNumbers(){
   let productNumbers = localStorage.getItem('cartNumbers');
   if(productNumbers){
      document.querySelector('.cart span').textContent = productNumbers;
   }
}

function cartNumbers(product){
   let productNumbers = localStorage.getItem('cartNumbers');
   
   productNumbers = parseInt(productNumbers);
   if( productNumbers ){
     localStorage.setItem('cartNumbers', productNumbers + 1);
     document.querySelector('.cart span').textContent = productNumbers + 1;
   }
   else{
     localStorage.setItem('cartNumbers', 1);
     document.querySelector('.cart span').textContent = 1;
   }
   
   setItems(product);
}

function setItems(product){
   let cartItems = localStorage.getItem('productsInCart');
   cartItems = JSON.parse(cartItems);
   
   if(cartItems != null){
     if(cartItems[product.tag] == undefined){
        cartItems = {
           ...cartItems,
           [product.tag]: product
        }
        cartItems[product.tag].inCart = 0;
     }
     cartItems[product.tag].inCart += 1;
   }
   else{
      product.inCart = 1;
      cartItems = {
         [product.tag]: product
      }
   }
   
   localStorage.setItem("productsInCart", JSON.stringify(cartItems));
}

function totalCost(product){
   //console.log("the product price is", product.price);
   let cartCost = localStorage.getItem('totalCost');
   
   console.log("My cartCost is ", cartCost);
   console.log(typeof cartCost);
   
   if(cartCost != null){
      cartCost = parseInt(cartCost);
      localStorage.setItem("totalCost", cartCost + product.price);
   }
   else{
      localStorage.setItem("totalCost", product.price);
   }
}

function displayCart(){
   // console.log("running");
   // let finalTotal = 0;
   let cartItems = localStorage.getItem("productsInCart");
   cartItems = JSON.parse(cartItems);
   let productContainer = document.querySelector(".products");
   
   //console.log(cartItems);
   if(cartItems && productContainer){
      // console.log("running");
      productContainer.innerHTML = '';
      Object.values(cartItems).map(item => {
         console.log(item.price);
         // finalTotal += (parseInt(item.price) * parseInt(item.incart));
         productContainer.innerHTML += `
           <div class="product">
             <ion-icon name="close-circle"></ion-icon>
             product: <img src="${item.tag}.JPG">
             <span>${item.name}</span>
           </div>
           <div class="price">price: $${item.price},00</div>
           <div class="quantity">
             <span>quantity: ${item.inCart}</span>
           </div>
           <div class="total">
             total: $${item.inCart * item.price},00
           </div>
         `
      });
      let finalCost = localStorage.getItem('totalCost')
      // console.log("yoyo",finalCost);
      productContainer.innerHTML += `
        <div class="basketTotalContainer">
          <h4 class="basketTotalTitle">
            Basket Total + 10% Tax
          </h4>
          <h4 class="basketTotal">
            $${finalCost},00 + $${finalCost*0.1},00 = $${finalCost*1.1} Contact for discount
          </h4>
        </div>
      `
   }
}

function clearLocalStorage(){
   window.localStorage.clear();
}

function reloadPage(){
   location.reload(); 
}

function executeAsynchronously(functions, timeout) {
  for(var i = 0; i < functions.length; i++) {
    setTimeout(functions[i], timeout);
  }
}

onLoadCartNumbers();
displayCart();