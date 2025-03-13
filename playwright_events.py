from playwright.sync_api import sync_playwright, Request, Response


def log_request(request: Request):
    print(f'Request: {request.url}')


def log_response(response: Response):
    print(f'Response: {response.url}')


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.on('request', log_request)
    page.on('response', log_response)

    page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
    )
    page.wait_for_timeout(2000)
