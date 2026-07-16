# QL REDES — Website

## Live site

- **Website:** https://salesio.github.io/ql-redes/
- **Repository:** https://github.com/salesio/ql-redes
- **Branch:** main (GitHub Pages source: / root)


Website multi-página moderno para **QL REDES / QL Group** (Maputo, Moçambique): redes informáticas, electricidade, segurança electrónica, portões e pérgolas.

## Estrutura

```
ql-redes/
├── index.html          # Início
├── sobre.html          # Sobre nós
├── servicos.html       # Serviços
├── portfolio.html      # Galeria de projectos
├── produtos.html       # Catálogo + pedido de orçamento (carrinho)
├── blog.html           # Artigos / SEO
├── contacto.html       # Contacto + formulário → WhatsApp
├── faq.html
├── privacidade.html
├── assets/
│   ├── css/style.css
│   ├── js/
│   │   ├── main.js       # Header, footer, galeria, formulário
│   │   ├── cart.js       # Carrinho de orçamento + WhatsApp
│   │   └── products.js   # Catálogo
│   └── images/           # Fotos do cliente (copiadas)
└── README.md
```

## Como abrir

Abra `index.html` no browser (duplo clique) ou sirva a pasta com um servidor local:

```powershell
cd "C:\Users\Alves King Edition\Documents\Project 2\ql-redes"
python -m http.server 8080
```

Depois visite: http://localhost:8080

## Funcionalidades

- Design responsivo (mobile-first), cores ciano / navy
- WhatsApp flutuante e CTAs em todas as páginas
- **Produtos**: adicionar ao “carrinho” → enviar **pedido de orçamento** (não é loja com pagamento)
- Portfólio com filtros e lightbox
- Formulário de contacto que abre WhatsApp com a mensagem pronta
- SEO básico (meta tags em português, keywords Maputo)

## Contactos no site

| Canal | Valor |
|--------|--------|
| WhatsApp / Tel | +258 84 842 6310 |
| Tel alt. | +258 87 249 7969 |
| E-mail | qlredes@gmail.com |
| Morada | Rua Irmãos Rubbi 2250, Maputo |
| Facebook | facebook.com/joaquimlleao |
| Instagram | @ql_group_ |

## Personalizar

1. **Produtos** — edite `assets/js/products.js`
2. **Cores** — variáveis em `assets/css/style.css` (`:root`)
3. **Textos / depoimentos** — HTML de cada página
4. **Imagens** — pasta `assets/images/`

## Deploy

Hospede a pasta completa (HTML/CSS/JS/imagens) em Hostinger, Netlify, Cloudflare Pages, ou qualquer hosting estático. Aponte o domínio (ex. `qlgroup.co.mz` / `qlredes.co.mz`) para a pasta pública.

Não requer Node.js nem base de dados.
