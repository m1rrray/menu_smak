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

    //добавление количество блюд
    const minus = document.querySelector('.button__minus'),
          plus = document.querySelector('.button__plus');
     number = document.querySelector('.button__counter-number');
    let drink = document.querySelector(".modal__title");


    minus.addEventListener('click', () => {
        // minusNumber();
        if (parseInt(number.value) > 1) {
            number.value = parseInt(number.value) - 1;}
    });

    plus.addEventListener('click', () => {
        // plusNumber();
        if (parseInt(number.value) < 15) {
            number.value = parseInt(number.value) + 1;
        }
    })


    // Modal

    const modalTrigger = document.querySelectorAll('[data-modal]'),
          modal = document.querySelector('.modal');

    function openModal() {
        modalTrigger.forEach((item) => {
            item.addEventListener('click', () => {
                if (modal.classList.contains('hide')) {
                    modal.classList.remove('hide');
                    modal.classList.add('fade');
                    // number.innerHTML = counter;
                }
            });
        });
    }

    function closeModal() {
        modal.classList.add('hide');
        modal.classList.remove('fade');
        document.body.style.overflow = '';
        number.value = 1;
    }

    document.addEventListener('keydown', (e) => {
        if (e.code == 'Escape' && !modal.classList.contains('hide')) {
            closeModal();
        }
    });

    document.addEventListener('keydown', (e) => {
        if (e.code == 'Escape' && !modal.classList.contains('hide')) {
            closeModal();
        }
    });// закрыти на нажатие вне escape

    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    }); // закрыти на нажатие вне окна



    closeModal();
    openModal();






    var addButtons = document.querySelectorAll('.button');

    // Добавляем обработчик события клика для каждой кнопки
    addButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        // Получаем информацию о блюде из атрибутов data-*
          var dishPicture = button.dataset.dishPicture;
        var dishId = button.dataset.dishId;
        var dishName = button.dataset.dishName;
        var dishDescription = button.dataset.dishDescription;
        var dishPrice = button.dataset.dishPrice;
        var dishWeight = button.dataset.dishWeight;
        var dishCategory = button.dataset.dishCategory;



        // Отображаем информацию о блюде в модальном окне

          document.querySelector('#my-modal__img-food').src = '/static/img/' + dishPicture;
        document.querySelector('.modal .modal__title').textContent = dishName;
        document.querySelector('.modal .modal__text').textContent = dishDescription;
        document.querySelector('.modal .modal__img-price').textContent = dishPrice + ' ₽';
        if (dishCategory == 'drink')
            document.querySelector('.modal .modal__img-grams').textContent = dishWeight + 'мл' ;
        else
            document.querySelector('.modal .modal__img-grams').textContent = dishWeight + ' г' ;
        document.querySelector('#product_id').value = dishId;

        // Открываем модальное окно
        // document.querySelector('.modal').classList.add('show');
      });
    });















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