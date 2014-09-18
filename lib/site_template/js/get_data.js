$(document).ready(function(){
	function fetch(view){
		$.getJSON(view.data_source, function(data){
			console.log(view.title, data);
		    var source = $('#'+view.id).html();
		    var template = Handlebars.compile(source);
		    var html = template({data:data});
		    $('#'+view.id).after(html);
		});
	}
	$.each(site_json.views, function(index, view){ fetch(view); });
});

