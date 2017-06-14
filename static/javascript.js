$(() => {

    $('#fb-login').click(() => {
        FB.getLoginStatus(function(response) {
            console.log(response.status);
            if (response.status === 'connected') {
                console.log('yo');
                FB.login();
            }
            //statusChangeCallback(response);
        });
    });
});