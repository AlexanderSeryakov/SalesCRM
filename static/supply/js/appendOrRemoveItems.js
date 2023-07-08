function appendOrRemoveItems(){
    let res = JSON.parse(localStorage.getItem('items'));

    let insertF = doc.getElementById('insertField'),
        wrappers = doc.getElementsByClassName('wrapper');

    // Check elements on page and elements on localStorage. If element in localStorage and
    // not on page - append element on page.
    for(let item of res){
        let wrapper = doc.createElement('div'),
            inputLabel = doc.createElement('label'),
            inp = doc.createElement('input');
            
        
        if(doc.getElementById(item.productName) === null){
            wrapper.classList.add('wrapper');
            wrapper.classList.add('col-6')
            // wrapper.classList.add('col-sm-3')
            wrapper.id = item.productName;

            inputLabel.append(item.productName);
            inputLabel.classList.add('form-label');
            inputLabel.for = item.productId;

            inp.classList.add('form-control');
            inp.classList.add('num-input');
            inp.value = 1;
            inp.id = item.productId;
            inp.placeholder = 'Количество товара'

            wrapper.appendChild(inputLabel);
            wrapper.appendChild(inp);

            insertF.parentNode.appendChild(wrapper);
        }
    };
    document.querySelector('.num-input').addEventListener('input', 
        function(e){
          this.value = this.value.replace(/[^\d]/g, '');
        }
    );

    // Check elements on page and elements on localStorage. If element is on page, 
    // but not in localStorage - remove element.
    let copy_wrappers = [...wrappers];
    for(let elem of copy_wrappers){
        // elem = <div class="wrapper" id="Keyboard">…</div>
        if(res.find(item => item.productName == elem.id) === undefined){
            insertF.parentNode.removeChild(elem);
        }
    };
};