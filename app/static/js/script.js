// Particles.js configuration and initialization
function initParticles() {
    if (typeof particlesJS !== 'undefined' && document.getElementById('particles-js')) {
        particlesJS('particles-js', {
            particles: {
                number: { 
                    value: 80, 
                    density: { 
                        enable: true, 
                        value_area: 800 
                    } 
                },
                color: { 
                    value: '#00f3ff' 
                },
                shape: { 
                    type: 'circle' 
                },
                opacity: { 
                    value: 0.5, 
                    random: true 
                },
                size: { 
                    value: 3, 
                    random: true 
                },
                line_linked: {
                    enable: true,
                    distance: 150,
                    color: '#00f3ff',
                    opacity: 0.4,
                    width: 1
                },
                move: {
                    enable: true,
                    speed: 2,
                    direction: 'none',
                    random: true,
                    straight: false,
                    out_mode: 'out',
                    bounce: false
                }
            },
            interactivity: {
                detect_on: 'canvas',
                events: {
                    onhover: { 
                        enable: true, 
                        mode: 'repulse' 
                    },
                    onclick: { 
                        enable: true, 
                        mode: 'push' 
                    },
                    resize: true
                }
            }
        });
        console.log('🚀 Particles initialized!');
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, initializing effects...');
    
    // Initialize particles
    initParticles();
    
    // Re-init particles when navigating (for SPA-like behavior)
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type === 'childList') {
                const particlesContainer = document.getElementById('particles-js');
                if (particlesContainer && !particlesContainer.hasChildNodes()) {
                    console.log('Re-initializing particles for new page...');
                    initParticles();
                }
            }
        });
    });
    
    // Start observing
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });

    // Typing effect
    const typingText = document.querySelector('.typing-text');
    if (typingText) {
        const text = typingText.textContent;
        typingText.textContent = '';
        let i = 0;
        
        function typeWriter() {
            if (i < text.length) {
                typingText.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        }
        setTimeout(typeWriter, 1000);
    }

    // Scroll animations
    const scrollObserverOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const scrollObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, scrollObserverOptions);

    // Observe elements for animation
    document.querySelectorAll('.cyber-card, .service-preview-card, .contact-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'all 0.6s ease';
        scrollObserver.observe(card);
    });

    // Mobile menu
    const mobileToggle = document.querySelector('.nav-mobile-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (mobileToggle && navLinks) {
        mobileToggle.addEventListener('click', function() {
            const isDisplayed = navLinks.style.display === 'flex';
            navLinks.style.display = isDisplayed ? 'none' : 'flex';
            mobileToggle.classList.toggle('active');
        });
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // Handle page transitions and re-initialize particles
    window.addEventListener('popstate', function() {
        setTimeout(initParticles, 100);
    });

    console.log('🚀 CYBER PORTFOLIO LOADED! Ready to impress!');
});

// Re-initialize particles when page becomes visible again
document.addEventListener('visibilitychange', function() {
    if (!document.hidden) {
        setTimeout(initParticles, 500);
    }
});

// Add some cyber console logs
console.log(`%c
    ╔═══════════════════════════════╗
    ║       🚀 KENTIY DEV          ║
    ║    ELITE PYTHON DEVELOPER     ║
    ║                               ║
    ║  Ready to build something     ║
    ║          LEGENDARY?           ║
    ╚═══════════════════════════════╝
`, 'color: #00f3ff; font-family: monospace; font-size: 12px;');