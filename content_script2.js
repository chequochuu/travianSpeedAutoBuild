function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function clickPlanet() {
    var t2 = document.getElementsByClassName('button-content');
    var i = 0;
    var shouldUp = false;
    for (i = 0; i < t2.length; i++){
        console.log(i);
        var bgImage = getComputedStyle(t2[i].parentNode.children[0].children[0]).backgroundImage;
        if (bgImage.endsWith('goldNormal.png")')){
            console.log(bgImage);
            continue;
        }
        if (t2[i].innerText.startsWith('Up') && !t2[i].innerText.endsWith("level") ){
            shouldUp = true;
            console.log("up");
            break;
        }
    }
    if (shouldUp){
        console.log('click');
        t2[i].click();
    }
    else{
        console.log('back');
        var s = document.URL
        var matches = s.match(/\d+$/);
        console.log(matches[0]);
        var num = parseInt(matches[0]);
        console.log(num);
//        await sleep(5000);
//        if (num < 19){
//            console.log('here');
//            window.location.replace("http://tx4.crusadertrav.eu/dorf1.php");
//        }
//        else {
//            window.location.replace("http://tx4.crusadertrav.eu/dorf2.php");
//        }
    }
}
console.log("script2");
    clickPlanet();

