# Classificacao-Reconhecimento-de-Imagens

ítulo
Classificação de Imagem do banco de dados CIFAR-10

Equipe
Denis Rodrigues Rocha

Dataset
CIFAR-10 (https://www.cs.toronto.edu/~kriz/cifar.html)

Descrição do projeto
O código apresentado realiza classificação/reconhecimento de imagens usando o conjunto de dados CIFAR-10. Vamos analisar as etapas do código:

Importação das bibliotecas: O código importa as bibliotecas necessárias, incluindo TensorFlow, Keras e Matplotlib.

Carregamento do conjunto de dados CIFAR-10: O código usa a função datasets.cifar10.load_data() para baixar e carregar o conjunto de dados CIFAR-10. O conjunto de treinamento é armazenado nas variáveis train_images e train_labels, enquanto o conjunto de teste é armazenado nas variáveis test_images e test_labels.

Normalização dos valores dos pixels: Os valores dos pixels nas imagens são normalizados dividindo-os por 255.0, o que garante que eles estejam no intervalo de 0 a 1.

Construção do modelo de convolução: O modelo é construído usando a classe Sequential do Keras. É adicionada uma camada de convolução com 32 filtros, uma função de ativação "relu" e uma forma de entrada de (32, 32, 3) para imagens de entrada de tamanho 32x32 e 3 canais de cor (RGB). Em seguida, é adicionada uma camada de pooling máxima para reduzir a dimensionalidade espacial. Esse padrão é repetido com mais uma camada de convolução e pooling. Finalmente, é adicionada uma camada de convolução adicional sem pooling.

Adição de camadas densas: Após as camadas de convolução, é adicionada uma camada Flatten para achatar a saída e transformá-la em um vetor unidimensional. Em seguida, são adicionadas duas camadas densas com ativação "relu". A última camada densa possui 10 unidades, correspondendo ao número de classes no conjunto de dados CIFAR-10.

Compilação e treinamento do modelo: O modelo é compilado usando o otimizador "adam" e a função de perda SparseCategoricalCrossentropy. A métrica de avaliação usada é a acurácia. Em seguida, o modelo é treinado usando os dados de treinamento (train_images e train_labels) por 10 épocas, com validação sendo realizada em cada época usando os dados de teste (test_images e test_labels).

O histórico de treinamento é armazenado na variável history para posterior análise ou visualização dos resultados.

Repositório do projeto
