function viewOrCloseAlert(){
    let isActiveAlert = localStorage.getItem('newSupply');
    if (0 < isActiveAlert){
        localStorage.setItem('newSupply', 0);
        let alert = document.getElementById('supply__created');
        alert.classList.remove('hidden_field');
    }
};

viewOrCloseAlert();
