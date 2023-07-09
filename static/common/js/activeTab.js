let docPage = document;

function stylingActiveTab(){
    const currentUrl = window.location.href;
    let currentTab = null;

    if (currentUrl.includes('product')){
        currentTab = docPage.getElementById('product');
    } else if (currentUrl.includes('supply')){
        currentTab = docPage.getElementById('supply');
    } else if (currentUrl.includes('analytics')){
        currentTab = docPage.getElementById('analytics');
    } else if (!(currentUrl.includes('help') | currentUrl.includes('about'))) {
        currentTab = docPage.getElementById('sale');
    }

    try{
        currentTab.classList.add('active_tab');
    } catch (err) {
        console.log('')
    };

};

stylingActiveTab();
