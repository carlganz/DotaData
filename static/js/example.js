$(document).ready(function() {
  $("#sub").click(function () {
      var new_entry = $("#entryInput").val()
	  route = "/submit"
	  $.post(route, {"val":new_entry}, function(data) {
		  location.reload()
	  });
  });
});
