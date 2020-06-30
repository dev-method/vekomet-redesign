window.onscroll = function() {
    stickyFunction();
    toTopFunction();
};
var navbarDev = document.getElementById("navbar");
var mob_navbar = document.getElementById("mobile-navbar");
var sticky = navbarDev.offsetTop;
var mob_sticky = mob_navbar.offsetTop;

function stickyFunction() {
    if (window.pageYOffset > sticky) {
        navbarDev.classList.add("sticky");
        navbarDev.style.height = "50px";
    } else {
        navbarDev.classList.remove("sticky");
        navbarDev.style.height = "70px";
    }
    if (window.pageYOffset > mob_sticky) {
        mob_navbar.classList.add("sticky");
    } else {
        mob_navbar.classList.remove("sticky");
    }
}
toTopButton = document.getElementById("toTopButton");

function toTopFunction() {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        toTopButton.style.display = "block";
    } else {
        toTopButton.style.display = "none";
    }
}
var phone_modal = document.getElementById('phone-modal');
var ph_icon_wide = document.getElementById('phone-icon-wide');
var ph_modal_close = document.getElementById('ph-modal-close');
var form_modal = document.getElementById('form-modal');
var form_icon_wide = document.getElementById('form-icon-wide');
var footer_button = document.getElementById('footer-button');
var f_modal_close = document.getElementById('f-modal-close');
ph_icon_wide.onclick = function() {
    phone_modal.style.display = "block"
};
ph_modal_close.onclick = function() {
    phone_modal.style.display = "none"
};
form_icon_wide.onclick = function() {
    form_modal.style.display = "block"
};
footer_button.onclick = function() {
    form_modal.style.display = "block"
};
f_modal_close.onclick = function() {
    form_modal.style.display = "none"
};
var menu_icon = document.getElementById("nav-icon3");
var menu = document.getElementById("mobile-menu");
var topbar = document.getElementById("topbar-container");
var phone_block = document.getElementById("phone-block");
var phone_pointer = document.getElementById("phone-block-pointer");
var slide = document.getElementById("sliding-container");
var form_block = document.getElementById("hidden-form-block");
var form_pointer = document.getElementById("form-block-pointer");

function burgerFunction() {
    slide.classList.remove("form-slide-down");
    form_block.classList.remove("form-block-visible");
    form_pointer.classList.remove("form-pointer-visible");
    slide.classList.remove("phone-slide-down");
    phone_block.classList.remove("phone_block_visible");
    phone_pointer.classList.remove("phone-pointer-visible");
    if (menu_icon.classList.contains("open")) {
        menu_icon.classList.remove("open");
        menu.classList.remove("mobile-menu-open");
        slide.style.marginTop = "0";
        topbar.style.display = "flex"
    } else {
        menu_icon.classList.add("open");
        menu.classList.add("mobile-menu-open");
        topbar.style.display = "none";
        if (window.scrollY === 0) {
            var h = String(menu.scrollHeight - 2);
            slide.style.marginTop = h + "px";
        }
    }
}

function togglePhoneBlock() {
    form_block.classList.remove("form-block-visible");
    form_pointer.classList.remove("form-pointer-visible");
    if (phone_block.classList.contains("phone_block_visible")) {
        phone_pointer.classList.remove("phone-pointer-visible");
        phone_block.classList.remove("phone_block_visible");
        slide.style.marginTop = "0";
    } else {
        phone_pointer.classList.add("phone-pointer-visible");
        phone_block.classList.add("phone_block_visible");
        slide.style.marginTop = String(phone_block.scrollHeight) + "px";
    }
}

function toggleFormBlock() {
    phone_block.classList.remove("phone_block_visible");
    phone_pointer.classList.remove("phone-pointer-visible");
    if (form_block.classList.contains("form-block-visible")) {
        form_block.classList.remove("form-block-visible");
        form_pointer.classList.remove("form-pointer-visible");
        slide.style.marginTop = "0";
    } else {
        form_block.classList.add("form-block-visible");
        form_pointer.classList.add("form-pointer-visible");
        slide.style.marginTop = slide.style.marginTop = String(form_block.scrollHeight) + "px";
    }
}

function toggleMobileMenuItem(item, open, close, hidden) {
    var pointer = document.getElementById(item);
    var open_icon = document.getElementById(open);
    var close_icon = document.getElementById(close);
    var hidden_item = document.getElementById(hidden);
    if (pointer.classList.contains("open-collapse")) {
        open_icon.style.display = "block";
        close_icon.style.display = "none";
        hidden_item.style.display = "none";
        pointer.classList.remove("open-collapse");
        if (window.scrollY === 0) {
            slide.style.marginTop = String(menu.scrollHeight - 2) + "px";
        }
    } else {
        pointer.classList.add("open-collapse");
        open_icon.style.display = "none";
        close_icon.style.display = "block";
        hidden_item.style.display = "block";
        if (window.scrollY === 0) {
            slide.style.marginTop = String(menu.scrollHeight - 2) + "px";
        }
    }
}