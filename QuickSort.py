import random
import time
import sys

sys.setrecursionlimit(2000)

class QuicksortRecursivo:
    def __init__(self):
        # Inicializa os contadores de métricas de desempenho para o algoritmo.
        self.comparisons = 0
        self.swaps = 0

    def reset_counters(self):
        # Zera os contadores para permitir uma nova execução de teste limpa.
        self.comparisons = 0
        self.swaps = 0
    
    def sort(self, array):
        self._quicksort(array, 0, len(array) - 1)
        
    def _quicksort(self, array, low, high):
        # A verificação 'if low < high' é uma comparação fundamental da lógica do Quicksort.
        self.comparisons += 1
        if low < high:
            pivot = self._partition(array, low, high)
            self._quicksort(array, low, pivot - 1)
            self._quicksort(array, pivot + 1, high)
            
    def _partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        
        for j in range(low, high):
            # Conta a comparação de cada elemento com o pivô.
            self.comparisons += 1
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                # Conta a troca de posição entre elementos.
                self.swaps += 1
        
        array[i + 1], array[high] = array[high], array[i + 1]
        # Conta a troca final que coloca o pivô em sua posição correta.
        self.swaps += 1
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
        # Inicializa os contadores de métricas de desempenho para o algoritmo
        self.comparisons = 0
        self.swaps = 0

    def reset_counters(self):
        # Zera os contadores para permitir uma nova execução de teste limpa
        self.comparisons = 0
        self.swaps = 0
    
    def sort(self, array):
        # Processo de ordenação
        self._quicksort(array, 0, len(array) - 1)
        
    def _insertion_sort(self, array, low, high):
        # Algoritmo de Insertion Sort para as pequenas sub-listas
        for i in range(low + 1, high + 1):
            key = array[i]
            j = i - 1
            
            # Conta a primeira comparação do 'while' para cada elemento.
            self.comparisons += 1
            while j >= low and array[j] > key:
                # Conta as comparações subsequentes dentro do 'while'.
                self.comparisons += 1
                array[j + 1] = array[j]
                # Movimentar um elemento é análogo a uma troca de valores.
                self.swaps += 1
                j -= 1
            
            array[j + 1] = key
    
    def _quicksort(self, array, low, high):
        self.comparisons += 1 # Verificação 'if low < high'
        if low < high:
            # Compara o tamanho do sub-vetor com o limiar M.
            self.comparisons += 1
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
            # Conta a comparação de cada elemento com o pivô.
            self.comparisons += 1
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                self.swaps += 1
                
        array[i + 1], array[high] = array[high], array[i + 1]
        self.swaps += 1
        return i + 1

class QuickSortHibridoMedianaDeTres:
    # Versão melhorada do Quicksort Híbrido.
    # Utiliza a técnica da "Mediana de Três" para escolher um pivô mais eficaz,
    # reduzindo a chance de pegar o pior caso (lista já ordenada)
    
    def __init__(self, M):
        if M < 1:
            raise ValueError("M deve ser um valor positivo")
        
        self.M = M
        # Inicializa os contadores de métricas de desempenho para o algoritmo.
        self.comparisons = 0
        self.swaps = 0

    def reset_counters(self):
        # Zera os contadores para permitir uma nova execução de teste limpa.
        self.comparisons = 0
        self.swaps = 0
    
    def sort(self, array):
        self._quicksort(array, 0, len(array) - 1)
    
    def _insertion_sort(self, array, low, high):
        # Algoritmo de Insertion Sort para as pequenas sub-listas
        for i in range(low + 1, high + 1):
            key = array[i]
            j = i - 1
            
            self.comparisons += 1 # Primeira comparação do 'while'
            while j >= low and array[j] > key:
                self.comparisons += 1 # Comparações subsequentes
                array[j + 1] = array[j]
                self.swaps += 1
                j -= 1
            
            array[j + 1] = key
            
    def _quicksort(self, array, low, high):
        self.comparisons += 1 # Verificação 'if low < high'
        if low < high:
            self.comparisons += 1 # Verificação do tamanho vs M
            if (high - low + 1) < self.M:
                self._insertion_sort(array, low, high)
            else:
                pivot = self._partition(array, low, high)
                self._quicksort(array, low, pivot - 1)
                self._quicksort(array, pivot + 1, high)
                
    def _mediana(self, array, low, high):
        mid = (low + high) // 2
        
        # Cada 'if' representa uma comparação para encontrar a mediana.
        self.comparisons += 1
        if array[low] > array[mid]:
            array[low], array[mid] = array[mid], array[low]
            self.swaps += 1
        
        self.comparisons += 1
        if array[low] > array[high]:
            array[low], array[high] = array[high], array[low]
            self.swaps += 1
            
        self.comparisons += 1
        if array[mid] > array[high]:
            array[mid], array[high] = array[high], array[mid]
            self.swaps += 1
            
        # Move a mediana para a posição do pivô.
        array[mid], array[high] = array[high], array[mid]
        self.swaps += 1
        return array[high]
    
    def _partition(self, array, low, high):
        pivot = self._mediana(array, low, high)
        i = low -1
        
        for j in range(low, high):
            self.comparisons += 1
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                self.swaps += 1
        
        array[i + 1], array[high] = array[high], array[i + 1]
        self.swaps += 1
        return i + 1

