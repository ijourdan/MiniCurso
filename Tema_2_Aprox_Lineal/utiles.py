import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TABLEAU_COLORS

def corpus_generator(quant_tag = 4, quant_data = 1000, dimension = 2, test_proportion = 0.2, gap=4):
    """

    :param quant_tag: 4 cantidad de etiquetas
    :param quant_data: 1000 cantidad de datos del corpus
    :param dimension: 2 dimensiones del problema
    :param gap: 4 separación entre clusters
    :param test_proportion:
    :return: training, training_tags, test, test_tags
    """

    centers = np.random.randn(quant_tag,dimension)*gap
    data = np.random.randn(quant_data,dimension)
    data_tags = np.random.randint(low=0, high=quant_tag, size=(quant_data,))

    for i in range(quant_data):
        data[i,:] += centers[data_tags[i].item(),:]

    limit_index_for_test = np.floor((1-test_proportion)*quant_data).astype('int')
    training = data[:limit_index_for_test,:]
    training_tags = data_tags[:limit_index_for_test]
    test = data[limit_index_for_test:,:]
    test_tags = data_tags[limit_index_for_test:]

    return training, training_tags, test, test_tags

def sec_experimental(N=1000):
    """
    Genera una secuencia senoidal y = sin(x)
    donde x es Unif[0, 4pi)
    """
    
    x = 4 * np.pi * np.random.rand(N)
    y = np.sin(x) + np.random.randn(N)*4
    return y,x

def plt_data_2d(data,data_tags):
    keys = list(TABLEAU_COLORS.keys())
    fig = plt.figure(figsize=(6,6))
    for i in range(data_tags.max().item()+1):
        index = data_tags == i
        plt.plot(data[index,0],data[index,1], '*' ,color=TABLEAU_COLORS[keys[i]])
    plt.show()

