# Projeto: teste-hackarun — ensaio do HackaRun 2026

## Contexto
- Projeto de TESTE para ensaiar o fluxo do HackaRun 2026 (11–14/11). Nada daqui vira código do projeto real: o regulamento proíbe começar a solução antes do lançamento.
- Problema: validar a stack e o deploy antes do evento. Usuário: a própria equipe. Fluxo principal: digitar uma pergunta → app chama o Gemini → mostra a resposta e o modelo que respondeu.
- No dia do evento, este arquivo serve de molde: trocar o Contexto pelo desafio real.

## Stack
- Python 3 + Streamlit (`app.py`). Dependências em `requirements.txt`, ambiente virtual em `.venv/`.
- IA via API do Gemini (`google-genai`), chave lida da variável de ambiente `GEMINI_API_KEY`.
- Deploy no Streamlit Community Cloud, com a chave em Secrets (não no repositório).
- Rodar localmente: `source .venv/bin/activate && streamlit run app.py`.

## Regras de trabalho
- Mudanças pequenas; explique o que vai fazer antes de editar muitos arquivos.
- Nunca ler, imprimir ou commitar o `.env`. Chaves e dados pessoais nunca entram no código.
- Confirmar comigo antes de qualquer push, merge ou exclusão.
- Toda função nova ganha pelo menos 1 teste simples em `tests/`.
- Comentários e textos da interface em português.
- Priorize o fluxo principal funcionando antes de qualquer extra.
- Ao terminar uma tarefa, sugira a mensagem de commit.

## Armadilhas já conhecidas
- A API pode responder `503 UNAVAILABLE` em horário de pico. Manter o fallback de `MODELOS` em `app.py` (principal `gemini-3.8-flash`, reserva `gemini-3.5-flash`) e o `st.error` amigável quando os dois falham.
- Em script rodado via stdin (`python - <<EOF`), `load_dotenv()` não acha o arquivo; usar `load_dotenv(".env")`.
