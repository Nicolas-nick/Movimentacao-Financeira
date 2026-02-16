# Sistema de Movimentação Financeira

Projeto desenvolvido para processar movimentações financeiras a partir de um arquivo CSV, calculando saldos por conta, totais de crédito e débito, além de identificar inconsistências e lançamentos duplicados.


## Funcionalidades

- Leitura de arquivo CSV com movimentações financeiras
- Cálculo de saldo final por conta
- Cálculo total de créditos e débitos
- Identificação de:
  - Tipos inválidos
  - Contas com saldo negativo
  - Lançamentos duplicados
- Geração de relatório organizado no terminal
- Fechamento diário por conta


##  Estrutura do Projeto
├── main.py
├── Dados.csv (arquivo de entrada - ignorado no git)
└── README.md


## Formato do Arquivo CSV

O arquivo deve seguir o padrão:
2026-02-01;ContaA;C;1000;Saldo inicial
2026-02-02;ContaA;D;200;Compra mercado


### Regras:

- `C` = Crédito (soma ao saldo)
- `D` = Débito (subtrai do saldo)

---

## ▶ Como Executar

1. Certifique-se de ter o Python 3 instalado
2. Coloque o arquivo `Dados.csv` na mesma pasta do projeto
3. Execute:

O relatório será exibido no terminal.


## Regras de Negócio Implementadas

- Créditos somam ao saldo da conta
- Débitos subtraem do saldo
- Contas são exibidas em ordem alfabética
- Movimentações duplicadas são ignoradas
- Inconsistências são registradas no relatório
- O saldo diário é atualizado conforme a movimentação



##  Tecnologias Utilizadas

- Python 3
- Biblioteca padrão `csv`


##  Observações

Projeto desenvolvido para fins educacionais e avaliação técnica em processo seletivo.


## Observações Técnicas

Este projeto foi desenvolvido utilizando a biblioteca padrão `csv` do Python, especificamente o `csv.DictReader`, para realizar a leitura estruturada do arquivo CSV.

Embora bibliotecas como o `pandas` ofereçam recursos avançados para manipulação de dados, a escolha por utilizar apenas a biblioteca padrão teve como objetivo:

- Demonstrar domínio da lógica de processamento manual
- Evidenciar compreensão de estruturas de dados (dicionários, listas e sets)
- Manter o projeto leve e sem dependências externas
- Atender aos requisitos técnicos propostos no processo seletivo

A implementação prioriza clareza, organização e aplicação das regras de negócio diretamente no código.


##  Autor

Nicolas Rodrigues

