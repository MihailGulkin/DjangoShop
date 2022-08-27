function active_button()
{

    if (!window.location.pathname.includes('comments'))
    {
        document.getElementById('desc_a').classList.add('description_a_active', 'disable')

    }
    else
    {
        document.getElementById('id_comment').classList.add('description_a_active', 'disable')
    }
}
active_button()