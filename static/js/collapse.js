$(document).ready(function() {
  var r_ind = $(".team-0-ind").html()
  var d_ind = $(".team-1-ind").html()

  var r_group = $(".radiant-team-stats").html()
  var d_group = $(".dire-team-stats").html()

  var is_ind = true;

  $("#individual").click(function () {
    if(!is_ind) {
      is_ind = true;
      $(".collapse-0").collapse("hide");
      $(".collapse-1").collapse("hide");
    }
  });

  $("#grouped").click(function () {
    if(is_ind) {
      is_ind = false;
      $(".collapse-0").collapse("hide");
      $(".collapse-1").collapse("hide");
    }
  });

  $(".collapse-0").on('hidden.bs.collapse', function () {
    if(is_ind) {
      $(".0-detail").html(r_ind);
    } else {
      $(".0-detail").html(r_group);
    }

    window.setTimeout(showTeam, 500, 0);
  });

  $(".collapse-1").on('hidden.bs.collapse', function () {
    if(is_ind) {
      $(".1-detail").html(d_ind);
    } else {
      $(".1-detail").html(d_group);
    }
    
    window.setTimeout(showTeam, 500, 1);
  });

});

function showTeam(i) {
  if (i == 0) {
    $(".collapse-0").collapse("show");
  } else {
    $(".collapse-1").collapse("show");
  }
}
