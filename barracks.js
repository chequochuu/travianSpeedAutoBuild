function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function trainImperian() {
        await sleep(191000);
        var t = document.getElementsByClassName("details")[2];
        t.children[5].click();
        var t2 = document.getElementsByClassName("button-content")[0];
        t2.click();
//    await sleep(2000);
}


trainImperian();

