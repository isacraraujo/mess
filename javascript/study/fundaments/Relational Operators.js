console.log('01)', '1' == 1) // são iguais estou comparando valores
console.log('02)', '1' === 1) // são extritamente iguais (considerada não só o valor, mas também os tipos das variáveis)
console.log('03)', '3' != 3) // é diferente
console.log('04)', '3' !== 3) // é extritamente diferente

console.log('05)', 3 < 2) // é menor que
console.log('06)', 3 > 2) // é maior que
console.log('07)', 3 <= 2) // é menor ou igual
console.log('08)', 3 >= 2) // é maior ou igual

const d1 = new Date(0)
const d2 = new Date(0)
console.log('09)', d1 === d2)
console.log('10)', d1 == d2)
console.log('11)', d1.getTime() === d2.getTime())

console.log('12)', undefined == null)
console.log('13)', undefined === null)