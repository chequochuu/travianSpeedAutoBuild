function sleep(ms) {
console.log('dsfds')
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function clickPlanet() {
    var classname = "contentContainer";
    var t = document.getElementsByName('rx');
    console.log(t)
    var pos = Math.floor(Math.random() * 18);
    var status = document.getElementById("village_map").children[pos].classList[2];
    console.log(status);
    //await sleep(2000);
    var count = 0;
    while (status != "good"){
        count++;
        if (count > 100){
            break;
            count = 0;
        }
        //await sleep(2000);
        pos = Math.floor(Math.random() * 18);
        status = document.getElementById("village_map").children[pos].classList[2];
    }
    var s = t[0].children[pos];
    if (count < 100){
        s.click();
    }
    else{
        await sleep(60000);
        window.location.href = "http://tx4.crusadertrav.eu/dorf1.php"
    }
}

console.log('click');

clickPlanet();

