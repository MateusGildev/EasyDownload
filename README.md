# EasyDownload

Automatize a organização de arquivos na pasta Downloads, movendo-os para subpastas específicas com base no tipo de arquivo (ex.: PDFs para "Documentos", imagens para "Imagens").

## Dependências

- **Python 3**

```bash
sudo apt install python3-pip
```

## Como Rodar

Certifique-se de que as dependências estejam instaladas e que você esteja no diretório correto.

Execute o script de monitoramento:

```bash
python3 Automatiza-Downloads.py
```

## Executando de Qualquer Lugar

Para rodar o script de qualquer diretório no terminal, siga os passos abaixo:

1. **Mova o script para um diretório acessível** (ex.: `/usr/local/bin`):

   ```bash
   sudo mv Automatiza-Downloads.py /usr/local/bin/automatiza-downloads
   sudo chmod +x /usr/local/bin/automatiza-downloads
   ```

2. **Agora, você pode executar o script de qualquer pasta**:

   ```bash
   automatiza-downloads
   ```

Se preferir manter o script na sua pasta de projetos, adicione seu diretório ao PATH no arquivo `~/.bashrc` ou `~/.zshrc`:

```bash
echo 'export PATH="$HOME/Documents/Programação/EasyDownload:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

## Personalização

Você pode configurar as extensões de arquivos no script para atender às suas necessidades. Exemplo:

```python
extensoes = {
    "Documentos": [".pdf", ".docx", ".txt"],
    "Imagens": [".jpg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv"],
}
```

## Automatização

Para rodar o script automaticamente ao iniciar o sistema, você pode adicioná-lo ao **Startup Applications** do seu sistema operacional ou criar um serviço no systemd.

## Licença

Este projeto está disponível sob a licença MIT.


