const search = document.querySelector('#etnia')

const ResultsSearch = (data) => {
    const content = document.querySelector('.datalist')
    content.innerHTML = ''
    for (const el of data) {
        content.innerHTML += `<p class="p">${el}</p>`
    }
    const p = document.querySelectorAll('.p').forEach(p => {
        p.addEventListener("click", target => {
            search.value = p.innerHTML
        });
    });
    
}
var oi;
fetch('/get/etnia')
.then(data => data.json())
.then(array => {
    const data = array['etnia']
    search.addEventListener('input', target => {
    oi = data.filter(e => e.toLocaleLowerCase().includes(search.value.toLocaleLowerCase()))
    ResultsSearch(oi)
    })
    document.querySelector('#form').addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && search.value != oi[0]) {
            e.preventDefault()
            console.log(oi.length)
            if (oi.length >0) {
                search.value = oi[0]
            }

        }
    })
    let prox = document.querySelector('#proximo')
    prox.addEventListener('click', e => {
        if (search.value != oi[0]) {
            e.preventDefault()
            if (oi.length>0) {
                search.value = oi[0]
            }
        }
    })

    search.addEventListener('click', target => {
    let oi = data.filter(e => e.toLocaleLowerCase().includes(search.value.toLocaleLowerCase()))
    ResultsSearch(oi)
    })
})