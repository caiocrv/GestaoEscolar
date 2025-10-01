#include <stdio.h>

__declspec(dllexport) float media(float notas[], int tamanho){
    if (tamanho <= 0) {
        return 0.0f;
    }

    float soma = 0;
    for(int i = 0; i < tamanho; i++){
        soma += notas[i];
    }

    return soma / tamanho;
}