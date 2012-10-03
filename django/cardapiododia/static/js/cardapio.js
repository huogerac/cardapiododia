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
			
			$(obj).bind('keyup',function(){
				$(this).val($(this).val().replace(/[^\d\/]/g,"").substr(0,10));
			});
			
			var idObj = $(obj).attr('id');
			
			$('#' +idObj + '_hour').bind('keyup',function(){
				$(this).val($(this).val().replace(/[^\d\:]/g,"").substr(0,8));
			});
			
			var regexp1 = /^(\d{4})-(\d{2})-(\d{2}) (.+)$/;
			var regexp2 = /^(\d{2})\/(\d{2})\/(\d{4}) (.+)$/;
			
			if (data = $(obj).val().match(regexp1)){
				$('#' +idObj + '_hour').val(data[4].replace(/[^\d\:]/g,""));
				$(obj).val(data[3] + "/" + data[2] + "/" + data[1].replace(/[^\d\/]/g,""));
			} else if (data = $(obj).val().match(regexp2)){
				$('#' +idObj + '_hour').val(data[4].replace(/[^\d\:]/g,""));
				$(obj).val(data[1] + "/" + data[2] + "/" + data[3].replace(/[^\d\/]/g,""));
			}	
		}	
	});
}
