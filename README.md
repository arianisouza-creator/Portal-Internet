# Portal-MSE

Portal administrativo em Streamlit com o primeiro modulo de `Controle de Internet`, adaptado ao layout MSE.

## Como rodar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Estrutura principal

- `app.py`: entrada da aplicacao Streamlit.
- `controle-internet.html`: interface do portal com o layout MSE.
- `requirements.txt`: dependencias para execucao no Streamlit Cloud.

## Acesso protegido

O portal abre normalmente na visao geral.

- As abas de cadastro protegidas usam `ADM` / `mse2026`.
- A protecao fica nas areas de `Linhas Ativas e Acessos` e `Contratos`.

## Deploy no Streamlit Community Cloud

1. Suba este repositorio no GitHub.
2. Entre em [Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud).
3. Clique em `Create app`.
4. Escolha o repositorio `Portal-MSE`.
5. Defina o arquivo principal como `app.py`.
6. Clique em `Deploy`.

## Observacoes

- O modulo atual e o `Controle de Internet`.
- O HTML foi mantido separado para preservar o visual MSE com menos retrabalho.
- A base esta pronta para crescer com novos modulos do portal.
