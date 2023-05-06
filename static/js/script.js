window.addEventListener ('DOMContentLoaded', () => {

    const slides = document.querySelectorAll('.stocks__slide'), //каждый слайд
          prev = document.querySelector('.stocks__slider-prev'),
          next = document.querySelector('.stocks__slider-next'),
          slidesWrapper = document.querySelector('.stocks__slider-wrapper'), // - главная обертка слайдера
          slidesField = document.querySelector('.stocks__slider-inner'), //- поле с нашими слайдами - ообертка
          width = window.getComputedStyle(slidesWrapper).width; // - получаем ширину обертку, которая показывает ширину

    // let slideIndex = 1;
    let offset = 0; // - отступ чтоб понимать на сколько мы отсутпили вправо или влево

    slidesField.style.width = 100  * slides.length + '%'; // - чтоб поместить все слайды которые есть на странице мы помещаем в обетку
    slidesField.style.display = 'flex'; //- делаем нашу обертку в горищонтальное положение
    slidesField.style.transition = '0.5s all'; // и добавляем плавность

    slidesWrapper.style.overflow = 'hidden';


    slides.forEach(slide => {
        slide.style.width = width;
    }); // - все слайдам задаем нужную нам ширину что они не вылезали за главную обертку

    function nextSlide() {
        if (offset == +width.slice(0, width.length - 2) * (slides.length - 1)) {
            // ширина одного слайда умноженное на количество слайдов
            // Width - 900px, нам надо убрать px ---- +width.slice(0, width.length - 2) = 900
            offset = 0; // = это если мы дошли в конецц
        } else {
            offset += +width.slice(0, width.length - 2)  //-это если надо в начало
        }

        slidesField.style.transform = `translateX(-${offset}px)`;  // - как мы сдвигаем наш слайд и на сколько процентов за это отвечает офсет
    }

    setInterval(() => {
        nextSlide();
    }, 15000);

    next.addEventListener('click', () => {
        nextSlide();
    });

    slides.forEach(slide => {
        slide.style.width = width;
    }); // - все слайдам задаем нужную нам ширину что они не вылезали за главную обертку


    prev.addEventListener('click', () => {
        if ( offset == 0) {
            offset = +width.slice(0, width.length - 2) * (slides.length - 1)
                    // ширина одного слайда умноженное на количество слайдов
        } else {
            offset -= +width.slice(0, width.length - 2)  //-это если надо в начало
        }

        slidesField.style.transform = `translateX(-${offset}px)`;  // - как мы сдвигаем наш слайд и на сколько процентов за это отвечает офсет
    });



    // tabs

    let button = document.querySelectorAll('.menu__tab')
    let  photoes = document.querySelectorAll('.menu__content')

    for (let i = 0; i < button.length; i++){
        button[i].addEventListener ('click', function() {
            for(let j = 0; j < button.length; j++) {
                button[j].classList.remove('menu__tab-active')
            }
            this.classList.add('menu__tab-active')
        })
    }

    function myapp() {
        const buttons = document.querySelectorAll(".menu__tab");
        const cards = document.querySelectorAll(".menu__content");

        function filter(category, items) {
        items.forEach((item) => {
            const isItemFiltered = !item.classList.contains(category);
            const isShowAll = category.toLowerCase() === "all";
            if (isItemFiltered && !isShowAll) {
                item.classList.add("hide");
                item.classList.add("fade");
            } else {
                item.classList.remove("hide");
                item.classList.add("fade");
            }
        });
        }

        buttons.forEach((button) => {
        button.addEventListener("click", () => {
            const currentCategory = button.dataset.filter;
            console.log(currentCategory);
            filter(currentCategory, cards);
        });
        });
    }

    myapp();



    // Modal

    const modalTrigger = document.querySelectorAll('[data-modal]'),
          modal = document.querySelector('.modal');

    function openModal() {
        modalTrigger.forEach((item) => {
            item.addEventListener('click', () => {
                if (modal.classList.contains('hide')) {
                    modal.classList.remove('hide');
                    modal.classList.add('fade');
                }
            });
        });
    }

    function closeModal() {
        modal.classList.add('hide');
        modal.classList.remove('fade');
        document.body.style.overflow = '';
    }

    document.addEventListener('keydown', (e) => {
        if (e.code == 'Escape' && !modal.classList.contains('hide')) {
            closeModal();
        }
    });





    closeModal();
    openModal();














    // showSlides(slideIndex);

    // function showSlides(n) {
    //     if (n > slides.length) {
    //         slideIndex = 1;
    //     }

    //     if ( n < 1) {
    //         slideIndex = slides.length
    //     }

    //     slides.forEach(item => item.style.display ='none');

    //     slides[slideIndex - 1].style.display ='block';
    // }

    // // в функции мы показываем нам нужный слайд, и если наш слайд больше количества слайдов то возвращаемся к первому, если наоборот то к последнему
    // // каждому слайду мы ставим дсплэй нон, а нужному нам дисплэй блок, для отображения

    // function plusSlides(n) {
    //     showSlides(slideIndex += n);
    // }

    // prev.addEventListener('click', () => {
    //     plusSlides(-1);
    // });

    // next.addEventListener('click', () => {
    //     plusSlides(1);
    // });

});