window.onload = function () {
    var receiver = document.getElementById('receiver').contentWindow;
    jQuery('body').on('click', '.measurments_btn', function () {
        var pcode = jQuery(this).attr("data-sku"); receiver.postMessage(pcode,
            "https://widget.viubox.com/index.html");
        console.log(pcode)
    });
}