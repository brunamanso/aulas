function calculaMac(linha){
    let acs = linha.querySelectorAll('td.ac')
    let tdMac = linha.querySelector('td.mac')
    let mac = 0
    
    for( let i = 0; i < acs.length; i++ ){
        let td = acs[i]
        let nota = parseFloat(td.textContent)
        mac += nota
    }
    
    mac = mac / acs.length
    tdMac.textContent = mac
    if(mac >= 6){
        tdMac.style.color = 'green'
    } else {
        tdMac.style.color = 'red'
    }
}

function calculaMp(linha){
    let prova = linha.querySelector('td.prova')
    let sub = linha.querySelector('td.sub')
    let tdMp = linha.querySelector('td.mp')
    let mp = 0
    
    if(sub.textContent == "N/A"){
        sub.textContent = 0
    }

    if(prova.textContent >= sub.textContent){
        tdMp.textContent = prova.textContent
    }else{
        tdMp.textContent = sub.textContent
    }
    
   
    if(tdMp.textContent >= 6){
        tdMp.style.color = 'green'
    } else {
        tdMp.style.color = 'red'
    }
}

function calculamf(linha){
    let mp = linha.querySelector('td.mp')
    let mac = linha.querySelector('td.mac')
    let tdMf = linha.querySelector('td.mf')
    
    let macp = mac.textContent * 0.6
    let mpp = mp.textContent * 0.4
    
    tdMf.textContent = macp + mpp
    
    if(tdMf.textContent >= 6){
        tdMf.style.color = 'green'
    } else {
        tdMf.style.color = 'red'
    }
}

const linhas = document.querySelectorAll('tr')

const btnPonderar = document.querySelector('#botao')

btnPonderar.addEventListener('click',function(){
    let macs = document.querySelectorAll('td.mac')
    for (let i = 0; i < macs.length; i++){
        let nota = parseFloat(macs[i].textContent)
        nota = nota*0.6
        macs[i].textContent = nota
    }
})

btnPonderar.addEventListener('click',function(){
    let mp = document.querySelectorAll('td.mp')
    for (let i = 0; i < mp.length; i++){
        let nota = parseFloat(mp[i].textContent)
        nota = nota*0.4
        mp[i].textContent = nota
    }
})


for(let i = 1; i < linhas.length; i++){
    let linha = linhas[i]
    calculaMac(linha)
    calculaMp(linha)
    calculamf(linha)
}


