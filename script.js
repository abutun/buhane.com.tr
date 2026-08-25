/**
 * Buhane Information Technologies
 * Main JavaScript - Animations & Interactions
 */

(function() {
    'use strict';

    document.documentElement.classList.add('js-enabled');

    // DOM Elements
    const header = document.getElementById('header');
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('nav-links');
    const navItems = document.querySelectorAll('.nav-links li a');

    // ============================================
    // Header Scroll Effect
    // ============================================
    function handleHeaderScroll() {
        if (!header) return;

        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }

    if (header) {
        window.addEventListener('scroll', handleHeaderScroll);
        handleHeaderScroll(); // Check on load
    }

    // ============================================
    // Mobile Navigation Toggle
    // ============================================
    if (hamburger && navLinks) {
        hamburger.addEventListener('click', function(e) {
            e.preventDefault();
            navLinks.classList.toggle('nav-active');
            hamburger.setAttribute('aria-expanded', navLinks.classList.contains('nav-active') ? 'true' : 'false');

            // Animate hamburger icon
            if (navLinks.classList.contains('nav-active')) {
                hamburger.innerHTML = '&#10005;'; // X icon
            } else {
                hamburger.innerHTML = '&#9776;'; // Hamburger icon
            }
        });

        // Close menu when clicking a link
        navItems.forEach(function(item) {
            item.addEventListener('click', function() {
                if (navLinks.classList.contains('nav-active')) {
                    navLinks.classList.remove('nav-active');
                    hamburger.innerHTML = '&#9776;';
                    hamburger.setAttribute('aria-expanded', 'false');
                }
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (navLinks.classList.contains('nav-active') &&
                !navLinks.contains(e.target) &&
                !hamburger.contains(e.target)) {
                navLinks.classList.remove('nav-active');
                hamburger.innerHTML = '&#9776;';
                hamburger.setAttribute('aria-expanded', 'false');
            }
        });
    }

    // ============================================
    // Active Navigation Link Highlighting
    // ============================================
    function setActiveNavLink() {
        const sections = document.querySelectorAll('section[id]');
        const scrollPos = window.scrollY + 100;

        sections.forEach(function(section) {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
                navItems.forEach(function(item) {
                    item.classList.remove('active');
                    if (item.getAttribute('href') === '#' + sectionId) {
                        item.classList.add('active');
                    }
                });
            }
        });
    }

    window.addEventListener('scroll', setActiveNavLink);
    setActiveNavLink(); // Check on load

    // ============================================
    // Smooth Scroll for Anchor Links
    // ============================================
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                const headerHeight = header ? header.offsetHeight : 0;
                const targetPosition = targetElement.offsetTop - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ============================================
    // Scroll-Triggered Animations
    // ============================================
    function initScrollAnimations() {
        const fadeElements = document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right');
        const staggerElements = document.querySelectorAll('.stagger-item');

        if (!('IntersectionObserver' in window)) {
            fadeElements.forEach(function(el) { el.classList.add('visible'); });
            staggerElements.forEach(function(el) { el.classList.add('visible'); });
            return;
        }

        const observerOptions = {
            root: null,
            rootMargin: '0px 0px -50px 0px',
            threshold: 0.1
        };

        // Fade-in observer
        const fadeObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    fadeObserver.unobserve(entry.target);
                }
            });
        }, observerOptions);

        fadeElements.forEach(function(el) {
            fadeObserver.observe(el);
        });

        // Stagger animation observer
        const staggerObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    // Find all siblings in the same container
                    const parent = entry.target.parentElement;
                    if (!parent) return;
                    const siblings = parent.querySelectorAll('.stagger-item');

                    siblings.forEach(function(sibling, index) {
                        setTimeout(function() {
                            sibling.classList.add('visible');
                        }, index * 100); // 100ms delay between each item
                    });

                    // Unobserve all siblings
                    siblings.forEach(function(sibling) {
                        staggerObserver.unobserve(sibling);
                    });
                }
            });
        }, observerOptions);

        staggerElements.forEach(function(el) {
            staggerObserver.observe(el);
        });
    }

    // ============================================
    // Parallax Effect for Hero Geometry
    // ============================================
    function initParallax() {
        const heroGeometry = document.querySelector('.hero-geometry');
        if (!heroGeometry) return;

        window.addEventListener('mousemove', function(e) {
            const mouseX = e.clientX / window.innerWidth;
            const mouseY = e.clientY / window.innerHeight;

            const moveX = (mouseX - 0.5) * 18;
            const moveY = (mouseY - 0.5) * 18;

            heroGeometry.style.transform = 'translate(' + moveX + 'px, ' + moveY + 'px)';
        });
    }

    // ============================================
    // Button Ripple Effect
    // ============================================
    function initRippleEffect() {
        const buttons = document.querySelectorAll('.btn, .product-link');

        buttons.forEach(function(button) {
            button.addEventListener('click', function(e) {
                const ripple = document.createElement('span');
                const rect = this.getBoundingClientRect();
                const size = Math.max(rect.width, rect.height);
                const x = e.clientX - rect.left - size / 2;
                const y = e.clientY - rect.top - size / 2;

                ripple.style.cssText =
                    'position: absolute;' +
                    'width: ' + size + 'px;' +
                    'height: ' + size + 'px;' +
                    'left: ' + x + 'px;' +
                    'top: ' + y + 'px;' +
                    'background: rgba(255, 255, 255, 0.3);' +
                    'border-radius: 50%;' +
                    'transform: scale(0);' +
                    'animation: ripple 0.6s ease-out;' +
                    'pointer-events: none;';

                this.appendChild(ripple);

                setTimeout(function() {
                    ripple.remove();
                }, 600);
            });
        });

        // Add ripple animation keyframes
        if (!document.getElementById('ripple-styles')) {
            const style = document.createElement('style');
            style.id = 'ripple-styles';
            style.textContent = '@keyframes ripple { to { transform: scale(4); opacity: 0; } }';
            document.head.appendChild(style);
        }
    }

    // ============================================
    // Counter Animation for Stats
    // ============================================
    function animateCounters() {
        const statNumbers = document.querySelectorAll('.stat-number');

        if (!statNumbers.length || !('IntersectionObserver' in window)) return;

        const counterObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const target = entry.target;
                    const text = target.textContent;
                    const hasPlus = text.includes('+');
                    const isTime = text.includes('/');

                    if (isTime) {
                        // Don't animate "24/7" type values
                        counterObserver.unobserve(target);
                        return;
                    }

                    const number = parseInt(text.replace(/[^0-9]/g, ''));
                    if (isNaN(number)) {
                        counterObserver.unobserve(target);
                        return;
                    }

                    let current = 0;
                    const increment = number / 30;
                    const duration = 1500;
                    const stepTime = duration / 30;

                    const timer = setInterval(function() {
                        current += increment;
                        if (current >= number) {
                            target.textContent = number + (hasPlus ? '+' : '');
                            clearInterval(timer);
                        } else {
                            target.textContent = Math.floor(current) + (hasPlus ? '+' : '');
                        }
                    }, stepTime);

                    counterObserver.unobserve(target);
                }
            });
        }, { threshold: 0.5 });

        statNumbers.forEach(function(stat) {
            counterObserver.observe(stat);
        });
    }

    // ============================================
    // Tilt Effect for Cards
    // ============================================
    function initTiltEffect() {
        const cards = document.querySelectorAll('.service-card, .product-card, .app-card, .stat-card');

        cards.forEach(function(card) {
            card.addEventListener('mousemove', function(e) {
                const rect = this.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                const rotateX = (y - centerY) / 20;
                const rotateY = (centerX - x) / 20;

                this.style.transform = 'perspective(1000px) rotateX(' + rotateX + 'deg) rotateY(' + rotateY + 'deg) translateY(-8px)';
            });

            card.addEventListener('mouseleave', function() {
                this.style.transform = '';
            });
        });
    }

    // ============================================
    // Initialize All Features
    // ============================================
    function init() {
        initScrollAnimations();
        initParallax();
        initRippleEffect();
        animateCounters();
        initTiltEffect();
    }

    // Run initialization when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
