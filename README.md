# 🛠️ System Automation & IT Support CLI

[English Version](#-english-version) | [Versão em Português](#-versao-em-portugues)

---

## 🇧🇷 Versão em Português

Uma ferramenta leve e robusta de linha de comando (CLI) desenvolvida em Python para otimizar tarefas rotineiras de suporte de TI, monitoramento de hardware e organização de arquivos.

Desenvolvido como parte de um portfólio ativo voltado para administração de sistemas, automação de resolução de problemas e scripts limpos em Python.

### 🚀 Funcionalidades
1. **Relatório de Status do Sistema e Hardware**
   - Identifica a versão exata do SO (totalmente otimizado para Windows 11 e ambientes Linux).
   - Monitora em tempo real o **uso de CPU** e **consumo de memória RAM**.
   - Varre e lista **todas as unidades de armazenamento conectadas (SSDs/HDs)**, detalhando capacidade total, espaço usado e percentual livre.
2. **Limpeza de Arquivos Temporários**
   - Analisa diretórios temporários do sistema e remove arquivos de cache/lixo com segurança para liberar espaço em disco e melhorar a performance.
3. **Organizador Automático de Arquivos por Pastas**
   - Pergunta ao usuário o caminho do diretório alvo e organiza automaticamente arquivos soltos em pastas limpas e categorizadas (*Imagens, Documentos, Compactados, Executáveis, Outros*) com base em suas extensões.
4. **Log de Auditoria**
   - Registra automaticamente todas as ações executadas com timestamps exatos em um arquivo `automation_history.log` para rastreabilidade.

### 💻 Tecnologias Utilizadas
* **Python 3.x** (Linguagem Principal)
* **`psutil`** (Telemetria de sistema e hardware)
* **`colorama`** (Formatação de cores para interface de terminal)
* **Bibliotecas Padrão:** `os`, `shutil`, `platform`, `datetime`

---

## 🇺🇸 English Version

A lightweight, robust command-line interface (CLI) tool built in Python designed to streamline routine IT support tasks, hardware monitoring, and file organization.

Developed as part of an active portfolio focusing on system administration, troubleshooting automation, and clean Python scripting.

### 🚀 Features
1. **System & Hardware Status Report**
   - Detects the exact OS version (fully optimized for Windows 11 and Linux environments).
   - Monitors real-time **CPU usage** and **RAM utilization**.
   - Scans and lists **all connected storage drives (SSDs/HDs)**, detailing total capacity, used space, and free space percentage.
2. **Temporary Files Cleanup**
   - Scans system temporary directories and safely removes cache/junk files to free up disk space and boost performance.
3. **Automated Directory File Organizer**
   - Prompts the user for a target directory path and automatically sorts loose files into clean, categorized folders (*Images, Documents, Archives, Executables, Others*) based on their extensions.
4. **Audit Logging**
   - Automatically records all executed actions with exact timestamps into an `automation_history.log` file for traceability.

### 💻 Technologies Used
* **Python 3.x** (Core Language)
* **`psutil`** (System and hardware telemetry)
* **`colorama`** (CLI colored output formatting)
* **Standard Libraries:** `os`, `shutil`, `platform`, `datetime`

---

## ⚙️ Installation & Usage / Instalação e Uso

### Prerequisites / Pré-requisitos
Make sure you have Python installed on your machine. / Certifique-se de ter o Python instalado na sua máquina.

1. **Clone the repository / Clone o repositório:**
   ```bash
   git clone [https://github.com/Kiri404/system-automation-cli.git](https://github.com/Kiri404/system-automation-cli.git)
   cd system-automation-cli

Install dependencies / Instale as dependências:
Bash
pip install -r requirements.txt

Run the application / Execute a aplicação:
Bash
python main.py

📂 Project Structure / Estrutura do Projeto
system-automation-cli/
│
├── main.py                  # Main script containing CLI logic / Script principal da CLI
├── requirements.txt         # Dependencies (psutil, colorama) / Dependências
└── automation_history.log   # Auto-generated audit log / Log de auditoria gerado automaticamente

👤 Author / Autor:

Kiri
