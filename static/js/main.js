$(function () {
    console.log("Loaded");
    $.material.init();
	
	var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',];
	function checkTime(i) {
        return (i < 10) ? "0" + i : i;
    }

    function startTime() {
		var date = new Date();
        var hours = date.getHours();
		var minutes = date.getMinutes();
		var ampm = hours >= 12 ? 'PM' : 'AM';
		
		hours = hours % 12;
		hours = hours ? hours : 12; // the hour '0' should be '12'
		minutes = minutes < 10 ? '0'+minutes : minutes;
		
		document.getElementById('time').innerHTML = hours + ':' + minutes + '' + ampm;
        
		t = setTimeout(function () {
            startTime()}, 500);
    }
    startTime();

	(function worker() {
		$.ajax({
			url: '/smartbytes', 
			success: function(data) {
				$('#smartbytes_rem_pct').html(data.remaining_pct);
				$('#smartbytes_used').html(105-data.remaining_data);
				$('#smartbytes_daysleft').html(data.remaining_days);
			},
			complete: function() {
				// Schedule the next request when the current one's complete
				//Refresh every 1hr
				setTimeout(worker, 3600000);
			}
		});
	})();

	(function worker() {
		$.ajax({
			url: '/weather',
			success: function(data) {
				$('#curr_temp').html(data.temperature + "&deg;C");
			},
			complete: function() {
				// Schedule the next request when the current one's complete
				//Refresh every 2hr
				setTimeout(worker, 7200000);
			}
		});
	})();

	(function worker() {
		$.ajax({
			url: '/gcalappts',
			success: function(data) {
				var li = '';
				for (var i=0; i < data.length; i++) {
					li += '<li class="list-group-item">'+data[i].date+": "+ data[i].summary +'</li>';
				}
				$('<li />', {html: li}).appendTo('#calendar_events')
								
				console.log(data);
				//$('#curr_temp').html(data.temperature + "&deg;C");
			},
			complete: function() {
				// Schedule the next request when the current one's complete
				//Refresh every 2hr
				setTimeout(worker, 7200000);
			}
		});
	})();


});