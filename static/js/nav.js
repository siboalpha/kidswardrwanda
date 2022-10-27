(function($) {
    $(function() {
      $('nav ul li > a:not(:only-child)').click(function(e) {
        $(this)
          .siblings('.nav-dropdown')
          .slideToggle()
        $('.nav-dropdown')
          .not($(this).siblings())
          .hide()
        e.stopPropagation()
      })
      $('html').click(function() {
        $('.nav-dropdown').hide()
      })
      // Toggle open and close nav styles on click
      $('#nav-toggle').click(function() {
        $('nav ul').slideToggle();
      });
      $('#nav-toggle').on('click', function() {
        this.classList.toggle('active')
      })
    })
  })(jQuery)
  
  jQuery(function($){
      var $navbar = $('.navigation')
      $(window).scroll(function(event){
          var $current = $(this).scrollTop();
          if($current > 50){
              $navbar.addClass('navigation-background');
          } else{
              $navbar.removeClass('navigation-background');
          }
      });
  });

  const scrollLinks = document.querySelectorAll(".scroll-link");
  const navBar = document.getElementById("nav")
  scrollLinks.forEach((link) => {
    link.addEventListener("click", (e) => {
      e.preventDefault()

      id = e.currentTarget.getAttribute("href").slice(2);
      element = document.getElementById(id)

      const navBarHeight = navBar.getBoundingClientRect().height + 50
      console.log(navBar)
      console.log(element)
      console.log(navBarHeight)

      let position = element.offsetTop - navBarHeight

      console.log(position)

      window.scrollTo (
        {
          top: position
        }
      )
    })
  })