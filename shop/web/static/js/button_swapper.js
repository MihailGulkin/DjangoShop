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