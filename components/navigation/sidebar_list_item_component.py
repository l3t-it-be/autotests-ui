import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(
            page, 'Sidebar item', f'{identifier}-drawer-list-item-icon'
        )
        self.title = Text(
            page,
            'Sidebar item title',
            f'{identifier}-drawer-list-item-title-text',
        )
        self.button = Button(
            page, 'Sidebar item title', f'{identifier}-drawer-list-item-button'
        )
        self.url = re.compile(f'.*/#/{identifier}')

    def check_visible(self, title: str):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.button.check_visible()

    def navigate(self):
        self.button.click()
        self.check_current_url(self.url)
