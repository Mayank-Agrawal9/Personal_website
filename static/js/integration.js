    $("#contact-form-submit").submit(function( event ) {
        event.preventDefault();
        formData = new FormData(this);
        $.ajax({
            type: "POST",
            url: "/api/v1/contact-form/",
            data: formData,
            processData: false,
            contentType: false,
            dataType: "json",
            success: function(data){
                window.location.href = '/thank-you';
            },
            error: function(errMsg) {
                alert('Something Went Wrong');
            }

        });
    });