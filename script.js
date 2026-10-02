/**
 * Buhane Information Technologies
 * Product-network interactions
 */

(function() {
    'use strict';

    document.documentElement.classList.add('js-enabled');

    const PRODUCTS = [
        { slug: 'moodjot', name: 'MoodJot', category: 'app', icon: '/images/products/moodjot.png' },
        { slug: 'vynix', name: 'Vynix', category: 'app', icon: '/images/products/vynix.png' },
        { slug: 'astral-post', name: 'Astral Post', category: 'app', icon: '/images/products/astral-post.png' },
        { slug: 'lastimo', name: 'Lastimo', category: 'app', icon: '/images/products/lastimo.png' },
        { slug: 'leaselore', name: 'LeaseLore', category: 'app', icon: '/images/products/leaselore.png' },
        { slug: 'swipe-slip', name: 'Swipe Slip', category: 'game', icon: '/images/products/swipe-slip.png' },
        { slug: 'glow-spin', name: 'Glow Spin', category: 'game', icon: '/images/products/glow-spin.png' },
        { slug: 'gridzle', name: 'Gridzle', category: 'game', icon: '/images/products/gridzle.png' },
        { slug: 'hoskin', name: 'Hoşkin', category: 'game', icon: '/images/products/hoskin.png' },
        { slug: 'rulr', name: 'RULR', category: 'game', icon: '/images/products/rulr.png' },
        { slug: 'hive-due', name: 'Hive Due / Site Hesap', category: 'saas', icon: '/images/products/hive-due.png' },
        { slug: 'u2m', name: 'U2M URL Shortener', category: 'saas', icon: '/images/products/u2m.png' },
        { slug: 'mintropolis', name: 'Mintropolis', category: 'saas', icon: '/images/products/mintropolis.png' },
        { slug: 'the-cosmic-meta', name: 'The Cosmic Meta', category: 'publication', icon: null }
    ];

    const COPY = {
        en: {
            allProducts: 'All products',
            apps: 'Apps',
            games: 'Games',
            platforms: 'Platforms / Publications',
            kicker: 'Product network',
            title: 'Fourteen available products, grouped by job.',
            summary: 'Open a Buhane product page first, then continue to the verified official destination from there.',
            category: {
                app: 'App',
                game: 'Game',
                saas: 'SaaS',
                publication: 'Publication'
            }
        },
        tr: {
            allProducts: 'Tüm ürünler',
            apps: 'Uygulamalar',
            games: 'Oyunlar',
            platforms: 'Platformlar / Yayınlar',
            kicker: 'Ürün ağı',
            title: 'Yayındaki 14 ürün, işlerine göre gruplanır.',
            summary: 'Önce Buhane ürün sayfasını açın; ardından doğrulanmış resmi adrese oradan geçin.',
            category: {
                app: 'Uygulama',
                game: 'Oyun',
                saas: 'SaaS',
                publication: 'Yayın'
            }
        }
    };

    function getLocale() {
        return document.documentElement.lang && document.documentElement.lang.toLowerCase().startsWith('tr') ? 'tr' : 'en';
    }

    function productBase(locale) {
        return locale === 'tr' ? '/tr/urunler/' : '/products/';
    }

    function productRoute(product, locale) {
        return productBase(locale) + product.slug + '/';
    }

    function closeMobileNav(navLinks, hamburger) {
        if (!navLinks || !hamburger) return;
        navLinks.classList.remove('nav-active');
        hamburger.setAttribute('aria-expanded', 'false');
        hamburger.textContent = '☰';
    }

    function initHeader() {
        const header = document.getElementById('header');
        const hamburger = document.getElementById('hamburger');
        const navLinks = document.getElementById('nav-links');

        function handleHeaderScroll() {
            if (!header) return;
            header.classList.toggle('scrolled', window.scrollY > 50);
        }

        if (header) {
            window.addEventListener('scroll', handleHeaderScroll, { passive: true });
            handleHeaderScroll();
        }

        if (hamburger && navLinks) {
            hamburger.addEventListener('click', function(event) {
                event.preventDefault();
                const isOpen = !navLinks.classList.contains('nav-active');
                navLinks.classList.toggle('nav-active', isOpen);
                hamburger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
                hamburger.textContent = isOpen ? '×' : '☰';
            });

            navLinks.addEventListener('click', function(event) {
                if (event.target.closest('a')) {
                    closeMobileNav(navLinks, hamburger);
                }
            });

            document.addEventListener('click', function(event) {
                if (
                    navLinks.classList.contains('nav-active') &&
                    !navLinks.contains(event.target) &&
                    !hamburger.contains(event.target)
                ) {
                    closeMobileNav(navLinks, hamburger);
                }
            });
        }
    }

    function findProductNavLink(navLinks, locale) {
        const directPath = productBase(locale);
        const links = Array.from(navLinks.querySelectorAll('a'));
        return links.find(function(link) {
            return link.getAttribute('href') === directPath;
        }) || links.find(function(link) {
            const href = link.getAttribute('href') || '';
            return href.indexOf(directPath) === 0;
        });
    }

    function createMegaIcon(product) {
        const icon = document.createElement('span');
        icon.className = 'mega-icon';

        if (product.icon) {
            const image = document.createElement('img');
            image.src = product.icon;
            image.alt = '';
            image.width = 28;
            image.height = 28;
            icon.appendChild(image);
        } else {
            icon.classList.add('mega-icon--initials');
            icon.textContent = 'CM';
        }

        return icon;
    }

    function createMegaLink(product, locale) {
        const copy = COPY[locale];
        const item = document.createElement('li');
        item.className = 'mega-item';

        const link = document.createElement('a');
        link.className = 'mega-link';
        link.href = productRoute(product, locale);
        link.dataset.productId = product.slug;

        const text = document.createElement('span');
        const name = document.createElement('strong');
        const meta = document.createElement('span');
        name.textContent = product.name;
        meta.textContent = copy.category[product.category];
        text.append(name, meta);
        link.append(createMegaIcon(product), text);
        item.appendChild(link);

        return item;
    }

    function createMegaGroup(title, products, locale) {
        const group = document.createElement('section');
        group.className = 'mega-group';

        const heading = document.createElement('h3');
        heading.className = 'mega-group-title';
        heading.textContent = title;

        const list = document.createElement('ul');
        list.className = 'mega-list';
        products.forEach(function(product) {
            list.appendChild(createMegaLink(product, locale));
        });

        group.append(heading, list);
        return group;
    }

    function buildMegaPanel(locale) {
        const copy = COPY[locale];
        const panel = document.createElement('div');
        panel.className = 'mega-panel';
        panel.id = 'mega-products';
        panel.setAttribute('aria-hidden', 'true');
        panel.setAttribute('aria-label', copy.kicker);

        const inner = document.createElement('div');
        inner.className = 'mega-inner';

        const head = document.createElement('div');
        head.className = 'mega-head';

        const kicker = document.createElement('span');
        kicker.className = 'mega-kicker';
        kicker.textContent = copy.kicker;

        const title = document.createElement('p');
        title.className = 'mega-title';
        title.textContent = copy.title;

        const summary = document.createElement('p');
        summary.className = 'mega-summary';
        summary.textContent = copy.summary;

        const all = document.createElement('a');
        all.className = 'mega-all';
        all.href = productBase(locale);
        all.textContent = copy.allProducts;

        head.append(kicker, title, summary, all);

        const grid = document.createElement('div');
        grid.className = 'mega-grid';
        grid.append(
            createMegaGroup(copy.apps, PRODUCTS.filter(function(product) { return product.category === 'app'; }), locale),
            createMegaGroup(copy.games, PRODUCTS.filter(function(product) { return product.category === 'game'; }), locale),
            createMegaGroup(copy.platforms, PRODUCTS.filter(function(product) { return product.category === 'saas' || product.category === 'publication'; }), locale)
        );

        inner.append(head, grid);
        panel.appendChild(inner);
        return panel;
    }

    function initMegaMenu() {
        const header = document.getElementById('header');
        const navLinks = document.getElementById('nav-links');
        const hamburger = document.getElementById('hamburger');
        if (!header || !navLinks || navLinks.querySelector('.nav-mega-toggle')) return;

        const locale = getLocale();
        const productLink = findProductNavLink(navLinks, locale);
        if (!productLink) return;

        const item = productLink.closest('li');
        if (!item) return;

        const originalLabel = productLink.textContent.trim() || COPY[locale].allProducts;
        const button = document.createElement('button');
        button.className = 'nav-mega-toggle';
        button.type = 'button';
        button.setAttribute('aria-controls', 'mega-products');
        button.setAttribute('aria-expanded', 'false');
        button.innerHTML = '<span>' + originalLabel + '</span><span class="nav-mega-caret" aria-hidden="true"></span>';

        item.classList.add('nav-mega-item');
        item.replaceChildren(button);

        const scrim = document.createElement('div');
        scrim.className = 'nav-scrim';
        scrim.setAttribute('aria-hidden', 'true');

        const panel = buildMegaPanel(locale);
        header.after(scrim, panel);

        let closeTimer = null;

        function isOpen() {
            return panel.classList.contains('is-open');
        }

        function cancelScheduledClose() {
            if (closeTimer) {
                window.clearTimeout(closeTimer);
                closeTimer = null;
            }
        }

        function openPanel(focusFirst) {
            cancelScheduledClose();
            panel.classList.add('is-open');
            scrim.classList.add('is-open');
            panel.setAttribute('aria-hidden', 'false');
            button.setAttribute('aria-expanded', 'true');
            closeMobileNav(navLinks, hamburger);

            if (focusFirst) {
                const firstLink = panel.querySelector('a');
                if (firstLink) firstLink.focus();
            }
        }

        function closePanel(returnFocus) {
            cancelScheduledClose();
            panel.classList.remove('is-open');
            scrim.classList.remove('is-open');
            panel.setAttribute('aria-hidden', 'true');
            button.setAttribute('aria-expanded', 'false');

            if (returnFocus) {
                button.focus();
            }
        }

        function scheduleClose() {
            cancelScheduledClose();
            closeTimer = window.setTimeout(function() {
                closePanel(false);
            }, 180);
        }

        button.addEventListener('click', function(event) {
            event.preventDefault();
            if (isOpen()) {
                closePanel(false);
            } else {
                openPanel(false);
            }
        });

        button.addEventListener('keydown', function(event) {
            if (event.key === 'ArrowDown') {
                event.preventDefault();
                openPanel(true);
            }
        });

        panel.addEventListener('keydown', function(event) {
            if (event.key === 'Escape') {
                event.preventDefault();
                closePanel(true);
            }
        });

        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape' && isOpen()) {
                closePanel(true);
            }
        });

        document.addEventListener('click', function(event) {
            if (!isOpen()) return;
            if (panel.contains(event.target) || button.contains(event.target)) return;
            closePanel(false);
        });

        scrim.addEventListener('click', function() {
            closePanel(false);
        });

        panel.addEventListener('focusin', cancelScheduledClose);
        panel.addEventListener('focusout', function(event) {
            if (!panel.contains(event.relatedTarget) && event.relatedTarget !== button) {
                scheduleClose();
            }
        });
    }

    function initActiveNavLinks() {
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('.nav-links a');
        if (!sections.length || !navLinks.length) return;

        function setActiveNavLink() {
            const scrollPosition = window.scrollY + 100;

            sections.forEach(function(section) {
                const sectionTop = section.offsetTop;
                const sectionBottom = sectionTop + section.offsetHeight;
                const sectionId = section.getAttribute('id');

                if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
                    navLinks.forEach(function(link) {
                        link.classList.toggle('active', link.getAttribute('href') === '#' + sectionId);
                    });
                }
            });
        }

        window.addEventListener('scroll', setActiveNavLink, { passive: true });
        setActiveNavLink();
    }

    function initSmoothAnchors() {
        const header = document.getElementById('header');
        document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
            anchor.addEventListener('click', function(event) {
                const targetId = anchor.getAttribute('href');
                if (!targetId || targetId === '#') return;

                const target = document.querySelector(targetId);
                if (!target) return;

                event.preventDefault();
                const headerHeight = header ? header.offsetHeight : 0;
                window.scrollTo({
                    top: target.offsetTop - headerHeight,
                    behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'
                });
            });
        });
    }

    function initProductFilters() {
        const filterButtons = document.querySelectorAll('[data-product-filter]');
        const productCards = document.querySelectorAll('[data-product-category]');
        if (!filterButtons.length || !productCards.length) return;

        filterButtons.forEach(function(button) {
            button.addEventListener('click', function() {
                const filter = button.getAttribute('data-product-filter') || 'all';

                filterButtons.forEach(function(item) {
                    const isActive = item === button;
                    item.classList.toggle('is-active', isActive);
                    item.setAttribute('aria-pressed', isActive ? 'true' : 'false');
                });

                productCards.forEach(function(card) {
                    const category = card.getAttribute('data-product-category');
                    const shouldShow = filter === 'all' || category === filter;
                    card.hidden = !shouldShow;
                    card.classList.toggle('is-filtered-out', !shouldShow);
                    card.setAttribute('aria-hidden', shouldShow ? 'false' : 'true');
                });
            });
        });
    }

    function animateCounters() {
        const statNumbers = document.querySelectorAll('.stat-number');
        if (!statNumbers.length) return;

        const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        if (reduceMotion || !('IntersectionObserver' in window)) return;

        const locale = getLocale() === 'tr' ? 'tr-TR' : 'en';
        const formatter = new Intl.NumberFormat(locale);

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (!entry.isIntersecting) return;

                const target = entry.target;
                const original = target.textContent.trim();
                const value = parseInt(original.replace(/[^0-9]/g, ''), 10);
                if (Number.isNaN(value) || original.indexOf('/') >= 0) {
                    observer.unobserve(target);
                    return;
                }

                const suffix = original.indexOf('+') >= 0 ? '+' : '';
                const startedAt = performance.now();
                const duration = 1200;

                function tick(now) {
                    const progress = Math.min((now - startedAt) / duration, 1);
                    const eased = 1 - Math.pow(1 - progress, 3);
                    target.textContent = formatter.format(Math.round(value * eased)) + suffix;

                    if (progress < 1) {
                        window.requestAnimationFrame(tick);
                    }
                }

                target.textContent = '0' + suffix;
                window.requestAnimationFrame(tick);
                observer.unobserve(target);
            });
        }, { threshold: 0.55 });

        statNumbers.forEach(function(stat) {
            observer.observe(stat);
        });
    }

    function initDetailProductMark() {
        const match = window.location.pathname.match(/\/(?:products|tr\/urunler)\/([^/]+)\/$/);
        if (!match) return;

        const product = PRODUCTS.find(function(item) {
            return item.slug === match[1];
        });
        if (!product) return;

        const hero = document.querySelector('.detail-hero .detail-narrow');
        if (!hero || hero.querySelector('.detail-product-mark')) return;

        const locale = getLocale();
        const copy = COPY[locale];
        const mark = document.createElement('div');
        mark.className = 'detail-product-mark';
        mark.dataset.productId = product.slug;

        const icon = document.createElement('span');
        icon.className = 'detail-product-mark__icon';

        if (product.icon) {
            const image = document.createElement('img');
            image.src = product.icon;
            image.alt = '';
            image.width = 48;
            image.height = 48;
            icon.appendChild(image);
        } else {
            icon.classList.add('detail-product-mark__icon--initials');
            icon.textContent = 'CM';
        }

        const text = document.createElement('span');
        text.className = 'detail-product-mark__text';
        const name = document.createElement('strong');
        const category = document.createElement('span');
        category.className = 'detail-product-mark__category';
        name.textContent = product.name;
        category.textContent = copy.category[product.category];
        text.append(name, category);
        mark.append(icon, text);

        const breadcrumb = hero.querySelector('.breadcrumb');
        if (breadcrumb) {
            breadcrumb.after(mark);
        } else {
            hero.prepend(mark);
        }
    }

    function init() {
        initHeader();
        initMegaMenu();
        initActiveNavLinks();
        initSmoothAnchors();
        initProductFilters();
        animateCounters();
        initDetailProductMark();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
