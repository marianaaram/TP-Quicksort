import random
import time
import sys

sys.setrecursionlimit(2000)

class QuicksortRecursivo:
    # Implementação comum do QuickSort
    
    def sort(self, array):
        self._quicksort(array, 0, len(array) - 1)
        
    def _quicksort(self, array, low, high):
        if low < high:
            # Encontra o pivô de tal forma que os elementos menores
            # ficam à sua esquerda e os maiores à sua direita.
            pivot = self._partition(array, low, high)
            
            # Ordena recursivamente as duas listas (metade menor e metade maior)
            self._quicksort(array, low, pivot - 1)
            self._quicksort(array, pivot + 1, high)
            
    def _partition(self, array, low, high):
        # Reparte a lista da recursão atual escolhendo o último elemento como o pivô
        pivot = array[high]
        i = low - 1
        
        # Percorre a lista e move os elementos menores que o pivô para a esquerda
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        
        # Coloca o pivô para sua posição correta.
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1
    
class QuicksortHibrido:
    # Implementação da versão híbrida do Quicksort.
    # Para sub-vetores pequenos, utiliza o Insertion Sort em vez de
    # continuar a recursão, otimizando a performance.
    
    def __init__(self, M):
        # M é o limite para troca de algoritmo
        if M < 1:
            raise ValueError("M deve ser um valor positivo")
        
        self.M = M
    
    def sort(self, array):
        # Processo de ordenação
        self._quicksort(array, 0, len(array) - 1)
        
    def _insertion_sort(self, array, low, high):
        # Algoritmo de Insertion Sort para as pequenas sub-listas
        for i in range(low + 1, high + 1):
            key = array[i]
            j = i - 1
            
            while j >= low and array[j] > key:
                array[j + 1] = array[j]
                j -= 1
            
            array[j + 1] = key
    
    def _quicksort(self, array, low, high):
        if low < high:
            # Se o tamanho da sub-lista for menor que M, usa o insertion sort
            if (high - low + 1) < self.M:
                self._insertion_sort(array, low, high)
            else:
                pivot = self._partition(array, low, high)
                self._quicksort(array, low, pivot - 1)
                self._quicksort(array, pivot + 1, high)
    
    def _partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

class QuickSortHibridoMedianaDeTres:
    # Versão melhorada do Quicksort Híbrido.
    # Utiliza a técnica da "Mediana de Três" para escolher um pivô mais eficaz,
    # reduzindo a chance de pegar o pior caso (lista já ordenada).
    
    def __init__(self, M):
        if M < 1:
            raise ValueError("M deve ser um valor positivo")
        
        self.M = M
    
    def sort(self, array):
        self._quicksort(array, 0, len(array) - 1)
    
    def _insertion_sort(self, array, low, high):
        # Algoritmo de Insertion Sort para as pequenas sub-listas
        for i in range(low + 1, high + 1):
            key = array[i]
            j = i - 1
            
            while j >= low and array[j] > key:
                array[j + 1] = array[j]
                j -= 1
            
            array[j + 1] = key
            
    def _quicksort(self, array, low, high):
        if low < high:
            # Se o tamanho da sub-lista for menor que M, usa o insertion sort
            if (high - low + 1) < self.M:
                self._insertion_sort(array, low, high)
            else:
                pivot = self._partition(array, low, high)
                self._quicksort(array, low, pivot - 1)
                self._quicksort(array, pivot + 1, high)
                
    def _mediana(self, array, low, high):
        # Calcula a mediana entre o primeiro, o meio e o último elemento
        # e a coloca na penúltima posição para ser usada como pivô
        mid = (low + high) // 2
        
        if array[low] > array[mid]:
            array[low], array[mid] = array[mid], array[low]
        
        if array[low] > array[high]:
            array[low], array[high] = array[high], array[low]
            
        if array[mid] > array[high]:
            array[mid], array[high] = array[high], array[mid]
            
        # O pivô (mediana) é movido para a posição 'high'
        array[mid], array[high] = array[high], array[mid]
        return array[high]
    
    def _partition(self, array, low, high):
        # Particiona a lista usando o pivô obtido da mediana de três
        pivot = self._mediana(array, low, high)
        i = low -1
        
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1
    

