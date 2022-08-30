function validator_submit()
{
     const inputs = document.getElementsByClassName('bucket_profile_input')
        for (let input of inputs)
        {
            input.addEventListener('input', function ()
            {
                if (input.value.toString().length > 3)
                {
                    input.value = input.value.slice(0, 3)
                }
            })
            input.addEventListener('change', () =>
            {

                document.getElementById(`form${input.id}`).submit()
            })
        }
}
validator_submit()