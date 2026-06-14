import kagglehub

print("Iniciando o download dos arquivos oficiais da competição via KaggleHub...")
try:
    # Este comando baixa o SDK e as fixtures oficiais
    path = kagglehub.competition_download('ai-agent-security-multi-step-tool-attacks')
    print("\n[SUCESSO] Arquivos baixados com sucesso!")
    print("Os arquivos estão armazenados em:", path)
except Exception as e:
    print(f"\n[ERRO] Falha ao baixar os arquivos: {e}")
    print("Dica: Se pedir autenticação, precisamos configurar o token do Kaggle.")

