
// https://youtu.be/r7a3JNdkgy0?t=27m12s
//отправляем ajax запрос на сервер

$("#miner_get_button").click(function () {
    console.log("test button")
    $.ajax({
        type: "GET",
        url: "/mainer_add/",
        data: {
            'user_height': $("#user_height").val(),
            'sys_height': $("#sys_height").val(),
        },
        dataType: "text",
        cache: false,
        success: function (data) {
            console.log(data);
            if (data == 'True') {
                $("#wiki_email_message").text("Ресурс добыт!");
                $("#wiki_email_message").attr("style", "color:black;");
                return true;
            }
        }
    });
}