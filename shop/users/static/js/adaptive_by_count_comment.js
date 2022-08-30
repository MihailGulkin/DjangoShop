function adaptive_by_count_comment()
{
    const profile_container = document.getElementsByClassName('profile_container_info_msg')[0]
    let h2_element = document.getElementById('profile_h2_container')
    h2_element = h2_element.textContent.replace('Мои отзывы(', '').replace(')', '')
    if (h2_element > 1)
    {
        profile_container.style.display = 'flex'
        profile_container.style.flexDirection = 'column'
        profile_container.style.justifyContent = 'space-between'
    }
}

adaptive_by_count_comment()