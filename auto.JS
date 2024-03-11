document.addEventListener("DOMContentLoaded", function () {
    // Select the loader element
    const loader = document.querySelector(".center");

    // Hide the ring after 3 seconds
    setTimeout(function () {
        loader.style.display = "none";
    }, 3000); 
});


document.addEventListener("DOMContentLoaded", function () {
    // Select the loader element
    const loader = document.querySelector(".center");
    setTimeout(function () {
        loader.style.transition = "opacity 1s ease-out";
        loader.style.opacity = "0";
    }, 3000); 
});

setTimeout(function() {
    const myButton = document.getElementById("myButton");
    myButton.style.display = "block"; 
  }, 3000);


  window.addEventListener("load", function () {
    
    var logo = document.getElementById("logo");

    setTimeout(function () {
     
      logo.classList.remove("hidden");
    }, 3000); 
  });