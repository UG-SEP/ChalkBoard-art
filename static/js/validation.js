/* regex for username validation 


[a-zA-Z0-9_]{5,} to match at least five alphanumerics and the underscore
[a-zA-Z]+ to have at least one letter
[0-9]* to match zero to any occurrence of the given numbers range

*/

/* regex for password validation

Min 1 uppercase letter.
Min 1 lowercase letter.
Min 1 special character.
Min 1 number.
Min 8 characters.
Max 30 characters.

*/

/* regex for email validation


*/
var state=false

function validate(){
var email=document.getElementById("email").value
var email_re= /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/

console.log("Yes")
    if(!email.match(email_re)){
        alert("Invalid Email Address")
        return false
    }
}

function change(){
   if(state){
       document.getElementById("password").setAttribute("type","password")
       document.getElementById("show").innerHTML="SHOW"
   }
   else{
    document.getElementById("password").setAttribute("type","text")
    document.getElementById("show").innerHTML="HIDE"
   }
   state=!state
}