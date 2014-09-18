$(document).ready(function(){
	function fetch(view){
		console.log("fetching", view);
		$.getJSON(view.data_source, function(data){
			console.log(view.title, data);
		    var source = $('#'+view.id+'-template').html();
		    var template = Handlebars.compile(source);
		    var html = template({data:data});
		    $('#'+view.id+'-template').after(html);
		});
	}
	$.each(site_json.views, function(index, view){ fetch(view); });
});

