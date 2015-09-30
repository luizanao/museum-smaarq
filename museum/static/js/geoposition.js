if (jQuery != undefined) {
    var django = {
        'jQuery': jQuery,
    }
}

(function($) {
    $(document).ready(function() {
        $('.geoposition-widget').children().closest('table').css('margin','15px');
        $('.geoposition-widget').children().closest('table').children().closest('tbody').children().closest('tr').css('float','left');
    });
})(django.jQuery);
