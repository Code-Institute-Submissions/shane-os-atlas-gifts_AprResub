// Stripe Payments
var stripePublicKey = $('#public_key_id').text().slice(1,-1);
var stripeSecretKey = $('#secret_key_id').text().slice(1,-1);
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
console.log(stripeForm)
stripeForm.addEventListener('submit', function(e){
    e.preventDefault();
    console.log('sumbit event')
    stripeCard.update({'disabled': true});
    $('#stripe-submit').attr('disabled', true);
    stripe.confirmCardPayment(stripeSecretKey, {
        payment_method: {
            card: stripeCard,
        }
    }).then(function(result){
        if (result.error) {
            var errorResponse = document.getElementById('card-error');
            var html = `
                <span>${result.error.message}</span>`;
            $(errorResponse).html(html);
            card.update({ 'disabled': false});
            $('#stripe-submit').attr('disabled', false);
        } else {
            console.log(result.paymentIntent)
            if (result.paymentIntent.status === 'succeeded'){
                stripeForm.submit();
            }
        }
    });
});