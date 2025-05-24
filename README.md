# Teste Kmeans

O objetivo deste repositório é testar o algoritmo K-Means em diferentes
conjuntos de dados específicos, avaliando sua capacidade de identificar
corretamente os grupos presentes em cada um deles.

## Como rodar o código

### Cria um ambiente virtual chamado ".venv"
```sh
python -m venv .venv
```

### Ativa o ambiente virtual
```sh
source .venv/bin/activate
```

### Instala todas as dependências listadas no arquivo requirements.txt
```sh
pip install -r requirements.txt
```

### Roda o código
```sh
python k-means.py <arquivo.csv> <seed> <n_init>
```

- `<arquivo.csv>`: Caminho para o arquivo CSV com os dados
- `<seed>`: Valor da seed aleatória para o algoritmo K-Means
- `<n_init>`: Número de inicializações diferentes do K-Means

# Testes Realizados

## Primeiro Teste

O primeiro teste foi realizado com o conjunto de dados presente no arquivo `dados.csv`.

![Dados1](https://github.com/kenjiThiago/Teste_Kmeans/blob/main/imagens/dados.png)

### Resultados

![Teste1](https://github.com/kenjiThiago/Teste_Kmeans/blob/main/imagens/dados_resultado.png)

`media_geral_silhouette`: 0.7527

O algoritmo K-Means conseguiu identificar os grupos com relativa facilidade,
separando bem os padrões presentes nos dados.  A visualização dos clusters
revelou uma boa correspondência com as classes reais.

## Segundo Teste

O segundo teste foi realizado com o conjunto de dados presente no arquivo `dados2.csv`

![Dados2](https://github.com/kenjiThiago/Teste_Kmeans/blob/main/imagens/dados2.png)

### Resultados

![Teste2](https://github.com/kenjiThiago/Teste_Kmeans/blob/main/imagens/dados2_resultado.png)

`media_geral_silhouette`: 0.5755

O algoritmo K-Means conseguiu identificar os grupos presentes nos dados, embora
tenha apresentado certa dificuldade em separar claramente todos os padrões.
Ainda assim, a visualização dos clusters mostrou uma correspondência razoável
com as classes reais, indicando um desempenho aceitável nesse segundo teste.

## Fontes

Os dados utilizados foram obtidos a partir do [Clustering basic benchmark](http://cs.joensuu.fi/sipu/datasets/)
