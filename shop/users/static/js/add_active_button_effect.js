function active_button()
{
    const path_name = window.location.pathname
    if (path_name.includes('personal'))
    {
        document.getElementById('profile_a_personal').classList.add('activate_btn_a')
    }
    else if(path_name.includes('bucket'))
    {
        document.getElementById('profile_a_bucket').classList.add('activate_btn_a')
    }
    else
    {
        document.getElementById('profile_a_main').classList.add('activate_btn_a')
    }

}
active_button()