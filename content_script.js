function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function clickPlanet() {
    var classname = "contentContainer";
    var t = document.getElementsByName('rx');
    var pos = Math.floor(Math.random() * 18);
    var status = document.getElementById("village_map").children[pos].classList[2];
    console.log(status);
    //await sleep(2000);
    var count = 0;
    while (status != "good"){
        count++;
        if (count > 100){
            console.log("sleep");
            await sleep(1000);
            count = 0;
        }
        //await sleep(2000);
        console.log(status);
        pos = Math.floor(Math.random() * 18);
        console.log(pos);
        status = document.getElementById("village_map").children[pos].classList[2];
        console.log(status);

    }
    var s = t[0].children[pos];
    if (count < 100){
        s.click();
    }
}

    console.log('click');

clickPlanet();

