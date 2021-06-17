#%%
from time import sleep

from selenium import webdriver
from selenium import common
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

from config import CREDENCIAIS_AHGORA

# %%

def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",element, s)
    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    sleep(.5)
    apply_style(original_style)

def change_tab(driver):
    #get current window handle
    p = driver.current_window_handle

    #get first child window
    chwd = driver.window_handles

    for w in chwd:
        #switch focus to child window
        if(w!=p):
            driver.switch_to.window(w)
            break

# %%
# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())
# %%
# Open the Website
url_ahgora = 'https://www.ahgora.com.br/externo/index/a746461/'
browser.get(url_ahgora)
# %%
sleep(3)
# %%
# Write credentials and
# click on Log in Ahgora Now
ahgora_matricula = CREDENCIAIS_AHGORA['matricula']
ahgora_senha = CREDENCIAIS_AHGORA['senha']
objeto_caixa_login = browser.find_element_by_id('boxLogin')
objeto_caixa_login.find_element_by_id('matricula').send_keys(ahgora_matricula)
objeto_caixa_login.find_element_by_id('senha').send_keys(ahgora_senha)
objeto_caixa_login.find_element_by_xpath('//*[@id="boxLogin"]/div[3]/button').click()
# %%
ahgora_espelho_ahgora = 'https://mirror.www.ahgora.com.br/#/dashboard'
browser.get(ahgora_espelho_ahgora)

# %%
area_solicitacao_class_name = 'espelho-resumo-dia'

area_solicitacao_objeto = browser.find_element_by_class_name(area_solicitacao_class_name)

incluir_solicitacao_xpath = '//main/div/div/div[1]/div[2]/div[2]/div/div[3]/button'

area_solicitacao_objeto.find_element_by_xpath(incluir_solicitacao_xpath).click()
# %%
solicitacao_abono_botao_xpath = '//div/div/div[2]/div/div[1]/div/div[1]/a'
browser.find_element_by_xpath(solicitacao_abono_botao_xpath).click()
# %%
dia_inteiro_checkbox_xpath = '//div/div/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/div/div[1]/div/div'
browser.find_element_by_xpath(dia_inteiro_checkbox_xpath).click()

# %%
seta_dropdown_xpath = '//div/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div'
browser.find_element_by_xpath(seta_dropdown_xpath).click()
sleep(0.5)
# %%
element_to_reach_xpath = '//div/div/div[20]'
element = browser.find_element_by_xpath(element_to_reach_xpath)
actions = ActionChains(browser)
actions.move_to_element(element).perform()

home_office_dropdown_xpath = '//div/div/div[22]/a'
element = browser.find_element_by_xpath(home_office_dropdown_xpath).click()
# %%
mensagem_text_area_xpath = '//div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/textarea'
mensagem_conteudo = "Trabalho em Remoto"
browser.find_element_by_xpath(mensagem_text_area_xpath).send_keys(mensagem_conteudo)

# %%
botao_enviar_xpath = '//div/div/div[2]/div/div[2]/div/div[3]/div/button[1]'
browser.find_element_by_xpath(botao_enviar_xpath).click()
# %%
try:
    seta_dia_seguinte_botao_xpath = '//main/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/button[2]'
    browser.find_element_by_xpath(seta_dia_seguinte_botao_xpath).click()
except common.exceptions.ElementClickInterceptedException:
    url_atual = browser.current_url
    mes_atual_int = int(url_atual[-2:])
    # A url trabalha com número sempre com dois algarismos
    if mes_atual_int + 1 < 10:
        proximo_mes_str = '0' + str(mes_atual_int + 1)
    else:
        proximo_mes_str = str(mes_atual_int + 1)

    proxima_url = url_atual[:-2] + proximo_mes_str
    browser.get(proxima_url)
    sleep(3)
    browser.refresh()
    # Garantindo que o botão do primeiro dia esteja marcado
    first_day_div_xpath = '//main/div/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]'
    browser.find_element_by_xpath(first_day_div_xpath).click()
    first_day_div_object = browser.find_element_by_xpath(first_day_div_xpath)
    hover_action_chain = ActionChains(browser).move_to_element(first_day_div_object)
    hover_action_chain.click().perform()
# %%
