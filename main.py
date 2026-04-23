# automacao-login-playwright
Automação de login usando Python e Playwright
from playwright.sync_api import sync_playwright
import time
with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    navegador = pw.chromium.launch(headless=False, slow_mo=3000)
    contexto = navegador.new_context()
    pagina = contexto.new_page()

    pagina.goto("https://www.hashtagtreinamentos.com/")

    #pagina.locator('xpath=/html/body/main/section[1]/div[2]/a').click()

    botao = pagina.locator("div").filter(has_text="Torne-se uma referência no").get_by_role("link")
    with contexto.expect_page() as pagina2_info:
     botao.click()


    #limks = pagina.get_by_role("link").all()
    #for limk in links:

       #print(link)
    

    pagina2 = pagina2_info.value
    pagina2.goto("https://www.hashtagtreinamentos.com/pg-inscricao-python")

    pagina.bring_to_front()

    pagina.locator('xpath=/html/body/header/div/div/a[1]').click()

    pagina.locator("#email-login").fill("arthurdenobregaarthurdenobrega@gmail.com")
    
    pagina.locator('xpath=//*[@id="login-grupo-conteudos"]/div/div/div[2]/div/button').click()

    pagina2.bring_to_front()

    pagina2.locator('xpath=//*[@id="botao-hero"]/div/div/a/span/span').click()

    pagina2.locator('xpath=//*[@id="botao-linkcomu-padrao1"]/span/span').click()

    inputs = pagina.locator("input")

    pagina2.get_by_placeholder("*Seu nome e sobrenome").fill("Arthur de Nóbrega")
    pagina2.get_by_placeholder("*Seu melhor e-mail").fill("arthurdenobregaarthurdenobrega@gmail.com")
    pagina2.get_by_placeholder("DDD").fill("55")
    pagina2.get_by_placeholder("Seu celular").fill("1191353031")
   
    pagina2.locator('xpath=//*[@id="_form_5346_submit"]').click()

    time.sleep(3000)
    navegador.close()
