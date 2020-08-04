const copyurl = () => {
    console.log('clicked')
    let copyText = document.getElementById('url')
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    document.execCommand("copy");

    var tooltip = document.getElementById("toolTipBtn");
    tooltip.setAttribute('title', 'copied: '+ copyText.value)
}
const outFunc = () => {
    var tooltip = document.getElementById("toolTipBtn");
    tooltip.setAttribute('title', 'copy to clipboard ')
}