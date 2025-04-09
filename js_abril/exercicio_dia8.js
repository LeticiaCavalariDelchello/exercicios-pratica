// Exercício dia 8 - Receber um valor e dobrar ele
function dobrar(numero) {
    return numero * 2;
}

let numero = Number(prompt('Digite um valor:'));
let resultado = dobrar(numero);
console.log(`O dobro do número ${numero} digitado é ${resultado}.`);