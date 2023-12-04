# Projeto-Redes1
Projeto final da disciplina de redes 1, curso de cic, 2023.1

## Protocolo da Camada de Aplicação
### 1. Visão Geral:
O protocolo da camada de aplicação permite a comunicação entre um cliente e um servidor para realizar um leilão de itens. O protocolo envolve trocas de mensagens e segue uma sequência de eventos para manter o software funcionando corretamente.
### 2. Participantes:
* **Cliente:** *A parte que pode solicitar a lista de itens disponíveis e fazer lances.*
* **Servidor:** *A parte que recebe as solicitações do cliente, processa os lances e mantém o controle dos itens em leilão.*
### 3. Mensagens:
* **Solicitação de Lista de Itens:**
   - **Cliente -> Servidor:** *Pedido para listar os itens disponíveis.*
* **Envio de Lance:**
    - **Cliente -> Servidor:** *Envia um lance com o nome do cliente, o ID do item e o valor do lance.*
* **Resposta ao Cliente:**
    - **Servidor -> Cliente:** *Confirmação de lance bem-sucedido ou falha.*
    - **Servidor -> Cliente:** *Lista de itens disponíveis com seus IDs e valores atuais.*
    - **Servidor -> Cliente:** *Maior lance realizado em cada item ao encerrar o leilão.*
### 4. Eventos e Estados:
* **Cliente:**
   - **Estado Inicial:** *Aguardando a escolha de uma opção (listar itens ou fazer um lance).*
   - **Evento:** *Cliente escolhe listar itens ou fazer um lance.*
   - **Estado Final:** *Aguardando resposta do servidor ou aguardando entrada para um novo lance.*
* **Servidor:**
   - **Estado Inicial:** *Esperando a conexão de um cliente.*
   - **Evento:** *Recebe uma conexão do cliente.*
   - **Estado Final:** *Processando solicitação do cliente ou aguardando nova conexão.*
### 5. Fluxo de Comunicação:
* **Cliente:** *Envia solicitação para listar itens ou faz um lance.*
*  **Servidor:** *Recebe a solicitação do cliente e processa, atualizando a lista de itens ou o maior lance, conforme necessário.*
*  **Servidor:** *Responde ao cliente com a confirmação do lance, a lista atualizada de itens ou os maiores lances realizados.*
*  **Cliente:** *Recebe a resposta do servidor e pode optar por fazer novas solicitações ou encerrar a conexão.*
### 6. Considerações:
* O protocolo é baseado em um modelo de requisição-resposta, onde o cliente envia solicitações específicas e o servidor responde de acordo.
* A comunicação é estabelecida por meio de sockets TCP/IP para garantir a confiabilidade e a ordem das mensagens.
* O servidor mantém o controle dos itens em leilão e registra os maiores lances em cada item.

## Funcionamento do Software
### 1. Propósito do Software:
O software tem como propósito coordenar um leilão, permitindo que clientes solicitem informações sobre itens disponíveis e façam lances nesses itens.
### 2. Motivação da escolha do protocolo de transporte:
O TCP (Transmission Control Protocol) foi escolhido para garantir uma comunicação confiável e ordenada entre o cliente e o servidor. Ele oferece garantias de entrega de mensagens e controle de fluxo, essenciais para um leilão.
### 3. Requisitos Mínimos de Funcionamento:
**a) Conectividade de Rede:** O cliente e o servidor devem estar em redes que permitam a comunicação entre eles, como redes locais.
**b) Portas de Comunicação:** O servidor deve estar configurado para ouvir em uma porta específica.
**c) Protocolo TCP:** Ambos, cliente e servidor, devem suportar o protocolo TCP.
**d) Entrada Válida:** O software deve lidar com entradas válidas e inválidas dos clientes ao fazer lances.
