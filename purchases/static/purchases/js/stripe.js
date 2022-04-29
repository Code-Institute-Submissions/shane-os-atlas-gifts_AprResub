// Stripe Payments
var stripePublicKey = $('#public_key_id').text().slice(1,-1);
var stripeSecretKey = $('#client_secret').text().slice(1,-1);
var stripe = Stripe(stripePublicKey);

var elements = stripe.elements();
var style  = {
    base: {
        color: '#000',
        fontSize: '14px',
    },
    invalid: {
        color: '#cc0000',
        iconColor: '#cc0000'
    }
};

var stripeCard = elements.create('card', {style: style});
stripeCard.mount('#card-payment');

// Error Handling

stripeCard.addEventListener('change', function (event) {
    var errorResponse = document.getElementById('card-error');
    if (event.error) {
        var html = `
            <span>${event.error.message}</span>
        `;
        $(errorResponse).html(html);
    } else {
        errorResponse.textContent = '';
    }
});

// Stripe Form Submission

const stripeForm = document.getElementById('delivery-form');
stripeForm.addEventListener('submit', function(ev){
    ev.preventDefault();
    stripeCard.update({'disabled': true});
    $('#stripe-submit').attr('disabled', true);
    $('#delivery-form').fadeToggle(100);
    $('#payment-processing-overlay').fadeToggle(100);

    var personalInfo = Boolean($('#id_personal_info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var profileData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': stripeSecretKey,
        'personal_info': personalInfo,
    };

    var url = '/purchases/purchases_data_cache/';

    $.post(url, profileData).done(function() {
        stripe.confirmCardPayment(stripeSecretKey, {
            payment_method: {
                card: stripeCard,
                billing_details: {
                    name: $.trim(stripeForm.name.value),
                    phone: $.trim(stripeForm.phone.value),
                    email: $.trim(stripeForm.email.value),
                    address: {
                        line1: $.trim(stripeForm.address_line1.value),
                        line2: $.trim(stripeForm.address_line1.value),
                        city: $.trim(stripeForm.town.value),
                        country: $.trim(stripeForm.country.value),
                        state: $.trim(stripeForm.address_line3.value),
                    }
                }
            },
            shipping: {
                    name: $.trim(stripeForm.name.value),
                    phone: $.trim(stripeForm.phone.value),
                    address: {
                        line1: $.trim(stripeForm.address_line1.value),
                        line2: $.trim(stripeForm.address_line2.value),
                        city: $.trim(stripeForm.town.value),
                        country: $.trim(stripeForm.country.value),
                        postal_code: $.trim(stripeForm.postcode.value),
                        state: $.trim(stripeForm.address_line3.value),
                    }
            }
        }).then(function(result){
            if (result.error) {
                var errorResponse = document.getElementById('card-error');
                var html = `
                    <span>${result.error.message}</span>`;
                $(errorResponse).html(html);
                $('#delivery-form').fadeToggle(100);
                $('#payment-processing-overlay').fadeToggle(100);
                stripeCard.update({ 'disabled': false});
                $('#stripe-submit').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded'){
                    stripeForm.submit();
                }
            }
        });
    }).fail(function() {
        location.reload();
    });
});