$(function(){
	//getConteudoSobreAjax();
	selecionaMenuSuperior();
});

function getConteudoSobreAjax(){
	$('#getConteudoSobreAjax').click(function(){
		$.get($(this).attr('href').substr(1),function(data){
			$("body").append(data);
			$('#sobre').modal('show');
			$('#removeConteudoSobre').click(function(){
					$('#sobre').modal('hide').remove();
					return false;
			});
		});
		return false;
	});
}

function selecionaMenuSuperior(){
	var menuId = $('#menuId').val();
	$('#menu-superior li').removeClass().eq(menuId).addClass('active');
}
