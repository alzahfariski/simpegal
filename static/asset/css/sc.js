const navbar = document.getElementsByTagName('nav')[0];
window.addEventListener('scroll',function(){
    if(window.scrollY > 100){
        navbar.classList.replace('bg-transparent', 'navbar-color');
    }else if(this.window.scrollY <= 100){
        navbar.classList.replace('navbar-color', 'bg-transparent');
    }
});