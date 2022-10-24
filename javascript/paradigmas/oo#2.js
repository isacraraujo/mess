class Carro {
    constructor(nome, ano){
        this.nome = nome
        this.ano  = ano
    }
    idade(){
        let date = new Date()
        return date.getFullYear() - this.ano
    }
}

let meuCarro = new Carro("Audi", 2019)
console.log(`${meuCarro.idade()} anos`)