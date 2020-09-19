var time = 0;
var timeStr = "0.00";

var loop;

var usingTimer = false;

function useTimer() {
	usingTimer = !usingTimer;
	if (usingTimer) {
		document.getElementById("engage").value = "Stop";
		loop = setInterval(
			function() {
				time = time + 1;
				var csStr = time.toString();
				while (csStr.length < 3) {
					csStr = "0" + csStr;
				}
				timeStr = csStr.slice(0, -2) + "." + csStr.slice(-2);
				document.getElementById("time").innerHTML = timeStr;
			},
			10
		);
	} else {
		document.getElementById("engage").value = "Start";
		clearInterval(loop);
	}
}
