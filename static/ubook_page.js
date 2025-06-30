// BookExchange - Book Page JavaScript
// Handles showing/hiding review form

document.addEventListener('DOMContentLoaded', function() {
    const rateButton = document.getElementById("rate");
    const reviewForm = document.querySelector("form");
    
    if (!rateButton) {
        console.error('Rate button not found');
        return;
    }
    
    if (!reviewForm) {
        console.error('Review form not found');
        return;
    }

    rateButton.addEventListener("click", function() {
        reviewForm.classList.remove("hidden");
        // Scroll to form for better UX
        reviewForm.scrollIntoView({ behavior: 'smooth' });
    });
});