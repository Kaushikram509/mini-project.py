document.addEventListener("DOMContentLoaded", () => {

    const sections = document.querySelectorAll("main section");
    const navLinks = document.querySelectorAll("nav a");

    // Hide all sections
    function hideAllSections() {
        sections.forEach(section => {
            section.style.display = "none";
        });
    }

    // Remove active class from all buttons
    function removeActiveClass() {
        navLinks.forEach(link => {
            link.classList.remove("active");
        });
    }

    // Add click event to each nav button
    navLinks.forEach(link => {
        link.addEventListener("click", function(e) {
            e.preventDefault();

            const targetId = this.getAttribute("href").substring(1);
            const targetSection = document.getElementById(targetId);

            if (!targetSection) return;

            hideAllSections();
            removeActiveClass();

            targetSection.style.display = "block";
            this.classList.add("active");
        });
    });

    // Default section on page load
    hideAllSections();

    const defaultSection = document.getElementById("about");
    if (defaultSection) {
        defaultSection.style.display = "block";
    }

    if (navLinks.length > 0) {
        navLinks[0].classList.add("active");
    }

});
