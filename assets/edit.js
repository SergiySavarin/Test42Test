function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#blah').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}

$("#photo").change(function(){
    readURL(this);
});

$(document).ready(function() {
    $('#data_saved').hide();
    $('#birthday').datetimepicker({
        'format': 'DD/MM/YYYY',
    });
});

