function showDate(){
    var d = new Date();
    var months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    document.getElementById("imgDate").innerHTML=months[d.getMonth()] + ", " + d.getFullYear();
    console.log(d);
    
}

function MessBox(){
     alert("Thanks you! I will get back to you soon!");

}

fetch('https://reqres.in/api/users?page=2').then(response => response.json())
.then(responseJSON => createUserList(responseJSON.data)).catch(err => 
console.log(err));

function createUserList(users) {
    console.log(users);
    const curr_main = document.querySelector("main");
    for(let user of users){
        const section = document.createElement("section");
        section.innerHTML = `
        <img src="${user.avatar}" alt="profile">
        <div>
           <span>  ${user.first_name} ${user.last_name} </span>
           <br>
           <a href="mail: ${user.email}">Send Email</a>
        </div>
        `;
        curr_main.appendChild(section);
    }
}