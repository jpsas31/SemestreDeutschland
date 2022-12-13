function insertText() {
    var selection
    if( $('#t1').is(':checked') ){
        selection = 'text1'
    }
    if( $('#t2').is(':checked') ){

        selection = 'text2'
    }
    $.ajax({
        url: "https://hiplan.thi.de/webservice/webtechtest/index.php",
        type: 'post',
        dataType: 'json', 
        data: jQuery.param({ selection}) ,
        success: function(res) {
            console.log(res);
            $('#text_block').children()[0].textContent=res.data
        }
    });
}

  