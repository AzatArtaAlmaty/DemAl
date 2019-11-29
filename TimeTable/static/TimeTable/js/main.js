//scrollspy in newindex #aboutUs
$('[href=\"#\"]').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top
        }, 500, function() {
          target.focus();
        });
        return false;
      }
     }
   });

$('[data-toggle="datepicker"]').datepicker(); //datepicker newindex
//dropdown
let dropdown = $('#dropdownMenuButton');
let dropdownItem = $('.dropdown-item');
console.log(dropdown);
dropdownItem.on('click', (event) => {
	console.log(event);
	dropdown[0].textContent = event.currentTarget.innerText;
});