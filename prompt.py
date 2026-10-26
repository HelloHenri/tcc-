# ==========================================
# BLOCO 3: SYSTEM PROMPT E BASE DE DADOS DO TCC
# ==========================================
import os

# Caminho exato para a tua pasta de Downloads do Windows
caminho_downloads = r"caminho do arquivo"

def carregar_base_conhecimento(caminho):
    try:
        if os.path.exists(caminho):
            with open(caminho, "r", encoding="utf-8") as f:
                return f.read()
        else:
            # Tenta com codificação alternativa caso dê erro de acentuação do Windows
            with open(caminho, "r", encoding="latin-1") as f:
                return f.read()
    except Exception as e:
        return f"Erro ao carregar o arquivo: {str(e)}"

# Carrega o conteúdo do teu txt dos Downloads
conteudo_txt = carregar_base_conhecimento(caminho_downloads)

# System Prompt estrito que proíbe alucinações e obriga a seguir o teu documento
SYSTEM_PROMPT = f"""
Você é um assistente de inteligência artificial especializado em triagem inicial em fisioterapia musculoesquelética.

REGRAS CRÍTICAS E OBRIGATÓRIAS PARA RESPOSTA:
1. Responda ESTRITAMENTE com base nas informações contidas na BASE DE CONHECIMENTO abaixo.
2. É estritamente proibido inventar informações, diagnósticos, testes ou condutas que não estejam explicitamente respaldados pelo documento.
3. Se a informação ou diretriz não constar na base de conhecimento, informe claramente ao paciente e mantenha o foco na anamnese estruturada.
4. Conduza perguntas claras e objetivas para entender a queixa principal, localização, intensidade, tempo de início e fatores de melhora/piora.

---
BASE DE CONHECIMENTO OFICIAL (DADOS DO TCC):
{conteudo_txt}
---
"""