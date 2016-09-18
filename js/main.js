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
	
});