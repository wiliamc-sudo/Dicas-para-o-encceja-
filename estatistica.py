# Autor: Wiliam C. - Dev Jr | Estatística Completa
# Objetivo: Código limpo, funções puras e tratamento de erros - padrão SOLID

from collections import Counter
import statistics

def limpar_dados(texto: str) -> list[float]:
    """Converte texto '7, 8, 9' em lista de números. Trata erro."""
    try:
        numeros = [float(x.strip()) for x in texto.replace(';',' ,').split(',') if x.strip()]
        if len(numeros) < 2:
            raise ValueError("Digite pelo menos 2 números")
        return numeros
    except Exception as e:
        raise ValueError(f"Erro nos dados: {e}")

def calcular_estatisticas(dados: list[float]) -> dict:
    """Calcula tudo - cada fórmula isolada (Clean Code)"""
    dados_ordenados = sorted(dados)
    freq = Counter(dados)
    
    # Moda - O(n) com Counter
    max_freq = max(freq.values())
    modas = [k for k,v in freq.items() if v == max_freq]
    moda_str = "Amodal" if max_freq == 1 else ", ".join(map(str, modas))

    return {
        "quantidade": len(dados),
        "ordenados": dados_ordenados,
        "media": round(statistics.mean(dados), 2),
        "mediana": statistics.median(dados),
        "moda": moda_str,
        "amplitude": round(max(dados) - min(dados), 2),
        "variancia": round(statistics.variance(dados), 2),
        "desvio_padrao": round(statistics.stdev(dados), 2),
        "min": min(dados),
        "max": max(dados),
        "frequencia": dict(freq)
    }

# --- EXEMPLO DE USO / RESULTADOS ---
if __name__ == "__main__":
    entrada = "7, 8, 9, 6, 8, 10, 7, 8"
    dados = limpar_dados(entrada)
    res = calcular_estatisticas(dados)
    
    print("=== RESULTADOS PROFISSIONAIS ===")
    for k,v in res.items():
        print(f"{k}: {v}")