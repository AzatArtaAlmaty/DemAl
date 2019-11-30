$('[data-toggle="datepicker"]').datepicker(); //datepicker newindex 
//dropdown
let dropdown = $('#dropdownMenuButton');
let dropdownItem = $('.dropdown-item');
console.log(dropdown);
dropdownItem.on('click', (event) => {
	console.log(event);
	dropdown[0].textContent = event.currentTarget.innerText;
});