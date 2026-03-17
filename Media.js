const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const notas = [];

function calculing(notas) {
  const soma = notas.reduce((acc, n) => acc + n, 0);
  const resultado = soma / notas.length;
  console.log(`soma: ${soma}, quantidade: ${notas.length}, média: ${resultado}`);
  console.log(resultado >= 7 ? "Aprovado" : "Reprovado");
}

function prompt() {
  rl.question("Digite uma nota (ou 'sair' para encerrar): ", (input) => {
    input = input.trim();

    if (input === "sair") {
      calculing(notas);
      rl.close();
      return;
    }

    const nota = parseFloat(input);

    if (isNaN(nota)) {
      console.log("Entrada inválida. Por favor, digite um número ou 'sair'.");
    } else if (nota < 0 || nota > 10) {
      console.log("Nota inválida. Por favor, digite um número entre 0 e 10.");
    } else {
      notas.push(nota);
    }

    prompt();
  });
}

prompt();