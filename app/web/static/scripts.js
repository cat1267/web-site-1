document.addEventListener('DOMContentLoaded', () => {
    const links = document.querySelectorAll('nav a');

    for (const link of links) {
        link.addEventListener('click', smoothScroll);
    }

    function smoothScroll(event) {
        event.preventDefault();
        const targetId = event.currentTarget.getAttribute('href').substring(1);
        const targetElement = targetId === 'top' ? document.body : document.getElementById(targetId);
        window.scrollTo({
            top: targetElement === document.body ? 0 : targetElement.offsetTop,
            behavior: "smooth"
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var nav = document.querySelector('nav');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            nav.classList.add('visible');
        } else {
            nav.classList.remove('visible');
        }
    });
});
