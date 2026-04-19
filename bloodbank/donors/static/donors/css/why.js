
        
        var fadeElements = document.querySelectorAll('.fade-in');

        // run this function every time the user scrolls
        window.addEventListener('scroll', function() {
            fadeElements.forEach(function(el) {
                // getBoundingClientRect tells us where the element is on screen
                var position = el.getBoundingClientRect().top;
                // if the element is within the visible screen area
                if (position < window.innerHeight - 80) {
                    el.classList.add('visible');
                }
            });
        });

        // also run once on page load in case elements are already visible
        window.dispatchEvent(new Event('scroll'));
    