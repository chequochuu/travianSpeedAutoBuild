
async function clickPlanet() {
    var id = "21";
    var t = document.getElementsByClassName("dropdown")[0].options;
    var i;
    for (i= 0; i < t.length; i++){
        if (t[i].value == id) {
            t[i].selected =true;
        }
    }
    var des = document.getElementsByClassName("button-content");
    des[0].click();
    
}
clickPlanet();
