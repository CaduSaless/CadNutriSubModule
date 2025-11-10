const radio = document.querySelectorAll('.item')
const progresso = document.querySelector('.completado')
const variaveis = document.querySelector('.variaveis-py')
const texto = document.querySelector('h3')
texto.innerHTML = `${100 - Number(variaveis.innerHTML)}% Completado`
progresso.style.transition = "width 0.7s ease-out";
progresso.style.width = `${variaveis.innerHTML}%`


const gRadio = document.querySelectorAll('.item-grande')

for (const el of radio) {
    el.addEventListener('click', () => {
        for (const element of gRadio) {
            element.className = 'item-grande'
        }
        for (const element of radio) {
            element.className = 'item'
        }
        el.className = 'item-selecionado'
        el.childNodes[1].checked = true
    })
}


for (const el of gRadio) {
    el.addEventListener('click', () => {
        for (const element of gRadio) {
            element.className = 'item-grande'
        }
        for (const element of radio) {
            element.className = 'item'
        }
        el.className = 'item-selecionado-g'
        el.childNodes[1].checked = true
    })
}
