$(function() {

	//Search function
	$("#searchProducts").on("keypress" , function(){
		console.log("search working");

		var searchConditions = $('#searchProducts').val().toLowerCase();
		$(".item_container").each(function() {
			if ($(this).text().toLowerCase().indexOf(searchConditions) == -1) {
				$(this).hide();
		} else{
			$(this).show();
		}
		}); //Each item container
	});//search function




	$('.add_button').on('click', function(){
		console.log("clicked");
		var pid = $(this).attr('data-pid');
		var qty = $(this).siblings(".qty").val();

		console.log(qty);

		$.loadmodal({
			url: "/homepage/shoppingCart.add/" + pid + "/" + qty,    //url: "/homepage/shopping_cart.add" + pid + "/" + qty,
			title: 'Shopping Cart',
			width: '600px',
		}); //loadmodal
		
	});//click





}); //ready