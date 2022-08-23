const buttons_filter = document.getElementsByClassName('shop_not_active')
let temp_button = 'f'
let btn_flag = true
for (let button of buttons_filter)
{

    button.addEventListener('click', function ()
    {
        if (btn_flag)
        {
            reset_class(buttons_filter)
            reset_color(buttons_filter)
            button.classList.add('shop_activate')

        }
        if (button.attributes[0].value !== temp_button && btn_flag)
        {

            btn_flag = false
            const all_products = document.getElementsByClassName('shop_product_container')
            temp_button = button.attributes[0].value
            for (let product of all_products)
            {
                if (!product.classList.contains(`${button.attributes[0].value}`) && button.attributes[0].value !== 'all')
                {
                    product.classList.add('hide')

                    setTimeout(function ()
                    {
                        product.classList.add('delete_obj')
                        btn_flag = true
                    }, 701)
                } else
                {
                    product.classList.remove('hide')
                    product.classList.remove('delete_obj')
                    setTimeout(function ()
                    {
                        btn_flag = true
                    }, 701)
                }
            }
        }
    })
}
