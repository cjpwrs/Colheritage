$(function() {
	$('.deleteCartItem').on('click', function(){
		console.log("clicked");
		
		var pid = $(this).attr('data-pid');
		//var qty = $(this).siblings(".qty").val();

		console.log(pid);

		console.log('javascript remove cart button worked');

		
		$.loadmodal({
			url: "/homepage/shoppingCart.delete/" + pid,    //url: "/homepage/shopping_cart.add" + pid + "/" + qty,
			title: 'Shopping Cart',
			width: '600px',
		}); //loadmodal 
		
	});//click





}); //ready