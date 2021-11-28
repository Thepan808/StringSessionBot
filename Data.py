from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
♦️ Opa {}

Bem vindo ao {}

Você pode me usar para gerar as sessões : Pyrogram e Telethon string sessão. Use alguns botões abaixo para saber mais!

By 『♚•꣣𝑻⃯̭꣣𝒉⃯̭꣣𝒆⃯̭꣣ ┼ ͓꣣𝑷⃯̭͓꣣𝒂⃯̭꣣𝒏⃯̭꣣𝒅⃯̭͓꣣𝒂⃯̭꣣•♚』 
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("➜ ♦️ Iniciar à Gerar à sua vossa Sessão String ♦️", callback_data="generate")],
        [InlineKeyboardButton(text="🧐 Voltar ao início 🧐", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("➜ ♦️ Iniciar à Gerar à sua vossa Sessão String ♦️", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("➜ ♦️ Iniciar à Gerar à sua vossa Sessão String ♦️", callback_data="generate")],
        [InlineKeyboardButton("➜ Criador", url="https://t.me/The_Panda_Ofc")],
        [
            InlineKeyboardButton("Como me usar❔", callback_data="help"),
            InlineKeyboardButton("♦️ Sobre o bot ♦️", callback_data="about")
        ],
        [InlineKeyboardButton("♥ Canal ♥", url="https://t.me/RabiscoS_MeuS_77")],
    ]

    # Help Message
    HELP = """
♦️ **Comandos do bot** ♦️

/about - Sobre o bot
/help - Ajuda sobre o bot
/start - Iniciar o bot
/generate - Iniciar a gerar a sessão 
/cancel - Cancelar o processo 
/restart - Reiniciar o processo
"""

    # About Message
    ABOUT = """
**Sobre o bot** 

♦️ Bot para gerar sessão Pyrogram e Telethon string ♦️

♦️ Criador : [Clique aqui](https://t.me/The_Panda_Ofc)

♦️ Estrutura : [Pyrogram](docs.pyrogram.org)

♦️ Linguagem : [Python](www.python.org)

♦️ Desenvolvedor : @The_Panda_Ofc
    """
