  
  $(function () {
console.log("jhbkjb");

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
    });

 