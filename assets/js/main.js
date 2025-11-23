// Haken-Breien-Shop.nl - MVP JavaScript

document.addEventListener('DOMContentLoaded', function() {
  
  // Mobile Navigation Toggle
  const navToggle = document.querySelector('.main-nav__toggle');
  const navList = document.querySelector('.main-nav__list');
  
  if (navToggle && navList) {
    navToggle.addEventListener('click', function() {
      const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
      
      navToggle.setAttribute('aria-expanded', !isExpanded);
      navList.classList.toggle('active');
      navToggle.textContent = isExpanded ? 'Menu' : 'Sluiten';
    });
  }
  
  // FAQ Accordion
  const faqQuestions = document.querySelectorAll('.faq-question');
  
  faqQuestions.forEach(question => {
    question.addEventListener('click', function() {
      const answer = this.nextElementSibling;
      const isActive = answer.classList.contains('active');
      
      // Close all other FAQ items
      document.querySelectorAll('.faq-answer').forEach(item => {
        item.classList.remove('active');
      });
      
      // Toggle current item
      if (!isActive) {
        answer.classList.add('active');
      }
    });
  });
  
  // Smooth scroll for anchor links
  const anchorLinks = document.querySelectorAll('a[href^="#"]');
  
  anchorLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      const targetElement = document.querySelector(targetId);
      
      if (targetElement) {
        e.preventDefault();
        targetElement.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
  
  // Affiliate link tracking (Google Analytics)
  const affiliateLinks = document.querySelectorAll('a[rel*="sponsored"]');
  
  affiliateLinks.forEach(link => {
    link.addEventListener('click', function() {
      const productName = this.closest('.card')?.querySelector('h2, h3')?.textContent || 'Unknown Product';
      const platform = this.href.includes('bol.com') ? 'Bol.com' : 'Amazon';
      
      // Google Analytics 4 event tracking
      if (typeof gtag !== 'undefined') {
        gtag('event', 'affiliate_click', {
          'product_name': productName,
          'platform': platform,
          'link_url': this.href
        });
      }
    });
  });
  
});
