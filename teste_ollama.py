from modules.SummarizerQwen3 import SummarizerQwen3
from modules import OutputManager

text = '''SPEAKER_00:  Iniciar a gravação, pronto.
SPEAKER_00:  É, então.
SPEAKER_01:  Aí vai estar gravando aqui também.
SPEAKER_00:  Bom.
SPEAKER_00:  Eu fiz algumas
SPEAKER_00:  anotações sobre...
SPEAKER_00:  Tem dois pontos, né, que tinha colocado.
SPEAKER_00:  A questão do Trello e a questão
SPEAKER_00:  de análise do projeto.
SPEAKER_00:  O Trello só tem uma questão que
SPEAKER_00:  aquele que você mandou,
SPEAKER_00:  eu consigo acessar ele.
SPEAKER_00:  Aqui. Eu consigo acessar esse
SPEAKER_00:  workspace, mas eu não consigo editar
SPEAKER_00:  ele. Eu não sei se eu...
SPEAKER_00:  Se é porque eu...
SPEAKER_01:  ainda não fazia parte da equipe
SPEAKER_01:  oficialmente no Teams
SPEAKER_01:  ou alguma coisa assim. Que era o motivo
SPEAKER_01:  de eu também não estar conseguindo mandar mensagem
SPEAKER_01:  no chat. Mas, enfim.
SPEAKER_01:  O Trello em específico eu não
SPEAKER_01:  consegui acessar e editar as coisas.
SPEAKER_01:  Mas, de qualquer forma, eu estava anotando
SPEAKER_01:  as coisas que precisava fazer
SPEAKER_01:  que eu observava
SPEAKER_01:  no Notion.
SPEAKER_01:  que eu estava fazendo algumas anotações
SPEAKER_01:  mais gerais
SPEAKER_01:  sobre o projeto.
SPEAKER_01:  Eu coloquei algumas melhorias
SPEAKER_01:  que eu tirei um tempo pra
SPEAKER_01:  dar uma olhada tanto no código
SPEAKER_01:  quanto no site em si.
SPEAKER_01:  Eu fiquei usando por algum tempo pra tentar
SPEAKER_01:  achar algumas partes que teria que melhorar.
SPEAKER_00:  Uma análise das tecnologias pra ver se tinha alguma coisa nova que eu não conhecia.
SPEAKER_00:  Isso, por exemplo, esse framework de front-end que vocês usaram
SPEAKER_00:  era um que eu nunca tinha usado, só que um framework de front-end não deve ser nada muito complicado de aprender.
SPEAKER_00:  E o outro também era essa tecnologia pra gerar PDFs.
SPEAKER_00:  E eu, quando vi, tinha ficado bem curioso pra saber
SPEAKER_00:  como é que funcionava.
SPEAKER_00:  Aí eu vi que tinha uma biblioteca, né, que importaram com Node
SPEAKER_00:  e usaram lá pra gerar, usando HTML.
SPEAKER_00:  a estrutura HTML.
SPEAKER_00:  A estrutura HTML, né.
SPEAKER_00:  É...
SPEAKER_00:  Tinha colocado algumas perguntas também, algumas dúvidas que eu ia tendo.
SPEAKER_00:  No caso eu não tive muitas, não consegui encontrar onde está hospedado.
SPEAKER_00:  Ahn...
SPEAKER_00:  E é mais isso.
SPEAKER_00:  Se quiser eu posso explicar mais dessas melhorias
SPEAKER_00:  ou se tiver alguma pergunta, alguma coisa que você queira ter certeza
SPEAKER_00:  se eu entendi direito ou não.
SPEAKER_00:  a vontade.
SPEAKER_00:  Primeira coisa, eu tô entrando aqui no Trello
SPEAKER_00:  só pra ver se você de alguma forma tá como...
SPEAKER_01:  Membro...
SPEAKER_01:  Eu acho que administra...
SPEAKER_01:  Eu vou te colocar como administrador pra ver se você consegue.
SPEAKER_01:  Você quer tentar de novo?
SPEAKER_01:  Eu vou entrar aqui.
SPEAKER_01:  Acho que fica mais...
SPEAKER_00:  Eu não entendi porque...
SPEAKER_01:  Ó...
SPEAKER_01:  Aqui tá...
SPEAKER_01:  Eu já tinha entrado antes quando você tinha me mandado inicialmente
SPEAKER_00:  e já tinha aparecido aqui que eu tava...
SPEAKER_01:  Pra mim pedir pra algum administrador
SPEAKER_01:  pra mim entrar na...
SPEAKER_01:  Na área de trabalho.
SPEAKER_01:  E aí tá aqui ainda a solicitação.
SPEAKER_01:  Então eu acredito que eu ainda precise ir.
SPEAKER_01:  Pode entrar como membro.
SPEAKER_01:  Solicitações para entrar.
SPEAKER_01:  Não há solicitações para entrar nesse quadro.
SPEAKER_01:  Ué...
SPEAKER_01:  Ah, eu te coloquei como administrador agora.
SPEAKER_00:  Deixa eu autorizar pra ver se muda alguma coisa.
SPEAKER_01:  Continua...
SPEAKER_00:  Ou é...
SPEAKER_00:  Será que...
SPEAKER_00:  Hum...
SPEAKER_00:  Hum...
SPEAKER_00:  Eu vou...
SPEAKER_00:  Eu vou remover um aluno do quadro.
SPEAKER_00:  Um dos alunos.
SPEAKER_00:  Que é o que não tava relacionado bem ao desenvolvimento.
SPEAKER_00:  Só pra ver se a quantidade de pessoas que estão no quadro, que pode ser a diferença, sabe?
SPEAKER_00:  Hum...
SPEAKER_00:  De alguma forma ele pode estar bloqueando porque é um recurso...
SPEAKER_01:  A gente tá usando um recurso gratuito.
SPEAKER_01:  Vamos ver se dá uma atualizada aí.
SPEAKER_01:  Tá.
SPEAKER_01:  Ainda tá.
SPEAKER_01:  Deixa eu...
SPEAKER_01:  Deixa eu...
SPEAKER_01:  Não sei se tá conseguindo editar.
SPEAKER_01:  Então...
SPEAKER_01:  É, assim, para o quadro.
SPEAKER_01:  Um dos alunos.
SPEAKER_01:  Um dos alunos.
SPEAKER_01:  Que é o que não tava relacionado bem ao desenvolvimento.
SPEAKER_01:  Só pra ver se a quantidade de pessoas que estão no quadro, que pode ser a diferença,
SPEAKER_01:  sabe?
SPEAKER_01:  Hum-hum.
SPEAKER_01:  Que de alguma forma ele pode estar bloqueando porque é um recurso...
SPEAKER_01:  A gente tá usando um recurso gratuito.
SPEAKER_01:  Vamos ver se...
SPEAKER_01:  Dá uma atualizada aí.
SPEAKER_00:  Tá.
SPEAKER_00:  Hum...
SPEAKER_00:  Ainda tá.
SPEAKER_00:  Mas você tá conseguindo editar
SPEAKER_00:  Deixa eu ver
SPEAKER_01:  Isso aqui apareceu pra você também?
SPEAKER_00:  Deixa eu abrir
SPEAKER_00:  Deixa eu só ver
SPEAKER_01:  Apareceu, teste
SPEAKER_01:  Apareceu?
SPEAKER_01:  Então
SPEAKER_00:  Agora abritou
SPEAKER_00:  Eu acho que tem a ver com a licença gratuita
SPEAKER_01:  E a quantidade de pessoas
SPEAKER_00:  Que ele deve bloquear
SPEAKER_01:  Eu posso até tentar adicionar
SPEAKER_00:  Ele me deixa adicionar
SPEAKER_00:  Mas a pessoa não vai ter
SPEAKER_01:  Não vai conseguir acessar os recursos aí
SPEAKER_01:  Então beleza
SPEAKER_01:  Tá resolvido, né?
SPEAKER_00:  Eu só
SPEAKER_00:  Como que eu apago isso?
SPEAKER_01:  Ah, esse é meio complicado
SPEAKER_01:  Porque ele pede
SPEAKER_01:  Ou eu arquivo
SPEAKER_01:  Ou eu edito
SPEAKER_01:  Ah, não tem como apagar
SPEAKER_01:  Não apaga
SPEAKER_00:  Eu acho que justamente
SPEAKER_01:  Uma forma de
SPEAKER_01:  De você ter um rastreio
SPEAKER_01:  Sobre o que foi inserido, sabe?
SPEAKER_01:  Você pode editar
SPEAKER_01:  Você não pode remover o cartão
SPEAKER_01:  Você pode arquivar ele
SPEAKER_01:  Tá
SPEAKER_01:  Entendi
SPEAKER_00:  Bom
SPEAKER_00:  Ah, o que eu ia te perguntar
SPEAKER_00:  Você pegou o projeto
SPEAKER_01:  E aí você pegou as partes
SPEAKER_01:  Assim, os objetivos
SPEAKER_01:  Quais são as metas
SPEAKER_01:  E aí com base
SPEAKER_01:  No projeto
SPEAKER_01:  Você foi levantando aqueles pontos
SPEAKER_01:  Que você colocou
SPEAKER_01:  Sim
SPEAKER_01:  Com base
SPEAKER_00:  Tanto no projeto
SPEAKER_01:  Nessa parte já aplicada
SPEAKER_01:  Quanto no código
SPEAKER_01:  Tem algumas coisas
SPEAKER_01:  Inclusive eu gravei um vídeo
SPEAKER_01:  Porque não era algo que eu ia conseguir
SPEAKER_01:  Só falar
SPEAKER_01:  Gravei um vídeo
SPEAKER_01:  De um problema
SPEAKER_01:  Que eu tinha visto
SPEAKER_01:  No site em si
SPEAKER_01:  Tem alguns problemas
SPEAKER_01:  Que eu tinha identificado
SPEAKER_01:  No código
SPEAKER_01:  Coisas pequenas
SPEAKER_01:  Mas só pra
SPEAKER_01:  Eu não esquecer de mudar
SPEAKER_01:  Né?
SPEAKER_01:  É
SPEAKER_00:  Enfim
SPEAKER_00:  Aquela questão que você tinha levantado
SPEAKER_00:  Também do PDF
SPEAKER_00:  Com
SPEAKER_00:  Ter duas questões
SPEAKER_00:  Duas colunas de questões
SPEAKER_00:  Pra
SPEAKER_00:  Ter um aproveitamento melhor
SPEAKER_00:  Da
SPEAKER_00:  Folha
SPEAKER_00:  E
SPEAKER_00:  Enfim
SPEAKER_00:  Isso aqui era um link
SPEAKER_00:  Dessa
SPEAKER_01:  Calma
SPEAKER_00:  Dessa página inicial aqui
SPEAKER_00:  Que apontava pra
SPEAKER_00:  Lugar nenhum
SPEAKER_00:  Mas eu acho que ele tinha um lugar
SPEAKER_00:  Pra apontar
SPEAKER_00:  Não vou lembrar qual link é agora
SPEAKER_00:  Mas eu deixei a linha anotada aqui
SPEAKER_00:  É
SPEAKER_00:  Tem um
SPEAKER_00:  Isso aqui também é detalhe de implementação
SPEAKER_00:  Isso aqui é o que você tinha levantado
SPEAKER_00:  Isso aqui
SPEAKER_00:  Vocês tem algum ícone que vocês estão usando pra esse projeto?
SPEAKER_00:  Algum
SPEAKER_00:  Uma logo
SPEAKER_00:  Ou algo assim?
SPEAKER_00:  É
SPEAKER_01:  Não
SPEAKER_01:  Não
SPEAKER_01:  Não foi
SPEAKER_01:  Não foi desenvolvido não
SPEAKER_01:  Também
SPEAKER_01:  É algo que
SPEAKER_00:  Dá pra trabalhar
SPEAKER_00:  E tá relacionado com esse favicon
SPEAKER_00:  Que eu tinha deixado anotado
SPEAKER_00:  Que seria interessante ter
SPEAKER_00:  Que é o iconezinho
SPEAKER_01:  Que fica
SPEAKER_01:  Aqui na aba
SPEAKER_01:  Quando você
SPEAKER_01:  Abre no navegador
SPEAKER_01:  Entendi
SPEAKER_01:  Legal
SPEAKER_01:  Assim
SPEAKER_00:  O que eu não sei se
SPEAKER_01:  Na leitura
SPEAKER_01:  Você conseguiu entender
SPEAKER_01:  Essa parte
SPEAKER_01:  De que
SPEAKER_01:  Por exemplo
SPEAKER_01:  Eu abri até projeto aqui
SPEAKER_01:  Pra ter certeza
SPEAKER_01:  Que essa parte do módulo de revisão de conteúdos
SPEAKER_01:  É um módulo lição
SPEAKER_01:  Que é projetado para permitir que os professores disponibilizem diversos materiais de revisão
SPEAKER_01:  Como mapas mentais, videoaulas e apostilas
SPEAKER_01:  Foi um pouquinho que a gente conversou, né?
SPEAKER_01:  Na última reunião
SPEAKER_01:  Esses recursos serão fundamentais para reforçar o aprendizado e ajudar os alunos
SPEAKER_01:  Isso seria
SPEAKER_01:  É um recurso novo que vai ser adicionado
SPEAKER_01:  Que é o que não está aqui ainda
SPEAKER_01:  Aham
SPEAKER_01:  Então
SPEAKER_00:  A gente não tem esse módulo
SPEAKER_01:  Um módulo revisão
SPEAKER_00:  Um módulo de
SPEAKER_00:  De inserir conteúdos, né?
SPEAKER_01:  Essa parte
SPEAKER_01:  A intenção seria ter
SPEAKER_00:  Literalmente conteúdos
SPEAKER_00:  Não questões ou algo assim
SPEAKER_00:  É mais o conteúdo em si
SPEAKER_00:  Descrito
SPEAKER_01:  Isso
SPEAKER_01:  Tá
SPEAKER_01:  Daí
SPEAKER_01:  Quem sabe
SPEAKER_01:  Dá pra pensar junto
SPEAKER_01:  Em conjunto
SPEAKER_01:  Com o Nicolas
SPEAKER_01:  O Nicolas vai pensar
SPEAKER_01:  Provavelmente junto com a Ana Paula
SPEAKER_01:  Na gamificação disso
SPEAKER_01:  Então ele depois vai pensar em como organizar
SPEAKER_01:  Por exemplo
SPEAKER_01:  As questões que vão estar no local
SPEAKER_01:  Com os conteúdos que vão estar disponibilizados, né?
SPEAKER_01:  Organizados
SPEAKER_01:  E ele também comentou
SPEAKER_01:  Eu não sei se você chegou a participar dessa conversa
SPEAKER_01:  De às vezes direcionar
SPEAKER_01:  Por exemplo
SPEAKER_01:  Fazer direcionamento para links externos
SPEAKER_01:  Mas eu acho que a sua preocupação agora
SPEAKER_01:  É construir um espaço em que o professor consiga inserir material
SPEAKER_01:  Seja link, videoaula, né?
SPEAKER_01:  Seja relacionado àquele assunto
SPEAKER_01:  Ele gostou daquela videoaula
SPEAKER_00:  Ele achou que é importante
SPEAKER_01:  E...
SPEAKER_00:  Ou seja
SPEAKER_01:  Alguma lista de revisão
SPEAKER_01:  Ou seja
SPEAKER_01:  Algum...
SPEAKER_01:  Algum mapa mental
SPEAKER_01:  Ou uma apostila
SPEAKER_01:  Entendi
SPEAKER_01:  Bom
SPEAKER_00:  Então isso não está implementado
SPEAKER_00:  Quanto a isso
SPEAKER_01:  Nessa parte de menu aqui
SPEAKER_00:  Eu acredito que esteja aqui
SPEAKER_00:  Eu acho que pode ser interessante criar então mais duas seções aqui
SPEAKER_00:  Uma parte de conteúdo
SPEAKER_00:  E outra parte de questões
SPEAKER_00:  Questões aqui eu deixaria separado de simulados
SPEAKER_00:  Porque teria um objetivo de tipo
SPEAKER_01:  Como que eu explico isso?
SPEAKER_01:  Tipo
SPEAKER_00:  Tem uma parte aqui para você fazer
SPEAKER_00:  Era o que?
SPEAKER_00:  Era do conteúdo
SPEAKER_00:  Vou marcar com C
SPEAKER_00:  E tem uma outra parte com a questão das questões
SPEAKER_00:  As questões sendo avulsas
SPEAKER_00:  E não
SPEAKER_01:  Tando
SPEAKER_01:  Vinculadas a um simulado
SPEAKER_01:  Daria para
SPEAKER_01:  Talvez ter uma
SPEAKER_01:  Quantificação melhor
SPEAKER_01:  De taxa de erros
SPEAKER_01:  E acertos
SPEAKER_01:  Esse tipo de coisa
SPEAKER_01:  Que daria para facilitar
SPEAKER_01:  A implementação da gamificação
SPEAKER_01:  Então
SPEAKER_01:  A parte das questões ficarem separadas
SPEAKER_01:  Seria onde a pessoa entraria
SPEAKER_01:  Para realizar questões
SPEAKER_01:  Sobre algum assunto específico
SPEAKER_01:  Que ele queira estudar
SPEAKER_01:  E
SPEAKER_01:  Sem precisar montar uma prova
SPEAKER_01:  Com início e fim
SPEAKER_01:  Ele faz o tanto que ele
SPEAKER_01:  Que ele estiver disposto a fazer
SPEAKER_01:  E ganhando a recompensa por isso
SPEAKER_01:  Mas
SPEAKER_01:  A recompensa em si é
SPEAKER_01:  É algo
SPEAKER_01:  A ser pensado na parte da gamificação
SPEAKER_01:  Sim
SPEAKER_01:  A gente
SPEAKER_01:  Conversou com o Nicolas
SPEAKER_01:  Depois de amanhã
SPEAKER_01:  A gente pode tentar conversar de novo
SPEAKER_01:  Amanhã inclusive
SPEAKER_01:  Eu vou ter reunião com ele
SPEAKER_01:  Durante o período da aula
SPEAKER_01:  Da aula mesmo da manhã
SPEAKER_01:  Eu vou até o laboratório
SPEAKER_01:  Em algum momento
SPEAKER_01:  Se você
SPEAKER_01:  Quiser trocar alguma ideia
SPEAKER_01:  Eu acho que pode ser
SPEAKER_01:  Na hora do intervalo
SPEAKER_01:  Também
SPEAKER_01:  E
SPEAKER_01:  Mas o que
SPEAKER_00:  O que eu queria comentar
SPEAKER_01:  É assim
SPEAKER_00:  As questões
SPEAKER_00:  Elas são inseridas individualmente
SPEAKER_00:  Né
SPEAKER_00:  E aí a gente classifica elas
SPEAKER_00:  Por tema
SPEAKER_00:  Por exemplo
SPEAKER_00:  Ela tem uma área
SPEAKER_01:  E tem um tópico
SPEAKER_01:  E às vezes tem mais de um tópico
SPEAKER_01:  Ela pode estar associada
SPEAKER_01:  A mais de um tópico
SPEAKER_01:  E subtópico
SPEAKER_00:  E subtópico também é possível
SPEAKER_01:  Então o aluno
SPEAKER_01:  Quando ele for
SPEAKER_01:  Querer revisar
SPEAKER_01:  Ele pode selecionar
SPEAKER_01:  Ele pode selecionar
SPEAKER_01:  O tipo de questão
SPEAKER_01:  O tipo de questão
SPEAKER_01:  O tipo de assunto
SPEAKER_01:  Eu na verdade
SPEAKER_01:  Como eu estou no modo administrador
SPEAKER_01:  E modo aluno
SPEAKER_01:  Eu não sei muito bem
SPEAKER_01:  Como é que está funcionando
SPEAKER_01:  O modo aluno
SPEAKER_01:  Você está no modo aluno?
SPEAKER_01:  Esse aqui é o modo aluno
SPEAKER_01:  É
SPEAKER_00:  Então
SPEAKER_01:  Como que está funcionando
SPEAKER_01:  Vamos dar uma olhadinha
SPEAKER_01:  Para ver como é que está funcionando
SPEAKER_01:  Por exemplo
SPEAKER_01:  Criar o simulado
SPEAKER_01:  Eu não estou lembrando
SPEAKER_01:  De como está isso
SPEAKER_01:  É
SPEAKER_00:  Descrição
SPEAKER_00:  É
SPEAKER_00:  Algum específico
SPEAKER_00:  Que você quer testar?
SPEAKER_00:  Vamos para a objetiva mesmo
SPEAKER_00:  Ok
SPEAKER_01:  E daí como é que ele é aleatório
SPEAKER_00:  Por exemplo
SPEAKER_01:  Ele poderia
SPEAKER_01:  Ali tem como
SPEAKER_01:  Ah dá para filtrar por assunto
SPEAKER_01:  Então ele pode filtrar por área
SPEAKER_01:  Por área ou por assunto
SPEAKER_01:  Por tópico
SPEAKER_01:  Pode ser matemática
SPEAKER_01:  Era isso que você queria dizer?
SPEAKER_00:  Ou não necessariamente
SPEAKER_01:  Ele precisa criar um simulado
SPEAKER_01:  Mas
SPEAKER_01:  Aí qual seria a sua ideia?
SPEAKER_01:  A intenção é que as questões
SPEAKER_01:  Fossem independentes
SPEAKER_00:  E você não precisasse criar um simulado
SPEAKER_00:  Para
SPEAKER_00:  Para precisar fazer as questões do simulado
SPEAKER_00:  Entendeu?
SPEAKER_00:  E aí como que seria a sua ideia?
SPEAKER_00:  Eu estou tentando entender
SPEAKER_01:  Porque se for interessante
SPEAKER_01:  No sentido de
SPEAKER_01:  Do ponto de vista do usuário
SPEAKER_01:  A gente pode implementar sim
SPEAKER_01:  Mas a ideia seria
SPEAKER_01:  Como que o aluno chegaria nessa questão?
SPEAKER_01:  Só para eu entender
SPEAKER_01:  Como que ele acessaria?
SPEAKER_01:  Bom, basicamente
SPEAKER_01:  Isso eu acabei de pensar literalmente
SPEAKER_00:  Porque
SPEAKER_01:  A ideia surgiu com o que você falou
SPEAKER_01:  Mas basicamente uma questão
SPEAKER_01:  Uma aba de questões aqui
SPEAKER_01:  Que você clica
SPEAKER_01:  E aí você pode
SPEAKER_01:  Ou selecionar temas gerais
SPEAKER_01:  Ou você pode deixar
SPEAKER_01:  Em uma área específica
SPEAKER_01:  Ou algum tópico específico
SPEAKER_01:  E vai vindo questão
SPEAKER_01:  E você vai resolvendo
SPEAKER_01:  Eu não sei se vocês chegaram
SPEAKER_01:  A pesquisar em outras plataformas
SPEAKER_01:  Que fazem isso
SPEAKER_01:  Mas
SPEAKER_01:  Quando eu comecei a pensar
SPEAKER_01:  No meu projeto pessoal
SPEAKER_01:  Que eu tinha pensado
SPEAKER_01:  Em fazer algo parecido
SPEAKER_01:  De questões
SPEAKER_01:  De uma forma mais gamificada
SPEAKER_01:  Tinha um amigo que fazia bastante
SPEAKER_01:  Usava essa plataforma aqui
SPEAKER_01:  E aí
SPEAKER_01:  Eu ficava pensando
SPEAKER_01:  Se essa plataforma
SPEAKER_01:  Tivesse uma gamificação
SPEAKER_01:  Mais interessante
SPEAKER_01:  Assim
SPEAKER_01:  E motivasse mais
SPEAKER_01:  A estudar
SPEAKER_01:  Basicamente
SPEAKER_01:  Deixa eu pegar aqui
SPEAKER_01:  Algum
SPEAKER_01:  Aqui
SPEAKER_01:  Basicamente tem como você
SPEAKER_01:  Filtrar aqui
SPEAKER_01:  E tem questão
SPEAKER_01:  Aí vai aparecendo essa questão
SPEAKER_01:  Se você só vai resolvendo
SPEAKER_01:  Tanto que você quiser
SPEAKER_01:  Resolver
SPEAKER_01:  E depois você sai
SPEAKER_01:  E aí
SPEAKER_01:  Fica
SPEAKER_01:  Conforme você vai resolvendo
SPEAKER_01:  Fica
SPEAKER_01:  Marcada na sua conta
SPEAKER_01:  Sua taxa de acerto
SPEAKER_01:  Sua taxa de acerto
SPEAKER_01:  Por tema
SPEAKER_01:  Esse tipo de coisa
SPEAKER_01:  Não pode ser
SPEAKER_01:  Eu pensei que
SPEAKER_01:  Quem sabe
SPEAKER_01:  Isso estaria mais relacionado
SPEAKER_01:  A gamificação
SPEAKER_01:  Você
SPEAKER_01:  Acho que não né
SPEAKER_01:  Não
SPEAKER_01:  Não mas é isso mesmo
SPEAKER_01:  Isso é pra facilitar
SPEAKER_00:  Implementar a gamificação
SPEAKER_01:  Na
SPEAKER_01:  No
SPEAKER_00:  Site
SPEAKER_01:  Não beleza
SPEAKER_00:  Boa ideia
SPEAKER_01:  E outra coisa
SPEAKER_01:  A gente chegou a acessar
SPEAKER_00:  Uma
SPEAKER_01:  Plataforma
SPEAKER_01:  Assim
SPEAKER_01:  E
SPEAKER_01:  E aí
SPEAKER_01:  O
SPEAKER_01:  O Nicolas
SPEAKER_01:  Ele mostrou
SPEAKER_01:  Essa taxa de acerto
SPEAKER_01:  Como que fica assim
SPEAKER_01:  O feedback
SPEAKER_01:  Pro aluno
SPEAKER_01:  Que é interessante né
SPEAKER_01:  Dá pra saber também
SPEAKER_01:  O que tem que estudar mais
SPEAKER_00:  O que você está
SPEAKER_00:  Errando com mais frequência
SPEAKER_01:  Qualquer área
SPEAKER_01:  Ele tem que
SPEAKER_01:  Investir mais
SPEAKER_01:  Pelo
SPEAKER_01:  Pelo
SPEAKER_01:  Escórdia
SPEAKER_01:  Outra coisa
SPEAKER_01:  Também é
SPEAKER_00:  Que as questões
SPEAKER_01:  Tendo
SPEAKER_01:  Os tópicos
SPEAKER_01:  Associados
SPEAKER_01:  Igual você tinha comentado
SPEAKER_01:  A gente pode
SPEAKER_01:  Criar uma conexão
SPEAKER_01:  Entre os tópicos
SPEAKER_01:  Das questões
SPEAKER_01:  E os tópicos
SPEAKER_01:  Dos conteúdos
SPEAKER_01:  Porque aí
SPEAKER_01:  Na própria questão
SPEAKER_01:  Pode ter algum
SPEAKER_01:  Direcionamento
SPEAKER_01:  Pra o conteúdo
SPEAKER_01:  Dentro da página
SPEAKER_01:  Pra pessoa
SPEAKER_01:  Poder revisar aquilo
SPEAKER_01:  Se tiver disponível
SPEAKER_01:  E aí pode ter
SPEAKER_01:  Alguma explicação
SPEAKER_01:  De algum professor
SPEAKER_01:  Que escreveu
SPEAKER_01:  Mesmo
SPEAKER_01:  Ou
SPEAKER_01:  Alguma indicação
SPEAKER_01:  De material da internet
SPEAKER_01:  Seja em texto
SPEAKER_01:  Vídeo
SPEAKER_01:  Ou qualquer coisa assim
SPEAKER_01:  Sim
SPEAKER_01:  Perfeito
SPEAKER_01:  Não
SPEAKER_01:  É isso mesmo
SPEAKER_01:  A gente
SPEAKER_01:  Pede pro
SPEAKER_01:  Sócio
SPEAKER_01:  Nesse
SPEAKER_01:  Revisar isso
SPEAKER_01:  E ver se essa ideia
SPEAKER_01:  É
SPEAKER_01:  É possível
SPEAKER_01:  Mas eu acredito
SPEAKER_01:  Que
SPEAKER_01:  Assim
SPEAKER_01:  Do meu ponto de vista
SPEAKER_01:  É bem interessante
SPEAKER_01:  É o que eu gostaria
SPEAKER_01:  Também
SPEAKER_01:  Eu acho que é isso
SPEAKER_01:  Viu
SPEAKER_00:  João
SPEAKER_01:  Por enquanto
SPEAKER_01:  Ok
SPEAKER_01:  Tem mais alguma pergunta
SPEAKER_00:  Alguma coisa
SPEAKER_00:  Que você queria saber
SPEAKER_00:  Se eu entendi direito
SPEAKER_00:  As tecnologias
SPEAKER_00:  Pelo que você comentou
SPEAKER_01:  Você já conhecia todas
SPEAKER_01:  E tem algumas
SPEAKER_01:  Ferramentas
SPEAKER_01:  Só
SPEAKER_01:  Que você colocou
SPEAKER_01:  Ali
SPEAKER_01:  Sim
SPEAKER_01:  Mas é
SPEAKER_00:  Tipo
SPEAKER_00:  São coisas
SPEAKER_01:  Bem
SPEAKER_00:  Fácil de pegar
SPEAKER_00:  E você
SPEAKER_00:  Já
SPEAKER_01:  Você está
SPEAKER_01:  Você está
SPEAKER_01:  Na
SPEAKER_01:  Desenvolvimento
SPEAKER_01:  Web 2
SPEAKER_01:  Web 1
SPEAKER_01:  Na verdade
SPEAKER_00:  Web 2
SPEAKER_00:  É o próximo semestre
SPEAKER_01:  Tá
SPEAKER_01:  Então beleza
SPEAKER_01:  Mas é legal
SPEAKER_01:  Que você já
SPEAKER_01:  Já vai direcionando
SPEAKER_01:  Aí
SPEAKER_01:  Já tem uma noção
SPEAKER_01:  E vai aprofundando
SPEAKER_01:  Dentro de outras
SPEAKER_01:  Ferramentas
SPEAKER_01:  Sim
SPEAKER_01:  Ah
SPEAKER_00:  Você colocou
SPEAKER_01:  Uma pergunta
SPEAKER_01:  Onde está hospedado
SPEAKER_01:  A gente
SPEAKER_01:  Fez um convênio
SPEAKER_01:  Com uma nuvem
SPEAKER_01:  Com uma empresa
SPEAKER_01:  Mesmo
SPEAKER_01:  A gente tinha um aluno
SPEAKER_01:  Que estava
SPEAKER_01:  Fazendo estágio lá
SPEAKER_01:  E ele
SPEAKER_01:  Estava no projeto
SPEAKER_01:  Ele que desenvolveu
SPEAKER_01:  O editor de equações
SPEAKER_01:  E aí
SPEAKER_01:  Ele fez o sapão
SPEAKER_01:  Com a empresa
SPEAKER_01:  A gente tentou
SPEAKER_01:  Um convênio
SPEAKER_01:  Tentamos por um bom tempo
SPEAKER_01:  Assim
SPEAKER_01:  Resolver a burocracia
SPEAKER_01:  E depois
SPEAKER_01:  A empresa
SPEAKER_01:  Ela
SPEAKER_01:  Ela fez um convênio
SPEAKER_01:  Com fatura zerada
SPEAKER_01:  Para a gente
SPEAKER_01:  Então a gente
SPEAKER_01:  Então a gente está
SPEAKER_01:  Nesse convênio
SPEAKER_01:  Ainda
SPEAKER_01:  É de quanto tempo
SPEAKER_01:  Mais ou menos
SPEAKER_00:  A sua hospedagem
SPEAKER_00:  E tem
SPEAKER_00:  Ah
SPEAKER_00:  Eles não estipularam
SPEAKER_01:  Não estipularam
SPEAKER_01:  Prazo
SPEAKER_01:  Então por enquanto
SPEAKER_01:  A gente está
SPEAKER_01:  E vocês tem
SPEAKER_01:  Tipo
SPEAKER_00:  É porque
SPEAKER_00:  Quando você tem
SPEAKER_00:  Esse tipo de hospedagem
SPEAKER_00:  É interessante
SPEAKER_00:  Você ter os dados
SPEAKER_00:  De tipo
SPEAKER_00:  Quanto que você pode
SPEAKER_00:  Armazenar
SPEAKER_00:  De
SPEAKER_00:  Eu não sei se isso
SPEAKER_00:  Incluir banco de dados
SPEAKER_00:  Ou vocês estão usando
SPEAKER_00:  Outra
SPEAKER_00:  Outro serviço
SPEAKER_00:  Mas no caso
SPEAKER_00:  De seu mesmo
SPEAKER_00:  Ou de não seu mesmo
SPEAKER_00:  Também
SPEAKER_00:  Quais são os limites
SPEAKER_00:  Dessa
SPEAKER_00:  Dessa
SPEAKER_00:  Dessa
SPEAKER_00:  Dessa
SPEAKER_00:  Dessa
SPEAKER_00:  Dessa
SPEAKER_00:  Dessa
SPEAKER_00:  Dessa
SPEAKER_00:  Dessa
SPEAKER_00:  Dessa
SPEAKER_00:  Dessa
SPEAKER_00:  Dessa
SPEAKER_00:  Dessa
SPEAKER_01:  Dessa
SPEAKER_01:  Dessa
SPEAKER_01:  Dessa
SPEAKER_01:  Eu vou te mandar
SPEAKER_00:  Eu vou te mandar
SPEAKER_01:  O link
SPEAKER_01:  E vou dizer
SPEAKER_01:  Mais ou menos
SPEAKER_01:  Qual que é o plano
SPEAKER_01:  Que a gente tem
SPEAKER_01:  Tá bom
SPEAKER_01:  Aí você
SPEAKER_01:  Consegue dar uma olhadinha
SPEAKER_01:  Porque eu não estou
SPEAKER_01:  Lembrando agora
SPEAKER_01:  De cabeça
SPEAKER_01:  Mas assim
SPEAKER_01:  Tem nos atendido bem
SPEAKER_01:  Não teve
SPEAKER_01:  Eu acho que
SPEAKER_01:  Nenhum problema
SPEAKER_01:  De
SPEAKER_01:  Não teve nenhum problema
SPEAKER_01:  Assim
SPEAKER_01:  Eu acho que
SPEAKER_01:  Em algum período
SPEAKER_01:  Oscilou
SPEAKER_01:  Acho que
SPEAKER_01:  Os alunos
SPEAKER_01:  Que estavam desenvolvendo
SPEAKER_01:  Comentaram alguma coisa
SPEAKER_01:  Mas assim
SPEAKER_01:  Muito pouco
SPEAKER_01:  Acho que teve
SPEAKER_01:  Em algum momento
SPEAKER_01:  Que caiu o servidor
SPEAKER_01:  Mas assim
SPEAKER_01:  Logo
SPEAKER_01:  Voltou
SPEAKER_01:  Bem
SPEAKER_01:  Bem tranquilo
SPEAKER_01:  Aí a gente tinha
SPEAKER_01:  Muito mais problema
SPEAKER_01:  Quando estava no campus
SPEAKER_01:  Que caiu o servidor
SPEAKER_01:  E a gente precisava
SPEAKER_01:  Às vezes
SPEAKER_01:  Precisava
SPEAKER_01:  Avisá-los
SPEAKER_01:  E pedir para retomar
SPEAKER_01:  E lá
SPEAKER_01:  A gente tinha
SPEAKER_01:  Um problema
SPEAKER_01:  Da questão
SPEAKER_01:  Segurança também
SPEAKER_01:  Que era a segurança
SPEAKER_01:  Do campus
SPEAKER_01:  Não só
SPEAKER_01:  Só da página
SPEAKER_01:  Mas enfim
SPEAKER_01:  Acho que agora
SPEAKER_01:  Está mais
SPEAKER_01:  Mais estável
SPEAKER_01:  Mas eu consigo
SPEAKER_01:  Te mandar
SPEAKER_01:  Essas informações
SPEAKER_01:  Para você dar uma olhada
SPEAKER_01:  Tá bom?
SPEAKER_01:  Uhum
SPEAKER_00:  Eu acho que pode parar a gravação
SPEAKER_00:  E mandar para ele
SPEAKER_01:  Tá bom?
SPEAKER_01:  Tá
SPEAKER_01:  Eu
SPEAKER_00:  Mando por onde?
SPEAKER_00:  É que
SPEAKER_00:  Tchau
SPEAKER_00:  Tchau
SPEAKER_00:  Tchau
'''
from modules.ArcanaFlow import Nayahath

Nayahath.add_entity("Summarizer", "yellow")

Nayahath.action("Summarizer", "Initializing Summarization")

om = OutputManager('./teste_ollama')
om.create_timestamped_folder("TESTE_OLLAMA")

qwen = SummarizerQwen3(model="llama3")
    
res = qwen.summarize(text)

om.save_text_file("OUTPUT", res)

# SPEAKERS_LIST = ["SPEAKER_00", "SPEAKER_01", "SPEAKER_02", "SPEAKER_03"]
# counter = 0
# for s in SPEAKERS_LIST:
#     question = qwen.questionToSpeaker(s, context=textABC)
#     om.save_text_file(f"{s}_question", question)
#     counter += 1
#     Nayahath.action("Summarizer", f"Pergunta concluída {counter}/{len(SPEAKERS_LIST)}")