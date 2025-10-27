let isEditing = false;

function openNav() {
    const back_menu = document.getElementById('my_menu_back');
    const menu = document.getElementById("myNav");

    // показываем фон и меню
    back_menu.style.display = "block";
    setTimeout(() => {
        back_menu.classList.add("active");
        menu.classList.add("active");
    }, 10); // чуть задержка — для плавного появления

    if (isEditing) {
        document.getElementById("myNavCreate").style.display = "none";
        document.getElementById("myNavCreateOpen").style.display = "block";
    } else {
        document.getElementById("myNavCreate").style.display = "block";
        document.getElementById("myNavCreateOpen").style.display = "none";
    }
}

function closeNav() {
    const back_menu = document.getElementById('my_menu_back');
    const menu = document.getElementById("myNav");

    // плавно скрываем меню
    menu.classList.remove("active");
    back_menu.classList.remove("active");

    setTimeout(() => {
        back_menu.style.display = "none"; // скрываем затемнение после анимации
    }, 300); // время совпадает с transition в CSS

    // сброс состояния
    document.getElementById("myNavCreate").style.display = "none";
    document.getElementById("myNavCreateOpen").style.display = "none";
    isEditing = false;
}

function openBar() {
    isEditing = true;
    document.getElementById("myNavCreate").style.display = "none";
    document.getElementById("myNavCreateOpen").style.display = "block";
}
