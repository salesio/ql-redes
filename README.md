# QL REDES â€” Website

Website multi-pÃ¡gina moderno para **QL REDES / QL Group** (Maputo, MoÃ§ambique): redes informÃ¡ticas, electricidade, seguranÃ§a electrÃ³nica, portÃµes e pÃ©rgolas.

## Estrutura

```
ql-redes/
â”œâ”€â”€ index.html          # InÃ­cio
â”œâ”€â”€ sobre.html          # Sobre nÃ³s
â”œâ”€â”€ servicos.html       # ServiÃ§os
â”œâ”€â”€ portfolio.html      # Galeria de projectos
â”œâ”€â”€ produtos.html       # CatÃ¡logo + pedido de orÃ§amento (carrinho)
â”œâ”€â”€ blog.html           # Artigos / SEO
â”œâ”€â”€ contacto.html       # Contacto + formulÃ¡rio â†’ WhatsApp
â”œâ”€â”€ faq.html
â”œâ”€â”€ privacidade.html
â”œâ”€â”€ assets/
â”‚   â”œâ”€â”€ css/style.css
â”‚   â”œâ”€â”€ js/
â”‚   â”‚   â”œâ”€â”€ main.js       # Header, footer, galeria, formulÃ¡rio
â”‚   â”‚   â”œâ”€â”€ cart.js       # Carrinho de orÃ§amento + WhatsApp
â”‚   â”‚   â””â”€â”€ products.js   # CatÃ¡logo
â”‚   â””â”€â”€ images/           # Fotos do cliente (copiadas)
â””â”€â”€ README.md
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
- WhatsApp flutuante e CTAs em todas as pÃ¡ginas
- **Produtos**: adicionar ao â€œcarrinhoâ€ â†’ enviar **pedido de orÃ§amento** (nÃ£o Ã© loja com pagamento)
- PortfÃ³lio com filtros e lightbox
- FormulÃ¡rio de contacto que abre WhatsApp com a mensagem pronta
- SEO bÃ¡sico (meta tags em portuguÃªs, keywords Maputo)

## Contactos no site

| Canal | Valor |
|--------|--------|
| WhatsApp / Tel | +258 84 842 6310 |
| Tel alt. | +258 87 249 7969 |
| E-mail | qlredes@gmail.com |
| Morada | Rua IrmÃ£os Rubbi 2250, Maputo |
| Facebook | facebook.com/joaquimlleao |
| Instagram | @ql_group_ |

## Personalizar

1. **Produtos** â€” edite `assets/js/products.js`
2. **Cores** â€” variÃ¡veis em `assets/css/style.css` (`:root`)
3. **Textos / depoimentos** â€” HTML de cada pÃ¡gina
4. **Imagens** â€” pasta `assets/images/`

## Deploy

Hospede a pasta completa (HTML/CSS/JS/imagens) em Hostinger, Netlify, Cloudflare Pages, ou qualquer hosting estÃ¡tico. Aponte o domÃ­nio (ex. `qlgroup.co.mz` / `qlredes.co.mz`) para a pasta pÃºblica.

NÃ£o requer Node.js nem base de dados.

