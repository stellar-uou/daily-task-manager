def menu():
  print("""
  Gerenciador de tarefas:

   1 - Adicionar nova tarefa
   2 - Visualizar todas as tarefas
   3 - Remover tarefa
   4 - Sair
  """)

def adicionar(tarefas):
  nova_tarefa = input("Digite sua nova tarefa: ")
  tarefas.append(nova_tarefa)
  print(f"A tarefa {nova_tarefa} foi adicionada com sucesso!")

def visualizar(tarefas):
  if tarefas:
    print("\nTarefas atuais:")

    for index, tarefa in enumerate(tarefas, start=1):
      print(f"{index}. {tarefa}")
    
  else:
    print("Não há tarefas registradas no momento.")

def remover(tarefas):
  visualizar(tarefas)
  if tarefas:
    try:
      indice = int(input("\nDigite o número da tarefa que deseja remover: "))
      tarefa_removida = tarefas.pop(indice - 1)
      print(f"A tarefa {tarefa_removida} foi removida com sucesso!")
    
    except:
      print("Número inválido, tente novamente.")

def gerenciador():
  tarefas = []
  while True:
    menu()
    operacao = input("Digite o número da ação que deeja fazer: ")

    if operacao == "1":
      adicionar(tarefas)

    elif operacao == "2":
      visualizar(tarefas)

    elif operacao == "3":
      remover(tarefas)
    
    elif operacao == "4":
      print("Fechando o programa, até mais!")
      break

    else:
      print("Opção inválida, tente novamente.")

gerenciador()
