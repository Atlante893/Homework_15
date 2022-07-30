def test_click_login_button_(get_home_page):
    home_page = get_home_page
    login_page = home_page.click_log_in()
    assert login_page.title == "Войти в аккаунт - Memrise", f'\nActual: {login_page.title}' \
                                                            f'\nExpected: "Войти в аккаунт - Memrise"'


def test_presence_logo_memrise_(get_home_page):
    home_page = get_home_page
    current_status = home_page.get_logo_memrise()
    assert current_status == True, f'\nActual: {current_status}\nExpected: "True"'


def test_learn_to_speak_text_(get_home_page):
    home_page = get_home_page
    current_text = home_page.get_learn_to_speak_text()
    assert current_text == "Learn to speak\nlike the locals", f'\nActual: {current_text}' \
                                                              f'\nExpected: "Learn to speak\nlike the locals"'


def test_click_start_learning_button_(get_home_page):
    home_page = get_home_page
    bienvenue_page = home_page.click_start_learning_button()
    assert bienvenue_page.title == "Создать бесплатный аккаунт - Memrise", \
        f'\nActual: {bienvenue_page.title}\nExpected: "Создать бесплатный аккаунт - Memrise"'


def test_blog_button_(get_home_page):
    home_page = get_home_page
    blog_page = home_page.click_blog_button()
    assert blog_page.title == "Memrise Blog", f'\nActual: {blog_page.title}\nExpected: "Memrise Blog"'


def test_login_greetings_message_text_(get_home_page):
    home_page = get_home_page
    login_page = home_page.click_log_in()
    current_text = login_page.get_greetings_message_text()
    assert current_text == "Войди в приложение, чтобы учиться быстрее и с удовольствием", \
        f'\nActual: {current_text}\nExpected: "Войди в приложение, чтобы учиться быстрее и с удовольствием"'


def test_blog_text_(get_home_page):
    home_page = get_home_page
    blog_page = home_page.click_blog_button()
    current_text = blog_page.get_mem_news_text()
    assert current_text == "MemNews", f'\nActual: {current_text}\nExpected: "MemNews"'


def test_blog_image_travel_presence_(get_home_page):
    home_page = get_home_page
    blog_page = home_page.click_blog_button()
    current_status = blog_page.get_image_travel()
    assert current_status == True, f'\nActual: {current_status}\nExpected: "True"'


def test_presence_image_background_(get_home_page):
    home_page = get_home_page
    current_status = home_page.get_image_background()
    assert current_status == True, f'\nActual: {current_status}\nExpected: "True"'


def test_travel_pages_(get_home_page):
    home_page = get_home_page
    blog_page = home_page.click_blog_button()
    bienvenue_page = blog_page.click_start_learning_button()
    login_page = bienvenue_page.click_log_in()
    assert login_page.title == "Войти в аккаунт - Memrise", f'\nActual: {login_page.title}' \
                                                            f'\nExpected: "Войти в аккаунт - Memrise"'


def test_login_page_chrome_(get_home_page):
    user_email = "eshenko.poul@gmail.com"
    user_password = "123456"
    home_page = get_home_page
    login_page = home_page.click_log_in()
    login_page.set_user_email(user_email).set_password(user_password).click_login_button()
    assert login_page.title == "Memrise", f'\nActual: {login_page.title}\nExpected: "Memrise"'
