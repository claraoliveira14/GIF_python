# GIF_python
## Projeto gerador de GIF em python
Esse é um script simples, em python, que automatiza a criação de GIF a partir de uma lista de imagens estáticas.
## Como funciona
* **Importação:** O script utiliza a biblioteca imageio para processar os arquivos e gerar as animações.Utilizei o imageio.v3 para interface moderna de leitura e escrita de imagens
* **Lista de Arquivos:** Criei uma lista (filenames) com o nome das minhas imagens escolhidas
* **Processamento:** Criei uma lista vazia chamada imagens, utilizei o for para percorrer cada arquivo e o imread() para transformar cada uma das imagens em matrizes de dados
* **Exportação:** A função imwrite() junta todas as matrizes, define a duração de cada frame e cria o arquivo final
## Pré-requisitos
Para rodar esse programa você precisará do python instalado e da biblioteca imageio
