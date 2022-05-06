let btnAddCounterAdult = document.querySelector('#addCounterAdult');
let btnSubtractCounterAdult = document.querySelector('#subtractCounterAdult');
let btnAddCounterSenior = document.querySelector('#addCounterSenior');
let btnSubtractCounterSenior = document.querySelector('#subtractCounterSenior');
let btnAddCounterChild = document.querySelector('#addCounterChild');
let btnSubtractCounterChild = document.querySelector('#subtractCounterChild');
let label = document.querySelectorAll('input');

btnAddCounterAdult.addEventListener('click', () => {
    if (parseInt(label[0].value) < 9) {
        label[3].value = 13.59 + parseFloat(label[3].value);
        label[4].value = parseFloat(label[3].value) / 10;
        label[5].value = parseFloat(label[4].value) + parseInt(label[3].value); 
        label[0].value = parseFloat(label[0].value) + 1;
    }
});

btnSubtractCounterAdult.addEventListener('click', () => {
    if (parseInt(label[0].value) > 0) {
        label[3].value = parseFloat(label[3].value) - 13.59;
        label[4].value = parseFloat(label[3].value) / 10;
        label[5].value = parseFloat(label[4].value) + parseInt(label[3].value); 
        label[0].value = parseFloat(label[0].value) - 1;
    }
});

btnAddCounterSenior.addEventListener('click', () => {
    if (parseInt(label[1].value) < 9) {
        label[3].value = 10.59 + parseFloat(label[3].value);
        label[4].value = parseFloat(label[3].value) / 10;
        label[5].value = parseFloat(label[4].value) + parseInt(label[3].value); 
        label[1].value = parseFloat(label[1].value) + 1;
    }
});

btnSubtractCounterSenior.addEventListener('click', () => {
    if (parseInt(label[1].value) > 0) {
        label[3].value = parseFloat(label[3].value) - 10.59;
        label[4].value = parseFloat(label[3].value) / 10;
        label[5].value = parseFloat(label[4].value) + parseInt(label[3].value); 
        label[1].value = parseFloat(label[1].value) - 1;
    }
});

btnAddCounterChild.addEventListener('click', () => {
    if (parseInt(label[2].value) < 9) {
        label[3].value = 9.59 + parseFloat(label[3].value);
        label[4].value = parseFloat(label[3].value) / 10;
        label[5].value = parseFloat(label[4].value) + parseInt(label[3].value); 
        label[2].value = parseFloat(label[2].value) + 1;
    }
});

btnSubtractCounterChild.addEventListener('click', () => {
    if (parseInt(label[2].value) > 0) {
        label[3].value = parseFloat(label[3].value) - 10.59;
        label[4].value = parseFloat(label[3].value) / 10;
        label[5].value = parseFloat(label[4].value) + parseInt(label[3].value); 
        label[2].value = parseFloat(label[2].value) - 1;
    }
});