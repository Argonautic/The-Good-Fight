/*$(() => {

    $('#fb-login').click(() => {
        FB.getLoginStatus(function(response) {
            console.log(response.status);
            if (response.status === 'connected') {
                FB.logout();
            }
            else if (response.status ==='not_authorized') {
                console.log('jo');
                FB.login();
            }
            //statusChangeCallback(response);
        });
    });
});*/