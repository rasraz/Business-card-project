let navBtn = document.querySelector(".nav__toggle-icon")
let mobileMenu = document.querySelector(".mobile-menu")
let skillsCaption = document.querySelectorAll (".skills-caption")
let skillsHoverShape = document.querySelectorAll(".resume__overall-skills-caption-icon-shape")
const firstClassCaption = document.querySelector(".first")
const secondClassCaption = document.querySelector(".second")
const thirdClassCaption = document.querySelector(".third")
const forthClassCaption = document.querySelector(".forth")
const fifthClassCaption = document.querySelector(".fifth")
const firstHover = document.querySelector(".firstHover")
const secondHover = document.querySelector(".secondHover")
const thirdHover = document.querySelector(".thirdHover")
const forthHover = document.querySelector(".forthHover")
const fifthHover = document.querySelector(".fifthHover")
const portfolioItems = document.querySelectorAll (".portfolio__headers__list__items")
let flag = true
let amir = true
navBtn.addEventListener("click", function(){      
navBtn.classList.toggle("nav__toggle-icon--open")
if (flag) {
    mobileMenu.style.display = "block"
    mobileMenu.style.height = "100%"
    mobileMenu.style.opacity = "1"
    mobileMenu.style.overflow = "visible"
    flag = false
}
    else {
        mobileMenu.style.display = "none"
        mobileMenu.style.height = "0"
        mobileMenu.style.opacity = "0"
        mobileMenu.style.overflow = "hidden"
        flag = true
    }
    window.classList.add("cover")
})
function firstCaptionClick(){
    skillsHoverShape.forEach(function(skill){
        skill.classList.remove("hover-shape")
    })
    skillsCaption.forEach(function(skill){
        skill.classList.remove("skills-caption--white-caption")
    })
    firstClassCaption.classList.toggle("skills-caption--white-caption")
    firstHover.classList.toggle("hover-shape")
    
}
function secondCaptionClick(){
    skillsHoverShape.forEach(function(skill){
        skill.classList.remove("hover-shape")
    })
    skillsCaption.forEach(function(skill){
        skill.classList.remove("skills-caption--white-caption")
    })
    secondClassCaption.classList.toggle("skills-caption--white-caption")
    secondHover.classList.toggle("hover-shape")
}
function thirdCaptionClick(){
    skillsHoverShape.forEach(function(skill){
        skill.classList.remove("hover-shape")
    })
    skillsCaption.forEach(function(skill){
        skill.classList.remove("skills-caption--white-caption")
    })
    thirdClassCaption.classList.toggle("skills-caption--white-caption")
    thirdHover.classList.toggle("hover-shape")
}
function forthCaptionClick(){
    skillsHoverShape.forEach(function(skill){
        skill.classList.remove("hover-shape")
    })
    skillsCaption.forEach(function(skill){
        skill.classList.remove("skills-caption--white-caption")
    })
    forthClassCaption.classList.toggle("skills-caption--white-caption")
    forthHover.classList.toggle("hover-shape")
}
function fifthCaptionClick(){
    skillsHoverShape.forEach(function(skill){
    skill.classList.remove("hover-shape")
    })
    skillsCaption.forEach(function(skill){
        skill.classList.remove("skills-caption--white-caption")
    })
    fifthClassCaption.classList.toggle("skills-caption--white-caption")
    fifthHover.classList.toggle("hover-shape")
}

skillsCaption.forEach(function(caption){
    caption.addEventListener("click" , function(){
        document.querySelector(".resume__details--show").classList.remove("resume__details--show")
        let contentId = this.getAttribute("data-content-id")
        document.querySelector(contentId).classList.add("resume__details--show")
    })
})
portfolioItems.forEach(function(item){
    item.addEventListener("click" , function(){
        document.querySelector(".portfolio__headers__list__items--active").classList.remove("portfolio__headers__list__items--active")
        item.classList.add("portfolio__headers__list__items--active")
        document.querySelector(".show").classList.remove("show")
        let portfolioId = this.getAttribute("data-content-id")
        document.querySelector(portfolioId).classList.add("show")
    })
})
// siwper

const swiper = new Swiper('.swiper',{
    pagination: {
        el: '.swiper-pagination',
    },
    breakpoints: {
        768 : {
          slidesPerView: 2,
          spaceBetween: 30

        },
        1200: {
          slidesPerView: 3,
          spaceBetween: 30          
        },
      }
});
