function active_button()
{

    if (window.location.pathname.includes('personal'))
    {
        document.getElementById('profile_a_personal').classList.add('activate_btn_a')

    } else
    {
        document.getElementById('profile_a_main').classList.add('activate_btn_a')
    }
}
active_button()