def main():
    TAMANHO_VETOR = 1000
    NUM_TESTS_M = 10
    # Define o número de execuções para cada cenário de teste para calcular a média
    NUM_EXECUCOES_FINAL = 10
    
    # ! Parte 1: Determinar o melhor valor de M para o Quicksort Híbrido
    
    print(f"Determinando o melhor valor de M para vetores de {TAMANHO_VETOR} elementos\n")
    melhor_m = -1
    melhor_tempo = float('inf')
    
    for m_candidato in range(5, 51, 5):
        tempo_total = 0
        for _ in range(NUM_TESTS_M):
            vetor_teste = [random.randint(0, TAMANHO_VETOR * 10) for _ in range(TAMANHO_VETOR)]
            sort_hibrido = QuicksortHibrido(M=m_candidato)
            
            inicio = time.perf_counter()
            sort_hibrido.sort(vetor_teste)
            fim = time.perf_counter()
            
            tempo_total += (fim - inicio)
            
        tempo_medio = tempo_total / NUM_TESTS_M
        if tempo_medio < melhor_tempo:
            melhor_tempo = tempo_medio
            melhor_m = m_candidato
            
    print(f"O melhor valor de M encontrado foi: {melhor_m}\n")
    
    # ! Parte 2: Comparar as implementações com diferentes massas de testes
    
    print(f"--- Iniciando comparação final com {NUM_EXECUCOES_FINAL} execuções por teste ---")

    # Estrutura para definir os diferentes cenários de teste a serem executados.
    testes = [
        {"nome": "Vetor Aleatório (Caso Médio)", "gerador": lambda: [random.randint(0, TAMANHO_VETOR * 10) for _ in range(TAMANHO_VETOR)]},
        {"nome": "Vetor Ordenado (Pior Caso para 'a' e 'b')", "gerador": lambda: list(range(TAMANHO_VETOR))},
        {"nome": "Vetor Ordenado Inversamente (Pior Caso para 'a' e 'b')", "gerador": lambda: list(range(TAMANHO_VETOR - 1, -1, -1))},
        {"nome": "Vetor com Elementos Repetidos", "gerador": lambda: [random.randint(0, int(TAMANHO_VETOR * 0.1)) for _ in range(TAMANHO_VETOR)]}
    ]

    sorter_a = QuicksortRecursivo()
    sorter_b = QuicksortHibrido(M=melhor_m)
    sorter_c = QuickSortHibridoMedianaDeTres(M=melhor_m)
    sorters = [sorter_a, sorter_b, sorter_c]

    # ! Rodada de testes com cada um dos casos no vetor de objetos 'testes'
    for teste in testes:
        print(f"\n--- TESTE ATUAL: {teste['nome']} ---")

        # Acumuladores para calcular as médias de tempo, comparações e trocas.
        tempos = [0, 0, 0]
        comparacoes = [0, 0, 0]
        trocas = [0, 0, 0]
        
        # Executa o mesmo teste várias vezes para obter resultados consistentes e calcular a média.
        for i in range(NUM_EXECUCOES_FINAL):
            vetor_original = teste["gerador"]()
            
            for idx, sorter in enumerate(sorters):
                vetor_copia = vetor_original.copy()
                sorter.reset_counters()

                inicio = time.perf_counter()
                sorter.sort(vetor_copia)
                fim = time.perf_counter()

                # Soma os resultados da execução atual aos acumuladores.
                tempos[idx] += (fim - inicio)
                comparacoes[idx] += sorter.comparisons
                trocas[idx] += sorter.swaps

        # Calcula e imprime os resultados médios para o cenário de teste atual.
        nomes = ["Quicksort Recursivo", f"Quicksort Híbrido (M={melhor_m})", "Quicksort Mediana de 3"]
        print("Resultados Médios:")

        for i in range(3):
            print(f"  - {nomes[i]}:")
            print(f"    Tempo: {tempos[i] / NUM_EXECUCOES_FINAL:.6f}s")
            print(f"    Comparações: {comparacoes[i] / NUM_EXECUCOES_FINAL:.0f}")
            print(f"    Trocas: {trocas[i] / NUM_EXECUCOES_FINAL:.0f}")


if __name__ == "__main__":
    main()