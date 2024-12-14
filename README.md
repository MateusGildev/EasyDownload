
# EasyDownload
Automatize a organização de arquivos na pasta `Downloads`, movendo-os para subpastas específicas com base no tipo de arquivo (ex.: PDFs para "Documentos", imagens para "Imagens").

---

## Dependências
- **Python 3**
- Biblioteca **watchdog**:
  ```bash
  pip install watchdog
  ```

---

## Como Rodar
1. Certifique-se de que as dependências estejam instaladas.
2. Execute o script de monitoramento:
   ```bash
   python3 monitorar_downloads.py
   ```

---

## Personalização
Configure as extensões de arquivos no script para atender às suas necessidades. Exemplo:
```python
extensoes = {
    "Documentos": [".pdf", ".docx", ".txt"],
    "Imagens": [".jpg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv"],
}
```

---

## Licença
Este projeto está disponível sob a licença MIT.


