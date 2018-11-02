# Trabalho final para Linguagens Formais

Esse é o relatório com a descrição sobre a linguagem formal criada para o trabalho final da matéria Linguages Formais e Autômatos Finitos - INF05005, do Instituto de Informática, UFRGS, ministrada pelo professor Lucio Mauro Duarte.

Integrantes do grupo:
* Augusto Zanella Bardini
* Lorenzo Cernicchiaro
* Rafael Baldasso Audibert

O trabalho também poderá ser encontrado no [Github](https://github.com/rafaeelaudibert/Formais)


# Descrição da Linguagem Whatsapp (3.2)

Para construção dessa linguagem nos baseamos no aplicativo [Whatsapp](https://www.whatsapp.com/) na sua versão para Android, que pode ser encontrada [aqui](https://play.google.com/store/apps/details?id=com.whatsapp).

Temos como alfabeto da linguagem, os seguintes símbolos, seguidos da representação que terão quando representados como transições no AFN:

* *AbrirCamera* -> **a**
* *AbrirCameraConversa* -> **b**
* *AbrirCameraStatus* -> **c**
* *AbrirChamadas* -> **d**
* *AbrirConversa* -> **e**
* *AbrirInfo* -> **f**
* *AbrirMidias* -> **g**
* *AbrirStatus* -> **h**
* *AdicionarStatus* -> **i**
* *AvancarStatus* -> **j**
* *EncerrarChamada* -> **k**
* *EnviarAudio* -> **l**
* *EnviarContato* -> **m**
* *EnviarLocalizacao* -> **n**
* *EnviarMensagem* -> **o**
* *EnviarMidia* -> **p**
* *EnviarSticker* -> **q**
* *LigarAlguem* -> **r**
* *RetrocederStatus* -> **s**
* *TirarFoto* -> **t**
* *VisualizarProprioStatus* -> **u**
* *VisualizarStatus* -> **v**
* *Voltar* -> **w**
As transições possíveis para essa gramática podem ser vistas no autômato disponibilizado no item *AFN(3.4)* abaixo.

# AFN (3.4)
O autômato capaz de reconhecer a linguagem mostrada acima, criado no JFLAP se encontra no arquivo *automato.jff* localizado na mesma pasta que esse arquivo se encontra.
Também foi gerado o autômato finito determinístico pelo JFLAP, que se encontra no arquivo *automatoDeterministico.jff*.

# Lista de Palavras a serem reconhecidas (3.3)
No arquivo *input.txt* que está na mesma pasta que essa, estão 10 palavras a serem reconhecidas por essa linguagem, sendo que as 5 primeiras são aceitas, e as outras 5 não são. Os motivos para as 5 últimas não serem aceitas, são, em ordem a partir da 5ª:
* *f,g,w,w*
    * **Indeterminação**, não tenho a transição *f* no estado inicial
* *r,k*
	* **Indeterminação**, não tenho a transição *r* no estado inicial
* *h,j,j,s,w,a,w*
	 * **Indeterminação**, não tenho a transição *j* após ter realizado a transição *h*. Precisaria ter feito a transição *u* ou *v* 
* *a,t,p*
	* **Não alcança estado final**, o jeito mais fácil de alcançar o estado final seria adicionar a transição *w* ao final da palavra acima. 
* *e,p,o,w,d,r,k*
	* **Não alcança estado final**, novamente o jeito mais fácil de alcançar o estado final seria adicionar a transição *w* ao final da palavra acima. 


# AFN formatado (3.5)
O AFN capaz de reconhecer a linguagem descrita acima, formatado de acordo com a especificação do trabalho se encontra no arquivo *whatsapp.txt* localizado na mesma pasta que esse arquivo se encontra.