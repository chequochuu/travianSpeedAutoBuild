
async function clickPlanet() {
    var id = ["25", "29", "33"];
    var t = document.getElementsByClassName("dropdown")[0].options;
    var i;
    var shoulddel = false;
    for (i= 0; i < t.length; i++){
        if (ids.indexOf(t[i].value) != -1) {
            t[i].selected =true;
            shoulddel = true;
            break;
        }
    }
    var des = document.getElementsByClassName("button-content");
    if (shoulddel){
        des[0].click();
    }
}
clickPlanet();
