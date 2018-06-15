function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function clickPlanet() {
    while (true){
        var t = document.getElementById("village_map");
        var pos = -1;
        var i;
        var count = 0;
        for (i = 1; i<= 20; i++){
            if (!t.children[i].alt.startsWith("Construction Site")){
                var status = document.getElementById("levels").children[count].classList[1];
                if (status == "good"){
                    pos = i-1;
                    break;
                }
                count ++;
            }
        }
        if (pos == -1){
            console.log("sleep");
            await sleep(1000);
        }
        else {
            break;
        }
    }
    //await sleep(2000);
    if (pos != -1){
        t.children[0].children[pos].click()
    }
//    await sleep(2000);
}

    console.log('here');
    console.log('click');

clickPlanet();

