var message = "Hi"; //spam message
var interval = 1000; //interval between each message (in milliseconds) (Here 1 second is given)
var count = 1000; //number of times you wanted to send the message
var i = 0;
var timer = setInterval(function() { // lines used        
    document.getElementsByClassName('composer_rich_textarea')[0].innerHTML = message; // to print
    $('.im_submit').trigger('mousedown'); // the message
    i++;
    if (i == count) // this condition makes the program stop when the required number of messages are sent
        clearInterval(timer);
}, interval);