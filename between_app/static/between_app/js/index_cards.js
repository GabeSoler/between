

$(function(){

    // True if in the view port
    function isInViewport(card) {
        var elementTop = $(card).offset().top;
        var elementBottom = elementTop + $(card).outerHeight();
        var viewportTop = $(window).scrollTop();
        var viewportBottom = viewportTop + $(window).height();
        return elementBottom > viewportTop + 80 && elementTop < viewportBottom - 80;
        };
    function isInFullView(card) {
        var elementTop = $(card).offset().top;
        var elementBottom = elementTop + $(card).outerHeight();
        var viewportTop = $(window).scrollTop();
        var viewportBottom = viewportTop + $(window).height();
        return elementBottom > viewportTop + 100 && elementTop < viewportBottom - 100;
        };
    function isInBottomNav(element) {
        let elementTop = $(element).offset().top;
        let elementBottom = elementTop + $(element).outerHeight();
        let viewportTop = $(window).scrollTop();
        let navbarTop = viewportTop + $(window).height() - 50;
        let navbarBottom = viewportTop + $(window).height();
        return navbarBottom > elementTop < navbarTop;
        };

    function animate(item) {
      item.velocity({
        transform: ["translateX(0)","translateX(5%)"],
        opacity:[1,0]
        },
        {
          duration: 1200,
          ease: "ease-out",
          loop: false
        });

    }

    //Animate if scrolling and in view port, appearing from right
    $(window).scroll(function() {
          $(".card").each(function(index,item){
            if (isInFullView(item)) {
              item.velocity("finish");
            } else if (isInBottomNav(item)) {
              item.velocity("fadeInRight");
            };
            return;
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