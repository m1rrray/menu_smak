window.addEventListener ('DOMContentLoaded', () => {

    // tabs 

    let button = document.querySelectorAll('[data-tab]')

    for (let i = 0; i < button.length; i++){
        button[i].addEventListener ('click', function() {
            for(let j = 0; j < button.length; j++) {
                button[j].classList.remove('login__tab-active')
            }
            this.classList.add('login__tab-active')
        })
    }

    function myapp() {
        const buttons = document.querySelectorAll("[data-tab]");
        const cards = document.querySelectorAll(".login__enter");


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
            filter(currentCategory, cards);
        });
        });
    }
    
    myapp();

    //  forget

    const forgetButton = document.querySelector('[data-forget]'),
          recovery = document.querySelector('.login__recovery'),
          enter = document.querySelector('.login__enter-reg'),
          back = document.querySelector('[data-back]');

    function nextMenu(button, activeMenu, needActiveMenu) {
        button.addEventListener('click', () => {
            if (needActiveMenu.classList.contains('hide')) {
                activeMenu.classList.add('hide','fade');
                needActiveMenu.classList.remove('hide');
            }
        });
    }

    

    function goBack(backButton, activeMenu, needActiveMenu) {
        backButton.addEventListener('click', () => {
            if (!activeMenu.classList.contains('hide')) {
                activeMenu.classList.add('hide');
                needActiveMenu.classList.remove('hide');
            }
        });
    }

    nextMenu(forgetButton, enter, recovery);
    goBack(back, recovery, enter);


    // password

    const openEye = document.querySelectorAll('[data-show]'),
          closeEye = document.querySelectorAll('[data-hide]'),
          enterId = document.getElementById('password__enter'),
          regId = document.getElementById('password__reg'),
          regRepeatId = document.getElementById('password__reg-repeat');


    function showHidePassword(showData, hideData, id){
        showData.forEach((show) => {
            hideData.forEach((hide) => {
                show.addEventListener('click', () => {
                    if (id.getAttribute('type') == 'password' && !show.classList.contains('hide')) {
                        show.classList.add('hide');
                        hide.classList.remove('hide');
                        id.setAttribute('type', 'text');
                    }
                    return false;
                });
                hide.addEventListener('click', () => {
                    if (id.getAttribute('type') == 'text' && !hide.classList.contains('hide')) {
                        hide.classList.add('hide');
                        show.classList.remove('hide');
                        id.setAttribute('type', 'password');
                    }
                    return true;
                });
                
            });
        });
    
    }

    showHidePassword(openEye, closeEye, enterId);
    showHidePassword(openEye, closeEye, regId);
    showHidePassword(openEye, closeEye, regRepeatId);

    //  const openEye = document.querySelectorAll('[data-show]'),
    //       closeEye = document.querySelectorAll('[data-hide]'),
    //       enterId = document.getElementById('password__enter'),
    //       regId = document.getElementById('password__reg'),
    //       regRepeatId = document.getElementById('password__reg-repeat');


    // function showHidePassword(showData, hideData, id){
    //     showData.forEach((show) => {
    //         hideData.forEach((hide) => {
    //             const hideEye = hide;
    //             const showEye = show;
    //             showEye.addEventListener('click', () => {
    //                 if (id.getAttribute('type') == 'password' && !showEye.classList.contains('hide')) {
    //                     showEye.classList.add('hide');
    //                     hideEye.classList.remove('hide');
    //                     id.setAttribute('type', 'text');
    //                 }
    //                 return false;
    //             });
    //             hideEye.addEventListener('click', () => {
    //                 if (id.getAttribute('type') == 'text' && !hideEye.classList.contains('hide')) {
    //                     hideEye.classList.add('hide');
    //                     showEye.classList.remove('hide');
    //                     id.setAttribute('type', 'password');
    //                 }
    //                 return true;
    //             });
            
    //         });
    //     });

    //     hideData.forEach((hide) => {
    //         // let hideEye = hide;
    //         showData.forEach((show) => {
   
    //                 const hideEye = hide;
    //                 const showEye = show;
    //                 showEye.addEventListener('click', () => {
    //                     if (id.getAttribute('type') == 'password' && !showEye.classList.contains('hide')) {
    //                         showEye.classList.add('hide');
    //                         hideEye.classList.remove('hide');
    //                         id.setAttribute('type', 'text');
    //                     }
    //                     return false;
    //                 });
    //                 hideEye.addEventListener('click', () => {
    //                     if (id.getAttribute('type') == 'text' && !hideEye.classList.contains('hide')) {
    //                         hideEye.classList.add('hide');
    //                         showEye.classList.remove('hide');
    //                         id.setAttribute('type', 'password');
    //                     }
    //                     return true;
    //                 });
                
   
    //         });
    //     });

    //     showEye.addEventListener('click', () => {
    //         if (id.getAttribute('type') == 'password' && !showEye.classList.contains('hide')) {
    //             showEye.classList.add('hide');
    //             hide.classList.remove('hide');
    //             id.setAttribute('type', 'text');
    //         }
    //         return false;
    //     });
    //     hideEye.addEventListener('click', () => {
    //         if (id.getAttribute('type') == 'text' && !hideEye.classList.contains('hide')) {
    //             hideEye.classList.add('hide');
    //             showEye.classList.remove('hide');
    //             id.setAttribute('type', 'password');
    //         }
    //         return true;
    //     });
    
    // }

    // showHidePassword(openEye, closeEye, enterId);
    // showHidePassword(openEye, closeEye, regId);
    // showHidePassword(openEye, closeEye, regRepeatId);




});