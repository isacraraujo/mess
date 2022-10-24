//Type 1
const carro  = {}
carro.nome   = "Audi"
carro.ano    = 2019
carro.idade  = function (){
    let date = new Date()
    return date.getFullYear() - carro.ano
}
console.log(`${carro.idade()} anos`)

//Type 2
const carro = {
    nome:  "Audi",
    ano:   2019,
    idade: function (){
        let date = new Date()
        return date.getFullYear() - carro.ano
    }
}
console.log(`${carro.idade()} anos`)