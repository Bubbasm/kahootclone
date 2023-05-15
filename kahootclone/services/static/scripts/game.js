function updateTimer(remainingTime) {
    $('#timer').html(remainingTime);
    if (remainingTime > 0) setTimeout(updateTimer, 1000, remainingTime-1);
}

$(document).ready(function () {
    // https://stackoverflow.com/a/68650203
    remainingTime = JSON.parse(document.getElementById('remaining_time').textContent)
    
    if (remainingTime == null || remainingTime == "" || isNaN(remainingTime) || remainingTime < 0){
      return;
    }
    $('#timer').html(Math.floor(remainingTime));
    
    // refresh page in remainingTime seconds
    setTimeout(function () {
      // same as window.location.reload(); but ensures GET request, to avoid submitting POST data
      
      form = document.getElementById("start_game");
      if (form != null)
        form.submit();
      else
        window.location = window.location.href.split('?')[0];

    }, remainingTime * 1000);

    // update text every second
    t = remainingTime - Math.floor(remainingTime) //more accurate timer for first update
    setTimeout(updateTimer, t*1000, Math.max(0, Math.floor(remainingTime)-1));
});