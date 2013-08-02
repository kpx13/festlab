  
  $(function () {

          var pattern = /^[a-z0-9_-]+@[a-z0-9-]+\.[a-z]{2,6}$/i;

            $(".slider__nav__l:first").addClass("_active");

            var imageWidth = $(".slider__wrap").width();
            var imageSum = $(".slider__i").size();
            var imageReelWidth = imageWidth * imageSum;
            var index =  $('.slider__nav__l._active').index();

            $(".slider").css({'width': imageReelWidth});

            rotate = function () {
                var triggerID = $active.index() ;
                var image_reelPosition = triggerID * imageWidth;

                $(".slider").animate({
                    left: -image_reelPosition
                }, 500);

                $(".slider__nav__l").removeClass('_active');
                $active.addClass('_active');
            };

            rotateSwitch = function () {
                play = setInterval(function () {
                    $active = $('.slider__nav__l._active').next();
                    if ($active.length === 0) {
                        $active = $('.slider__nav__l:first');
                    }
                    rotate();
                }, 6000);
            };

            rotateSwitch();

            $(".slider__nav__l").click(function () {
                $active = $(this);
                clearInterval(play);
                rotate();
                rotateSwitch();
                return false;
            });

      $('.rf').each(function(){

          // Объявляем переменные (форма и кнопка отправки)
          var form = $(this),
              btn = form.find('.feedback__btn');
          var email = $(".feedback__form__email").val();

          // Добавляем каждому проверяемому полю, указание что поле пустое
          form.find('.rfield').addClass('empty_field');
          form.find('.rfield2').addClass('empty_field');

          // Функция проверки полей формы
          function checkInput(){

              form.find('.rfield').each(function(){
                  if($(this).val() != ''){

                      // Если поле не пустое удаляем класс-указание
                      $(this).removeClass('empty_field');

                  } else {
                      // Если поле пустое добавляем класс-указание
                      $(this).addClass('empty_field');
                  }

              })
          }

              function checkInput2(){
              form.find('.rfield2').each(function(){
                  if($('.feedback__form__phone').val() != ''){
                      if($('.feedback__form__email').val() == ''){
                            $('.rfield2').removeClass('empty_field');

                      }
                     else{
                          var email = $(".feedback__form__email").val();

                          if(email.search(pattern) == 0)
                          {
                              $(".rfield2").removeClass('empty_field');
                          } else {
                              $('.feedback__form__phone').removeClass('empty_field');
                              $('.feedback__form__email').addClass('empty_field');
                          }
                      }
                  }
                  else if($('.feedback__form__email').val() != ''){
                      var email = $(".feedback__form__email").val();
                      if(email.search(pattern) == 0)
                      {
                          $(".rfield2").removeClass('empty_field');
                      } else {
                          $('.feedback__form__email').addClass('empty_field');
                      }
                  }
                  else{
                      $('.rfield2').addClass('empty_field');
                  }




              });
          }


          // Функция подсветки незаполненных полей
          function lightEmpty(){

              form.find('.feedback__form__info').css({'background-color':'#e9fcec'});
              form.find('.empty_field').css({'background-color':'#fed9d9'});



              // Через полсекунды удаляем подсветку
            //  setTimeout(function(){
                 // form.find('.feedback__form__info').css({'background-color':'#e9fcec'});
             // },500);
          }


          // Проверка в режиме реального времени
          setInterval(function(){

              // Запускаем функцию проверки полей на заполненность
              checkInput();
              checkInput2();

              // Считаем к-во незаполненных полей
              var sizeEmpty = form.find('.empty_field').size();
              // Вешаем условие-тригер на кнопку отправки формы
              if(sizeEmpty > 0){
                  if(btn.hasClass('disabled')){
                      return false
                  } else {
                      btn.addClass('disabled')
                  }
              } else {
                  btn.removeClass('disabled')
              }
              lightEmpty();
          },500);





      function isValidEmailAddress(emailAddress) {

          var pattern = /^[a-z0-9_-]+@[a-z0-9-]+\.[a-z]{2,6}$/i;

          return pattern.test(emailAddress);
      }
          // Событие клика по кнопке отправить
          btn.click(function(){

              if($(this).hasClass('disabled')){
                  // подсвечиваем незаполненные поля и форму не отправляем, если есть незаполненные поля
                  lightEmpty();
                  return false
              } else {
                  // Все хорошо, все заполнено, отправляем форму

                  form.submit();
              }
          });
      });

    });

 