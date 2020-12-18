# Salesforce scripts

### Pré-requisitos
- Python3
- Clonar o repositório na pasta base do SO (recomenda-se o caminho **``$HOME/``**)

## Python scripts to automatize cli salesforce commands

### create_scratch_org.py
- Conecta a DevHub, cria, instala as dependências e sobe o código do app na scratch org

### Como usar
- Adicione o json abaixo no **``tasks.json``** na pasta **``.vscode``**

  ```json
    {
    "label": "docker-run",
        "command": "python3 $HOME/docker-locally/create_scratch_org.py -wf ${workspaceFolder} -sa {nome do alias da scratch org}",
        "type": "shell",
        "group": {
            "kind": "test",
            "isDefault": true
            }
    }
    ```

- Execute a task pelo atráves do VSCode **``Ctrl + Shift + P ``** --> **``Run Tasks``** --> **``create_scratch_org``** 

### Argumentos do script 

#### Argumentos obrigatórios
- ``-wf WORKSPACE_FOLDER, --workspace-folder WORKSPACE_FOLDER The workspace path to the folder of the project``

- ``-sa SCRATCH_ALIAS, --scratch-alias SCRATCH_ALIAS The scratch org's alias``

#### Argumentos opcionais
- ``-dd DURATION_DAYS, --duration-days DURATION_DAYS The duration days of scratch org``
