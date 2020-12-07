function showDate(){
    var d = new Date();
    var months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    document.getElementById("imgDate").innerHTML=months[d.getMonth()] + ", " + d.getFullYear();
    console.log(d);
    
}

function MessBox(){
    alert("Thank you! I'll be in touch soon");
    location.href='../HTML/Home Page.html';

}

