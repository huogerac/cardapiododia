$(function(){
	//getConteudoSobreAjax();
	selecionaMenuSuperior();
	setFieldHourDatepicker();
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

function setFieldHourDatepicker(){
	$('input').each(function(i,obj){
		if ($(obj).attr('data-datepicker') != undefined){
			
			var idObj = $(obj).attr('id');
			
			var regexp = /^(\d{4})-(\d{2})-(\d{2}) (.+)$/;
			
			if (data = $(obj).val().match(regexp)){
				$('#' +idObj + '_hour').val(data[4]);
				$(obj).val(data[3] + "/" + data[2] + "/" + data[1]);
			}	
		}	
	});
}
