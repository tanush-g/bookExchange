// BookExchange - Add Book Step 2 JavaScript
// Handles showing/hiding genre input fields

document.addEventListener('DOMContentLoaded', function() {
    const noneOfTheAbove = document.querySelector("#none");
    const genresContainer = document.querySelector(".genres");
    
    if (!noneOfTheAbove) {
        console.error('None of the above radio button not found');
        return;
    }
    
    if (!genresContainer) {
        console.error('Genres container not found');
        return;
    }

    noneOfTheAbove.addEventListener("click", function() {
        genresContainer.classList.remove("hidden");
    });
});
