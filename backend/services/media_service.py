import ctypes

# Carregar DLL
lib = ctypes.CDLL("./build/media.dll")

# Informando como a funcao em C foi declarada
lib.media.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]
lib.media.restype = ctypes.c_float

def calcular_media(notas):
    tamanho = len(notas)
    arr = (ctypes.c_float * tamanho)(*notas)
    return lib.media(arr, tamanho)