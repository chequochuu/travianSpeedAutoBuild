function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function clickPlanet() {
//    await sleep(2000);
    var t2 = document.getElementsByClassName('button-content');
    var i = 0;
    for (i = 0; i < t2.length; i++){
        console.log(i);
        if (t2[i].innerText.startsWith('Up') && !t2[i].innerText.endsWith("level")){
            break;
        }
    }
    t2[i].click();
}
console.log('zzzzzzzzz');
    console.log('click');
    clickPlanet();

