import os
import shutil
import platform
import psutil
from datetime import datetime
from colorama import init, Fore

# Inicializa o colorama para cores no terminal
init(autoreset=True)

def log_action(message):
    """Grava um registro das ações executadas em um arquivo de log."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    with open("automation_history.log", "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)

def show_banner():
    print(Fore.CYAN + "=" * 50)
    print(Fore.GREEN + "       KIRI'S SYSTEM AUTOMATION CLI v1.0")
    print(Fore.CYAN + "=" * 50)

def system_info():
    print(Fore.YELLOW + "\n[+] Coletando Informações do Sistema e Armazenamento...")
    
    # Identifica o SO de forma mais precisa (capturando Windows 11 se aplicável)
    os_name = platform.system()
    if os_name == "Windows":
        win_version = platform.win32_ver()
        # win_version[1] traz a build. Build >= 22000 indica Windows 11
        build_num = int(win_version[1].split('.')[-1]) if win_version[1] else 0
        os_display = "Windows 11" if build_num >= 22000 else f"Windows {win_version[0]}"
    else:
        os_display = f"{os_name} {platform.release()}"

    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    
    print(Fore.WHITE + f"• Sistema Operacional: {os_display}")
    print(f"• Uso de CPU: {cpu_usage}%")
    print(f"• Memória RAM Usada: {memory.percent}% ({round(memory.used / (1024**3), 2)} GB / {round(memory.total / (1024**3), 2)} GB)")
    
    print(Fore.CYAN + "\n--- Unidades de Armazenamento (SSDs/HDs) ---")
    # Lista todas as partições/discos conectados
    partitions = psutil.disk_partitions(all=False)
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            print(Fore.WHITE + f"• Unidade [{partition.device}] ({partition.fstype})")
            print(f"  - Total: {round(partition_usage.total / (1024**3), 2)} GB")
            print(f"  - Usado: {partition_usage.percent}% ({round(partition_usage.used / (1024**3), 2)} GB)")
            print(f"  - Livre: {round(partition_usage.free / (1024**3), 2)} GB")
        except PermissionError:
            # Ignora unidades que exigem permissão especial ou estão desconectadas (como leitor de DVD vazio)
            continue

    log_action("Consulta detalhada de informações do sistema e múltiplos discos realizada.")

def clean_temp_files():
    print(Fore.YELLOW + "\n[+] Iniciando varredura de arquivos temporários...")
    # Caminho comum de temp (exemplo genérico ou focado no ambiente do usuário)
    temp_dirs = []
    
    if platform.system() == "Windows":
        user_temp = os.environ.get("TEMP")
        if user_temp:
            temp_dirs.append(user_temp)
    else:
        temp_dirs.append("/tmp")
        
    removed_count = 0
    for folder in temp_dirs:
        if os.path.exists(folder):
            for item in os.listdir(folder):
                item_path = os.path.join(folder, item)
                try:
                    if os.path.isfile(item_path) or os.path.islink(item_path):
                        os.unlink(item_path)
                        removed_count += 1
                except Exception:
                    # Ignora arquivos que estão em uso pelo sistema
                    pass
                    
    print(Fore.GREEN + f"[Sucesso] Limpeza concluída! {removed_count} arquivos temporários liberados.")
    log_action(f"Limpeza de temporários executada. {removed_count} itens removidos.")

def organize_downloads():
    print(Fore.YELLOW + "\n[+] Organizador de Pastas (Insira o caminho da pasta para organizar):")
    target_path = input(Fore.WHITE + "Digite o caminho completo da pasta (ex: C:/Users/SeuUsuario/Downloads): ").strip()
    
    if not os.path.exists(target_path):
        print(Fore.RED + "[Erro] O caminho informado não existe.")
        return

    # Dicionario de extensões
    extensions_map = {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
        "Compactados": [".zip", ".rar", ".7z", ".tar"],
        "Executaveis": [".exe", ".msi", ".bat", ".sh"]
    }

    moved_files = 0
    for filename in os.listdir(target_path):
        file_path = os.path.join(target_path, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            
            assigned_folder = "Outros"
            for folder_name, exts in extensions_map.items():
                if ext in exts:
                    assigned_folder = folder_name
                    break
            
            dest_folder = os.path.join(target_path, assigned_folder)
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
                
            shutil.move(file_path, os.path.join(dest_folder, filename))
            moved_files += 1

    print(Fore.GREEN + f"[Sucesso] Pasta organizada! {moved_files} arquivos movidos.")
    log_action(f"Organização de pasta realizada em: {target_path}. {moved_files} arquivos movidos.")

def main():
    while True:
        show_banner()
        print(Fore.WHITE + "\nEscolha uma opção:")
        print("1 - Exibir Status e Relatório de Hardware")
        print("2 - Limpar Arquivos Temporários")
        print("3 - Organizar Pasta por Tipo de Arquivo")
        print("0 - Sair")
        
        choice = input(Fore.CYAN + "\nOpção desejada: ").strip()
        
        if choice == "1":
            system_info()
        elif choice == "2":
            clean_temp_files()
        elif choice == "3":
            organize_downloads()
        elif choice == "0":
            print(Fore.GREEN + "\nSaindo... Bom trabalho, Kiri! 🚀")
            break
        else:
            print(Fore.RED + "[Erro] Opção inválida. Tente novamente.")
            
        input(Fore.YELLOW + "\nPressione ENTER para continuar...")
        os.system('cls' if platform.system() == 'Windows' else 'clear')

if __name__ == "__main__":
    main()