

$(function(){

    // True if in the view port
    function isInViewport(card) {
        var elementTop = $(card).offset().top;
        var elementBottom = elementTop + $(card).outerHeight();
        var viewportTop = $(window).scrollTop()-80;
        var viewportBottom = viewportTop + $(window).height()+80;
        return elementBottom > viewportTop && elementTop < viewportBottom;
        };


    //Animate if scrolling and in view port, appearing from right
    $(window).scroll(function() {
          $(".card").each(function(index,item){
            if (isInViewport(item)) {
              item.animate({
                "transform":"translateX(0)",
                "opacity":1
                },1200+index*200,"ease-out")          
              }else{
                this.animate({
                    "transform":"translateX(5%)",
                    "opacity":0
                    },800)    
              };
            });
            if (isInViewport($("#alert_bottom"))){
                $("#alert_bottom_text").fadeIn(800)
            }else{
                $("#alert_bottom_text").fadeOut(100)
                };           
        });
    $("#landing-text_1").hide().fadeIn(600);
    $("#landing-text_2").hide().fadeIn(1000);
    $("#landing-button").hide().fadeIn(1400);
    $("#my_site_link").hide().fadeIn(2000);
})