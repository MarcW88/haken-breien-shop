// Haken-Breien-Shop.nl - Custom JavaScript

document.addEventListener('DOMContentLoaded', function() {
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Track affiliate link clicks
    document.querySelectorAll('a[rel*="sponsored"]').forEach(link => {
        link.addEventListener('click', function() {
            // Track with Google Analytics if available
            if (typeof gtag !== 'undefined') {
                gtag('event', 'click', {
                    'event_category': 'affiliate',
                    'event_label': this.href,
                    'transport_type': 'beacon'
                });
            }
            
            // Optional: Add visual feedback
            this.style.opacity = '0.7';
            setTimeout(() => {
                this.style.opacity = '1';
            }, 200);
        });
    });

    // Lazy loading for images (if not natively supported)
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.classList.remove('lazy');
                        imageObserver.unobserve(img);
                    }
                }
            });
        });

        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }

    // Newsletter form handling (basic validation)
    const newsletterForms = document.querySelectorAll('form');
    newsletterForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const emailInput = this.querySelector('input[type="email"]');
            if (emailInput) {
                const email = emailInput.value.trim();
                if (!isValidEmail(email)) {
                    e.preventDefault();
                    alert('Voer een geldig email adres in.');
                    return false;
                }
                
                // Track newsletter signup
                if (typeof gtag !== 'undefined') {
                    gtag('event', 'newsletter_signup', {
                        'event_category': 'engagement',
                        'event_label': 'newsletter'
                    });
                }
            }
        });
    });

    // Product card hover effects
    document.querySelectorAll('.product-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Back to top button (if needed)
    const backToTopButton = document.createElement('button');
    backToTopButton.innerHTML = '<i class="fas fa-arrow-up"></i>';
    backToTopButton.className = 'btn btn-primary btn-sm position-fixed';
    backToTopButton.style.cssText = 'bottom: 20px; right: 20px; z-index: 1000; display: none; border-radius: 50%; width: 50px; height: 50px;';
    backToTopButton.setAttribute('aria-label', 'Terug naar boven');
    document.body.appendChild(backToTopButton);

    // Show/hide back to top button
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });

    // Back to top functionality
    backToTopButton.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Search functionality (basic)
    const searchInputs = document.querySelectorAll('input[type="search"]');
    searchInputs.forEach(input => {
        input.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                const query = this.value.trim();
                if (query) {
                    // Track search
                    if (typeof gtag !== 'undefined') {
                        gtag('event', 'search', {
                            'search_term': query
                        });
                    }
                    // Redirect to search results (implement as needed)
                    console.log('Searching for:', query);
                }
            }
        });
    });

    // Cookie consent (basic implementation)
    if (!localStorage.getItem('cookieConsent')) {
        showCookieConsent();
    }

    function showCookieConsent() {
        const cookieBanner = document.createElement('div');
        cookieBanner.className = 'alert alert-info position-fixed';
        cookieBanner.style.cssText = 'bottom: 0; left: 0; right: 0; z-index: 1050; margin: 0; border-radius: 0;';
        cookieBanner.innerHTML = `
            <div class="container">
                <div class="d-flex justify-content-between align-items-center">
                    <span>Deze website gebruikt cookies om je ervaring te verbeteren. Door verder te gaan ga je akkoord met ons cookiebeleid.</span>
                    <button type="button" class="btn btn-primary btn-sm ml-3" onclick="acceptCookies()">Akkoord</button>
                </div>
            </div>
        `;
        document.body.appendChild(cookieBanner);
    }

    // Make acceptCookies function global
    window.acceptCookies = function() {
        localStorage.setItem('cookieConsent', 'true');
        const cookieBanner = document.querySelector('.alert.position-fixed');
        if (cookieBanner) {
            cookieBanner.remove();
        }
    };

    // Performance optimization: Preload critical resources
    const criticalResources = [
        '/css/custom.css',
        '/images/hero/hero-haken-breien.jpg'
    ];

    criticalResources.forEach(resource => {
        const link = document.createElement('link');
        link.rel = 'preload';
        link.href = resource;
        link.as = resource.endsWith('.css') ? 'style' : 'image';
        document.head.appendChild(link);
    });
});

// Utility functions
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Error handling for missing images
document.addEventListener('error', function(e) {
    if (e.target.tagName === 'IMG') {
        e.target.src = 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjZGRkIi8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGZvbnQtZmFtaWx5PSJBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZHk9Ii4zZW0iPkFmYmVlbGRpbmcgbmlldCBiZXNjaGlrYmFhcjwvdGV4dD48L3N2Zz4=';
        e.target.alt = 'Afbeelding niet beschikbaar';
    }
}, true);

// Print optimization
window.addEventListener('beforeprint', function() {
    // Hide non-essential elements when printing
    document.querySelectorAll('.navbar, .footer, .btn, .alert').forEach(el => {
        el.style.display = 'none';
    });
});

window.addEventListener('afterprint', function() {
    // Restore elements after printing
    document.querySelectorAll('.navbar, .footer, .btn, .alert').forEach(el => {
        el.style.display = '';
    });
});
