$(document).ready(function(){
	function fetch(view){
		$.getJSON(view.endpoint, function(data){
			console.log(data);
		    var source = $('#'+view.id).html();
		    var template = Handlebars.compile(source);
		    var html = template({data:data});
		    $('#'+view.id).after(html);
		});
	}
	$.each(site_json.views, function(index, view){ fetch(view); });
});

