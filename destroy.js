
async function clickPlanet() {
    var id = "21";
    var t = document.getElementsByClassName("dropdown")[0].options;
    var i;
    var shoulddel = false;
    for (i= 0; i < t.length; i++){
        if (t[i].value == id) {
            t[i].selected =true;
            shoulddel = true;
        }
    }
    var des = document.getElementsByClassName("button-content");
    if (shoulddel){
        des[0].click();
    }
}
clickPlanet();
