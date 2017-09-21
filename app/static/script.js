$(function() {
    NProgress.configure({
        trickle: false
    });
    NProgress.start();
    email_list_status(email_list)
    NProgress.done();
    //NProgress.remove();  

});




email_string = `AARTI.RAINA@gsk.com
ANUJ.GUPTA@boehringer-ingelheim.com
Aakash.Mehta@sanofi.com
Aakash.Sarkar@elililly.com
Abhijeet.Goon@gsk.com
Abhijit.Sanyal@allergan.com
Abhilash.Chakraverty@ge.com
Abhilash.Jindal@ge.com
Adesh.Kumar@ge.com
Adil.Mirza@sanofi.com
Aditi.Patwardhan@ge.com
Aditya.Banerjee@boehringer-ingelheim.com
Ajay_Nanda@bd.com
Ajit.Nair@sanofi.com
Akhil.Juneja@allergan.com
Akhil.Sehrawat@stryker.com
Akshay.Jodha@shire.com
Albertraj.Balraj@roche.com`
email_list = email_string.split('\n');
var i = 0;

function email_list_status(emails) {
    url = 'https://mailgnome.herokuapp.com/check_email/'
    $.each(emails, function(index, email) {
        $.getJSON(url + email.toLowerCase(), function(data) {
                var html = '';
                if (data['message'])
                    //console.log(data['message']);
                    if (data['code'] == 1) {
                        html = "<li style=\"color:white; background:#4bb453\">" + data['email'] + " : " + data['message'] + "</li>";
                    }
                else {
                    html = "<li style=\"color:grey;\">" + data['email'] + " : " + data['message'] + "</li>";
                }

                $('#menu').append(html);

            })
            .done(function() {
                console.log('getJSON request for ' + email + ' succesfull');
                $('html,body').animate({
                    scrollTop: document.body.scrollHeight
                }, "fast");
            })
            .fail(function(jqXHR, textStatus, errorThrown) {
                console.log('getJSON request for ' + email + ' failed with ' + jqXHR.status);
                $('#menu').append("<li style=\"color:grey;\">" + email + " : FAILURE </li>");
            })
            .always(function() {
                console.log('Done with: ' + email);
                i += 1;
                
                NProgress.set(i / email_list.length);
                if(i==email_list.length)
                console.log('Finished');
            }); // progress bar


    });
}

