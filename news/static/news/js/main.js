
// https://youtu.be/r7a3JNdkgy0?t=27m12s
//отправляем ajax запрос на сервер

$(document).ready(function () {
    $("#miner_get_button").click(function () {
    $.ajax({
        type: "GET",
        url: "/miner_add",
        data: {
            'user_height': $("#user_height").val(),
            'sys_height': $("#sys_height").val(),
        },
        dataType: "text",
        cache: false,
        success: function (data) {
            if (data == 'True') {
                $("#miner_message").text("Ресурс добыт!");
                $("#miner_message").attr("style", "color:black;");
                return true;
            }
        }
    });
});
});