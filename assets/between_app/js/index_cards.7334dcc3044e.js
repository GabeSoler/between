

$(function(){

    // True if in the view port
    function isInViewport(card) {
        var elementTop = $(card).offset().top;
        var elementBottom = elementTop + $(card).outerHeight();
        var viewportTop = $(window).scrollTop();
        var viewportBottom = viewportTop + $(window).height();
        return elementBottom > viewportTop && elementTop < viewportBottom;
        };


    //Animate if scrolling and in view port, appearing from right
    $(window).scroll(function() {
          $(".card").not(":first").each(function(index,item){
            if (isInViewport(item)) {
              item.animate({
                "transform":"translateX(0)",
                "opacity":1
                },1200+index*100,"ease-out")          
              } else {
                this.animate({
                    "transform":"translateX(5%)",
                    "opacity":0
                    },800)    
              };
            });
            if (isInViewport($("#welcomeText"))){
                    $("#animateMe1").fadeIn(400);
                    $("#animateMe2").fadeIn(800);
                    $("#animateMe3").fadeIn(1000);
            }else{
                $("#animateMe1").fadeOut();
                $("#animateMe2").fadeOut();
                $("#animateMe3").fadeOut();
            };           
        });
    $("#landing-text").hide().fadeIn(900);
    $("#landing-button").hide().fadeIn(1800);
})