function calculaMac(linha){
    let acs = linha.querySelectorAll('td.ac')
    let tdMac = linha.querySelector('td.mac')
    let mac = 0
    
    for(let com=0;com<acs.lenght;com++){
        let td = acs[com]
        let nota = parseFloat(td.textContent)
        mac += nota
    }
    
    mac = mac/acs.length
    tdMac.textContent=mac
    if(mac >= 6){
        tdMac.style.color = 'green'
    }else{
        tdMac.style.color = 'red'
    }
}
const linhas = document.querySelectorAll('tr')
const btnPndera = document.querySelector('#titulo')
btnPndera.onclick = function(){
    let macs = document.querySelectorAll('td.mac')
    for(let i = 0; i<macs.lenght; i++){
        let nota = parseFloat(macs[i].textContent)
        nota = nota*0.6
        macs[i].textContent = nota
    }
}

for(let i=1; i < linhas.length; i++){
    let linha = linhas[1]
    calculaMac(linha)
}



