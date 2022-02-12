// Stripe Payments
var stripe_public_key = $('#public_key_id').text().slice(1,-1);
var stripe_secret_key = $('#secret_key_id').text().slice(1,-1);
var stripe = Stripe(stripe_public_key);
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

var stripe_card = elements.create('card', {style: style});
stripe_card.mount('#card-payment');

// Error Handling

stripe_card.addEventListener('change', function (event) {
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

const stripe_form = document.getElementById('delivery-form');

stripe_form.addEventListener('submit', function(e){
    e.preventDefault();
    card.update({ 'disabled': true});
    $('#stripe-submit').attr('disabled', true);
    stripe.confirmCardPayment(stripe_secret_key, {
        payment_method: {
            card: stripe_card,
        }
    }).then(function(result){
        var errorResponse = document.getElementById('card-error');
        if (result.error) {
            var html = `
            <span>${event.error.message}</span>
        `;
        $(errorResponse).html(html);
        card.update({ 'disabled': false});
        $('#stripe-submit').attr('disabled', false);
        } else {
            if (result.payment_intent === 'succeeded'){
                stripe_form.submit();
            }
        }
    });
});