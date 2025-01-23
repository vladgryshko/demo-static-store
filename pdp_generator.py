


template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Product Page - Product </title>
  <link rel="stylesheet" href="../style/style.css">


<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FN1P65M1SP"></script>
<script type="text/javascript" async="" src="https://static.klaviyo.com/onsite/js/klaviyo.js?company_id=Mk9Qwa"></script>
  
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-FN1P65M1SP');
</script>
  
  <style>
    .nosto_product span {
      display: block;
    }
  </style>
  <script src="//connect.nosto.com/include/qsjhb97s"></script>
  
  <script>
  function showPopup(id){
    nostojs(function(api) {
      console.log("showing popup "+id)
      console.log(api.popupCampaigns())
      api.openPopup(id, {preview:true});
    });
  }
    function showPopupFromList(){
        nostojs(function(api) {
          var arrayOfPopupCampaigns = api.popupCampaigns()
          var popupCampaignId = arrayOfPopupCampaigns[0].id
          console.log("showing popup "+popupCampaignId)
          console.log(api.popupCampaigns())
          api.openPopup(popupCampaignId, {preview:true})
        });
  }
    
 function addToCart(){   
 nostojs(api => {
  api.defaultSession()
   .setCart({
     items: [
     
      {
        name: "Product 1",
        price_currency_code: "USD",
        product_id: "1",
        quantity: 1,
        unit_price: 100.00
      }
    ]
   })
   .viewCart()
   .update()
});
 }

</script>

</head>
<body>

<div class="product-page">
  <div class="product-header">
    <img src="https://vladgryshko.github.io/demo-static-store/img/1.webp" alt="Product 1">
    <div>
      <h1>Product 1</h1>
      <p class="price">€100.00</p>
      <p class="description">Demo product 1</p>
      <p>Brand: Demo</p>
      <p>Availability: <span class="badge">In Stock</span></p>
      <p>Material: Cotton</p>
      <p>Weather: Summer</p>
      <p>Type: Top</p>
    </div>
  </div>

  <dl class="details">
    <dt>Category:</dt>
    <dd>/Cat 1, /discount</dd>
    <dt>List Price:</dt>
    <dd>€120.00</dd>
    <dt>Tags:</dt>
    <dd>12345, 33333</dd>
  </dl>

  <div class="sku-list">
    <h2>Available SKUs</h2>

    <div class="sku-item">
      <img src="https://vladgryshko.github.io/demo-static-store/img/1-1.webp" alt="S-Orange">
      <div class="sku-details">
        <h3>S-Orange</h3>
        <p class="price">€1269.00 <del>€1299.00</del></p>
        <p>Size: S</p>
        <p>Color: Orange</p>
        <p>Inventory Level: 55</p>
        <a href="https://vladgryshko.github.io/demo-static-store/products/1.html#/1-size-s/13-color-orange">View Details</a>
      </div>
    </div>

    <div class="sku-item">
      <img src="https://vladgryshko.github.io/demo-static-store/img/1-2.webp" alt="S-Blue">
      <div class="sku-details">
        <h3>S-Blue</h3>
        <p class="price">€1269.00 <del>€1299.00</del></p>
        <p>Size: S</p>
        <p>Color: Blue</p>
        <p>Inventory Level: 12</p>
        <a href="https://vladgryshko.github.io/demo-static-store/products/1.html#/1-size-s/14-color-blue">View Details</a>
      </div>
    </div>
  </div>
</div>



  <input type="button" value="add to cart product 1" onclick='addToCart();'/><br/>
  <input id="popupid" size="40" type="text" value="5ed887c360b2bfe4879c3018"></input>

<input type="button" value="show api popup with preview on" onclick="showPopup(document.getElementById('popupid').value)"/>
<br/>
  <div class="nosto_element" id="top">top2</div>
  <div class="nosto_page_type" style="display:none">product</div>
  <div id="klarna-test">
    klarna-test
    <a href="google.com">Goole</a>
    <br/>
    <a href="nosto.com">Nosto</a>
  </div>
  
  <div id="test-klarna">
    test-klarna
    <a href="google.com">Goole</a>
    <br/>
    <a href="nosto.com">Nosto</a>
  </div>
<div class="nosto_product" style="display: none;">
  <span class="url">https://vladgryshko.github.io/demo-static-store/products/1.html</span>
  <span class="product_id">1</span>
  <span class="name">Product 1</span>
  <span class="image_url">https://vladgryshko.github.io/demo-static-store/img/1.jpg</span>
  <span class="price">100.00</span>
  <span class="price_currency_code">EUR</span>
  <span class="availability">InStock</span>
  <span class="category">/Cat 1</span>
  <span class="category">/discount</span>
  <span class="description">Demo product 1</span>
  <span class="list_price">120</span>
  <span class="brand">Demo</span>
  <span class="tag1">12345</span>
  <span class="tag1">33333</span>
  <span class="custom_fields">
    <span class="material">Cotton</span>
    <span class="weather">Summer</span>
    <span class="pt">top</span>
  </span>
  <span class="nosto_sku">
    <span class="id">1</span>
      <span class="name">S-Orange</span>
      <span class="price">1269.00</span>
      <span class="list_price">1299.00</span>
      <span class="inventory_level">55</span>
      <span class="url">https://vladgryshko.github.io/staging-vlad-store/products/1.html#/1-size-s/13-color-orange</span>
      <span class="image_url">https://vladgryshko.github.io/staging-vlad-store/img/1-1.jpeg</span>
      <span class="availability">InStock</span>
      <span class="custom_fields">
        <span class="size">S</span>
        <span class="color">Orange</span>
      </span>
  </span>

  <span class="nosto_sku">
    <span class="id">2</span>
      <span class="name">S-Blue</span>
      <span class="price">1269.00</span>
      <span class="list_price">1299.00</span>
      <span class="inventory_level">12</span>
      <span class="url">https://vladgryshko.github.io/staging-vlad-store/products/1.html#/1-size-s/14-color-blue</span>
      <span class="image_url">https://vladgryshko.github.io/staging-vlad-store/img/1-2.jpeg</span>
      <span class="availability">InStock</span>
      <span class="custom_fields">
        <span class="size">S</span>
        <span class="color">Blue</span>
      </span>
  </span>
</div>
  <div class="nosto_element" id="bottom">bottom2</div>

  <br/>
<a href="../index.html">Go home</a>
<br/>
</body>
</html>
"""