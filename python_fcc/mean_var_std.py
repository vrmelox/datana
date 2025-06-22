import numpy as np

def calculate(elem):
    if len(elem) != 9:
        raise ValueError("List must contain nine numbers.")
    fun_np_array = np.array(elem).reshape(3, 3)
    calcul_dict = {}
    calcul_dict['mean'] = list([np.mean(fun_np_array, axis=0), np.mean(fun_np_array, axis=1), (np.mean(fun_np_array))])
    calcul_dict['variance'] = list([np.var(fun_np_array, axis=0), np.var(fun_np_array, axis=1), (np.var(fun_np_array))])
    calcul_dict['standard deviation'] = list([np.std(fun_np_array, axis=0), np.std(fun_np_array, axis=1), (np.std(fun_np_array))])
    calcul_dict['max'] = list([np.max(fun_np_array, axis=0), np.max(fun_np_array, axis=1), (np.max(fun_np_array))])
    calcul_dict['min'] = list([np.min(fun_np_array, axis=0), np.min(fun_np_array, axis=1), (np.min(fun_np_array))])
    calcul_dict['sum'] = list([np.sum(fun_np_array, axis=0), np.sum(fun_np_array, axis=1), (np.sum(fun_np_array))])
    return calcul_dict

