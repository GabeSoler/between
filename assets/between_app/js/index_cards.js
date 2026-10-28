

$(function(){




    $("#brand-text").velocity("headShake",{duration:1000});
    $("#landing-text_1").velocity("fadeInRight",{duration:600});
    $("#landing-text_2").velocity("fadeInRight",{duration:800});
    $("#landing-button").velocity("fadeInRight",{duration:1000});
    $("#my_site_link").velocity("fadeInRight",{duration:1500});




    
// define a callback function for the intersection observer. It receives an entry and a observer object that can stop observing    
    function animate_card_callback(entries,observer) {
      // entries are the observations
      entries.forEach(entry =>{
        //if an observation hits the options
        if (entry.isIntersecting){
          //trigger an animation
          entry.target.velocity("fadeInRight");
        }
      }
      )
      }
// define a set of options, in this case it gives a margin to the object or a threshold of visibility
    const card_observer_options = {
      rootMargin :"50px",
      //threshold : "0.1"
    }

    //define a observer object that receives a function and the options
    const card_observer = new IntersectionObserver(animate_card_callback, card_observer_options)

    //here I give each card an observer independently so each can trigger the function
    $(".card").each(function (index,item){

      card_observer.observe($(item)[0]);
    }
    )
    card_observer.observe($("#alert_bottom_text")[0]);

  })