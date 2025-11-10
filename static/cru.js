const inp = document.querySelector('#cpf')
inp.addEventListener('input', (el) => {
    let valor = inp.value
    let tam = inp.value.length
    console.log(el)
    console.log(el.data)
    if (el.data != null) {
        if (tam == 3 || tam == 7) {
            inp.value =  `${valor}.`
            console.log(valor)
        } else if (tam == 11) {
            inp.value =  `${valor}-`
            console.log(valor)
        }
    }
})