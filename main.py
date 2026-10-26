# main.py - Otimizado para gastar o mínimo de tokens
from google import genai
import time
import sys

from config import CHAVES_API
from prompt import SYSTEM_PROMPT

print("=" * 60)
print("🤖 TCC - TRIAGEM FISIOTERÁPICA (MODO ECONÓMICO)")
print("Digite 'sair' a qualquer momento para encerrar.")
print("=" * 60)
print()

client_genai = genai.Client(api_key=CHAVES_API["gemini"])

# Mensagem inicial de boas-vindas
print("🤖 Assistente: Olá! Sou seu assistente de triagem em fisioterapia musculoesquelética. Qual é a sua principal queixa ou dor no momento?\n")
print("-" * 60)

# Mantemos um histórico leve e limpo apenas com a última troca para poupar tokens
historico_conversa = ""

while True:
    try:
        texto_usuario = input("👤 Você (Paciente): ")
        
        if not texto_usuario.strip():
            continue
            
        if texto_usuario.strip().lower() in ['sair', 'exit', 'parar']:
            print("\n🤖 Assistente: Atendimento encerrado. Boa apresentação de TCC!")
            break
            
        # Monta um pacote enxuto: Regras + Contexto do Txt + Conversa recente
        prompt_atual = f"""
{SYSTEM_PROMPT}

Histórico recente:
{historico_conversa}

Paciente: {texto_usuario}
Assistente:
"""
        
        print("\n⏳ Processando...")
        
        # Chamada única e direta, sem loops exagerados para não queimar cota
        resposta = client_genai.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt_atual,
            config={"temperature": 0.1}
        )
        
        texto_resposta = resposta.text
        print(f"\n🤖 Assistente:\n{texto_resposta}\n")
        print("-" * 60)
        
        # Atualiza apenas a última interação para manter o contexto sem inflar tokens
        historico_conversa += f"\nPaciente: {texto_usuario}\nAssistente: {texto_resposta}"
        
    except KeyboardInterrupt:
        print("\n\n🤖 Atendimento interrompido.")
        break
    except Exception as e:
        print(f"\n❌ Erro: {str(e)}\n")