def rodar_testes(nome_teste, vetor_original, sorter_a, sorter_b, sorter_c):
    # Executa ordenações com os 3 algoritmos para um dado vetor e mede o tempo 
    print(f"\n --- TESTE ATUAL: {nome_teste} ---")
    
    # cópias do vetor para garantir ordenação da mesma lista
    vetor_a = vetor_original.copy()
    vetor_b = vetor_original.copy()
    vetor_c = vetor_original.copy()
    
    # Quicksort Recursivo
    inicio_a = time.perf_counter()
    sorter_a.sort(vetor_a)
    fim_a = time.perf_counter()
    print(f"Tempo Quicksort Recursivo: {fim_a - inicio_a:.6f}s")
    
    # Quicksort Hibrido
    inicio_b = time.perf_counter()
    sorter_b.sort(vetor_b)
    fim_b = time.perf_counter()
    print(f"Tempo Quicksort Recursivo: {fim_b - inicio_b:.6f}s")
    
    # Quicksort Hibrido com Mediana de Três
    inicio_c = time.perf_counter()
    sorter_c.sort(vetor_c)
    fim_c = time.perf_counter()
    print(f"Tempo Quicksort Recursivo: {fim_c - inicio_c:.6f}s")
    
    # ordeno o vetor usando uma função padrão no Python para validar se 
    # os testes foram ordenados corretamente
    vetor_validador = sorted(vetor_original)
    assert vetor_a == vetor_validador
    assert vetor_b == vetor_validador
    assert vetor_c == vetor_validador
    print("Todos os vetores foram ordenados corretamente.")

def main():
    TAMANHO_VETOR = 1000
    NUM_TESTS = 10
    
    # ! Parte 1: Determinar o melhor valor de M para o Quicksort Híbrido
    
    print(f"Determinando o melhor valor de M para vetores de {TAMANHO_VETOR} elementos\n")
    melhor_m = -1
    melhor_tempo = float('inf')
    
    # Testaremos com valores de M de 5 a 50
    for m_candidato in range(5, 51):
        # medir o tempo de cada um
        tempo_total = 0
        
        for _ in range(NUM_TESTS):
            # inicializa o vetor de teste com numeros inteiros randomicos
            vetor_teste = [random.randint(0, TAMANHO_VETOR * 10) for _ in range(TAMANHO_VETOR)]
            sort_hibrido = QuicksortHibrido(M=m_candidato)
            
            inicio = time.perf_counter()
            sort_hibrido.sort(vetor_teste)
            fim = time.perf_counter()
            
            tempo_total += (fim - inicio)
            
        tempo_medio = tempo_total / NUM_TESTS
        # ! Tire esse print caso queira ver o tempo médio de cada M
        # print(f"Com M = {m_candidato}: Tempo médio = {tempo_medio:.6f}s")
        
        # dados comparativos
        if tempo_medio < melhor_tempo:
            melhor_tempo = tempo_medio
            melhor_m = m_candidato
            
    print(f"O melhor valor de M encontrado foi: {melhor_m}\n")
    
    # ! Parte 2: Comparar as implementações com diferentes massas de testes
    
    # instanciando os algoritmos
    sorter_a = QuicksortRecursivo()
    sorter_b = QuicksortHibrido(M=melhor_m)
    sorter_c = QuickSortHibridoMedianaDeTres(M=melhor_m)
    
    # Teste 1: Vetor com elementos aleatórios (caso médio)
    vetor_randomico = [random.randint(0, TAMANHO_VETOR * 10) for _ in range(TAMANHO_VETOR)]
    rodar_testes("Vetor Aleatório (Caso Médio)", vetor_randomico, sorter_a, sorter_b, sorter_c)
    
    # Teste 2: Vetor já ordenado (pior caso para o Quicksort com pivô na ponta)
    vetor_ordenado = list(range(TAMANHO_VETOR))
    rodar_testes("Vetor Ordenado (Pior caso para 'a' e 'b')", vetor_ordenado, sorter_a, sorter_b, sorter_c)
    
    # Teste 3: Vetor ordenado de forma inversa (outro pior caso)
    vetor_inverso = list(range(TAMANHO_VETOR - 1, -1, -1))
    rodar_testes("Vetor Ordenado Inversamente (Pior caso para 'a' e 'b')", vetor_inverso, sorter_a, sorter_b, sorter_c)
    
    # Teste 4: Vetor com muitos elementos repetidos
    repeticao = int(TAMANHO_VETOR * 0.1)
    vetor_repetido = [random.randint(0, repeticao) for _ in range(TAMANHO_VETOR)]
    rodar_testes("Vetor com Elementos Repetidos", vetor_repetido, sorter_a, sorter_b, sorter_c)

if __name__ == "__main__":
    main()