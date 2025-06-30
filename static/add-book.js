// BookExchange - Add Book Form JavaScript
// Handles dynamic form field updates based on transaction type selection

document.addEventListener('DOMContentLoaded', function() {
    const lendRadio = document.getElementById("lend");
    const sellRadio = document.getElementById("sell");
    const exchangeRadio = document.getElementById("exchange");
    
    // Check if elements exist before adding event listeners
    if (!lendRadio || !sellRadio || !exchangeRadio) {
        console.error('Transaction type radio buttons not found');
        return;
    }

    const priceContainer = document.querySelector(".price");
    const numOfDaysContainer = document.querySelector(".num-of-days");
    const exchangeDescContainer = document.querySelector(".exchange-description");
    
    if (!priceContainer || !numOfDaysContainer || !exchangeDescContainer) {
        console.error('Form containers not found');
        return;
    }

    // Lending/Borrowing option
    lendRadio.addEventListener("click", function() {
        if (lendRadio.checked) {
            priceContainer.innerHTML = '<div class="form-group"><label for="price"><b>Daily rental price ($)</b></label><input type="number" step="0.01" placeholder="Enter price per day" name="price" required min="0" max="999.99"></div>';
            numOfDaysContainer.innerHTML = '<div class="form-group"><label for="num-of-days"><b>Maximum lending period (days)</b></label><input type="number" placeholder="Enter maximum days" name="num-of-days" required min="1" max="365"></div>';
            exchangeDescContainer.innerHTML = "";
        }
    });

    // Selling/Buying option
    sellRadio.addEventListener("click", function() {
        if (sellRadio.checked) {
            priceContainer.innerHTML = '<div class="form-group"><label for="price"><b>Selling price ($)</b></label><input type="number" step="0.01" placeholder="Enter selling price" name="price" required min="0" max="9999.99"></div>';
            numOfDaysContainer.innerHTML = "";
            exchangeDescContainer.innerHTML = "";
        }
    });

    // Exchange option
    exchangeRadio.addEventListener("click", function() {
        if (exchangeRadio.checked) {
            priceContainer.innerHTML = "";
            numOfDaysContainer.innerHTML = "";
            exchangeDescContainer.innerHTML = '<div class="form-group"><label for="exchange-description"><b>Exchange description</b></label><textarea placeholder="Describe the condition of your book and what you want to exchange it for" name="exchange-description" required maxlength="500" rows="3"></textarea></div>';
        }
    });
});