function lock_button()
{

    if(document.getElementsByClassName('js_locker')[0].textContent !== "В наличии")
    {
        for(let ele of document.getElementsByClassName('item_btn'))
        {
            ele.classList.add('disable')
        }
    }
}
lock_button()