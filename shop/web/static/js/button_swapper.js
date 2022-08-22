const buttons_swapper = document.getElementsByClassName('shop_not_active')
for (let button of buttons_swapper)
{
    button.addEventListener('click', function ()
    {
        reset_class(buttons_swapper)
        reset_color(buttons_swapper)
        button.classList.add('shop_activate')
    })
}

function reset_class(buttons)
{
    for (let button of buttons)
    {
        button.classList.remove('post_active')
    }
}

function reset_color(buttons)
{
    for (let button of buttons)
    {
        if (button.classList.contains('shop_activate'))
        {
            button.classList.remove('shop_activate')
            button.classList.add('post_active')
            return

        }
    }
}