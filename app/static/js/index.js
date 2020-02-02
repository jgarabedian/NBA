function showMenu() {
    document.getElementById('nav-menu')
}

$('#nav-icon').click(function() {
    $('#nav-menu').toggle('slide');
    setTimeout(function() {
        if($('#nav-menu').is(':visible')) {
            $('#nav-icon').attr('class', 'fas fa-times')
        } else {
            $('#nav-icon').attr('class', 'fas fa-ellipsis-v')
        }
    }, 500);
})