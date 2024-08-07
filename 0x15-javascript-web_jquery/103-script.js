$(document).ready(function(){
    function translate() {
        var languageCode = $('#language_code').val();
        var url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;

        $.get(url, function(data) {
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(translate);

    $('#language_code').keypress(function(event) {
        if (event.which == 13) { // 13 is the Enter key
            translate();
        }
    });
});
