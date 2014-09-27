$(document).ready(function(){
	function fetch(view){
		console.log("fetching", view);
		if ( view['data_source'] !== undefined ) {
			$.getJSON(view.data_source, function(data){
				console.log(view.title, data);
			    var source = $('#'+view.id+'-template').html();
			    var template = Handlebars.compile(source);
			    var html = template({data:data});
			    $('#'+view.id+'-template').replaceWith(html);
			});
		} else {
			var source = $('#'+view.id+'-template').html();
		    $('#'+view.id+'-template').replaceWith(source);
		}
		
	}
	$.each(site_json.views, function(index, view){ fetch(view); });
});

