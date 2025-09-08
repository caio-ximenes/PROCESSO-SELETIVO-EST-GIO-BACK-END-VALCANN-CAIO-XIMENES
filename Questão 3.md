# Questão 3
### As propostas Problema > Causa > Solução estão organizadas em primeiro, segundo, terceiro e quarto itens de forma respectiva entre si, ou seja, o primeiro problema tem a primeira causa e assim por diante..




# Cenário:
    "Uma empresa possui um software com Node.js (backend) e React (frontend).
     Atualmente, a cada nova versão, o cliente empacota os componentes manualmente 
     e realiza o deploy em homologação. Após uma semana, repete o processo para produção."

  

# Problemas:

* ### Esquecer de empacotar alguma dependencia como bibliotecas, códigos importados ou frameworks.
* ### Processos repetitivos, cansativos e dependencia de anotações do desenvolvedor.
* ### Fase de homologação sucetível a erros humanos.
* ### Redundância de processos.

# Causas:
* ### Todos os requisitos têm que ser prescritos manualmente.
* ### Excesso de códigos tanto de variedade quanto de quantidade.
* ### Todas as funcionalidades precisam ser repetidamente testadas  na homologação a cada deploy.
* ### Repete-se o mesmo processo cansativo para duas fazes (homologação e produção).

# Soluções:
* ### Uso de libs ou ferramentas como npm ou yarn para empacotar e organizar os requisitos de maneira automática e organizada. 
* ### Automação com ativação por commit usando GitHub Actions para execução autonoma dos códigos de deploy.
* ### Uso de testes automatizados antes do ambiente de homologação.
* ### A partir de que se executa o código para fase de homologação, é possível fazer integração com chatbot via MSTeams ou Discord para esperar por mensagem a aprovação que por sua vez ativa o deploy automático rumo a produção.

<br><br><br><br><br>![Diagrama de arquitetura](questao3.png)
