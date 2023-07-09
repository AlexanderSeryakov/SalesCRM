// window.addEventListener("DOMContentLoaded", (event) => {
    // ...
    //  write your code here, if you want to strat some code
    //  before DOMContentLoaded.
    // ...
// });
const URL = 'http://127.0.0.1:8000/'

function getCookie(name) {
    var matches = document.cookie.match(new RegExp(
      "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
};


function validateInputNum(clasSelector){
    let doc = document;
    let result = true;

    function removeError(inp){
        const parent = inp.parentNode;

        if (parent.classList.contains('input-error')){
            parent.querySelector('.error-label').remove();
            parent.classList.remove('input-error');
        }
    };

    function createError(inp, errorMsg){
        const parent = inp.parentNode;
        const errorLabel = doc.createElement('label');
        
        errorLabel.classList.add('error-label');
        errorLabel.textContent = errorMsg;

        parent.classList.add('input-error');
        parent.append(errorLabel);
    };

    const numInputs = doc.getElementsByClassName(clasSelector);

    for(numInp of numInputs){
        removeError(numInp);

        if(numInp.value == '' | numInp.value <= 0 | 1001 <= numInp.value){
            createError(numInp, 'Количество должно быть в диапазоне от 1 до 1000.');
            result = false;
        }
    };

    return result;
};

function validateShippingInput(){
    let result = true,
        doc = document;

    function removeError(inp){
        const parent = inp.parentNode;
    
        if (parent.classList.contains('input-error')){
            parent.querySelector('.error-label').remove();
            parent.classList.remove('input-error');
        }
    };
    
    function createError(inp, errorMsg){
        const parent = inp.parentNode;
        const errorLabel = doc.createElement('label');
            
        errorLabel.classList.add('error-label');
        errorLabel.textContent = errorMsg;
    
        parent.classList.add('input-error');
        parent.append(errorLabel);
    };
    
    let shipper = doc.getElementById('shipper'),
        shipperPhone = doc.getElementById('shipper-phone'),
        shipperBuisnes = doc.getElementById('shipper-buisnes'),
        shipperAddress = doc.getElementById('shipper-address'),
        shipperComments = doc.getElementById('shipper-comments');

    removeError(shipper);
    removeError(shipperPhone);
    removeError(shipperBuisnes);
    removeError(shipperAddress);
    removeError(shipperComments);

    if (shipper.value == ''){
        createError(shipper, 'Обязательное поле');
        result = false;
    }
    if (12 <= shipperPhone.value.length){
        createError(shipperPhone, 'Максимальная длина номера 11 символов');
        result = false;
    }
    if (20 <= shipperBuisnes.value.length){
        createError(shipperBuisnes, 'Допустимая длина 20 символов');
        result = false;
    }
    if (30 <= shipperAddress.value.length){
        createError(shipperBuisnes, 'Допустимая длина 30 символов');
        result = false;
    }
    if (100 <= shipperComments.value.length){
        createError(shipperBuisnes, 'Допустимая длина 100 символов');
        result = false;
    }
    return result
};

function getNumInputValues(){
    let doc = document,
        items = JSON.parse(localStorage.getItem('items')),
        products = [];

    for (let item of items){
        item.quantity = doc.getElementById(item.productName).lastElementChild.value;
        products.push(item);
    };
    // set arr in localStorage if you need
    // localStorage.setItem('products', JSON.stringify(products));
    return products
};

function getShippingInfo(arr){
    let doc = document,
        shippingInfo = [];

    for (let shippingInput of arr){
        shippingInfo.push({[shippingInput]: doc.getElementById(shippingInput).value})
    };
    return shippingInfo
};

function backToEditingSupply(){
    let doc = document;
    supplyWindow = doc.querySelector('.create__supply');
    supplyWindow.classList.remove('hidden_field');
    
    supplyCreated = doc.getElementById('supply__confirm');
    supplyCreated.classList.add('hidden_field');
}

function viewConfirmSupplyPage(){
    const shipperAttrs = ['shipper', 'shipper-phone', 
                          'shipper-buisnes', 'shipper-address', 'shipper-comments'];
    let products = getNumInputValues(),
        shippingInfo = getShippingInfo(shipperAttrs);

    let doc = document,
        edtiBtn = doc.getElementById('edit-supply'),
        confirmBtn = doc.getElementById('confirm-supply'),
        supplyWindow = doc.querySelector('.create__supply')

    supplyWindow.classList.add('hidden_field');
    
    let supplyCreated = doc.getElementById('supply__confirm');
    supplyCreated.classList.remove('hidden_field');

    let tBody = doc.getElementById('t-body');

    while (tBody.firstChild){
        tBody.removeChild(tBody.firstChild)
    };
    for (let product of products){
        let productTr = doc.createElement('tr'),
            productTdName = doc.createElement('td'),
            productTdQuantity = doc.createElement('td');

        productTr.appendChild(productTdName);
        productTr.appendChild(productTdQuantity);
        productTdName.append(product.productName);
        productTdQuantity.append(product.quantity);
    
        tBody.appendChild(productTr);
    };

    for (let i = 0; i < shippingInfo.length; i++){
        let parent = doc.getElementById('confirm-' + shipperAttrs[i]),
            shippingP = doc.createElement('p');
        
        let key = shipperAttrs[i]
        let sh = shippingInfo[i]

        if (parent.children.length == 1){
            // console.log(parent.lastElementChild)
            shippingP.append(sh[key]);
            shippingP.classList.add('shipper');

            parent.appendChild(shippingP);
            
        } else if(parent.children.length == 2){
            parent.lastElementChild.innerHTML = sh[key];
        }
        
        
    };
    edtiBtn.addEventListener('click', backToEditingSupply);
    confirmBtn.addEventListener('click', createNewSupply, {once: true})
    // confirmBtn.addEventListener('click', createNewSupply) for develop-mode
};

function alertToggle(){
    localStorage.setItem('newSupply', 1);
}

async function createNewSupply(){
    let products = getNumInputValues(),
        shippingInfo = getShippingInfo(['shipper', 'shipper-phone', 
                                    'shipper-buisnes', 'shipper-address', 'shipper-comments']);
    
    const response = await fetch(`${URL}supply/api/v1/supply/`, {
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        method: 'POST',
        body: JSON.stringify({
            'products': products,
            'shipping': shippingInfo
        })
    });

    const serverResponse = await response.json();

    if (serverResponse.status == 200){
        console.log('sucessful');
        const test = `${URL}supply/`
        document.location.href = test;
        alertToggle();
    } else {
        console.log('error', response.status)
    }
};

doc.getElementById('shipper-phone').addEventListener('input', 
        function(e){
          this.value = this.value.replace(/[^\d]/g, '');
        }
    );

const supplyBtn = document.getElementById('supply-btn');

supplyBtn.addEventListener('click', function() {
            if (validateInputNum('num-input') & validateShippingInput()){
                viewConfirmSupplyPage();
            }else {
                console.log('validation error!')
            }
});
