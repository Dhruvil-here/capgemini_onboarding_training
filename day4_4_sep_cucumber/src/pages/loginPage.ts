import { Page, expect } from '@playwright/test';

export class LoginPage {
  constructor(private page: Page) {}

  // Locators
  private txtUser = '#user-name';
  private txtPass = '#password';
  private btnLogin = '#login-button';

  async openApp() {
    await this.page.goto('https://www.saucedemo.com/');
  }

  async login() {
    console.log('Entering credentials');

    await this.page.fill(this.txtUser, 'standard_user');
    await this.page.fill(this.txtPass, 'secret_sauce');
    await this.page.click(this.btnLogin);
  }

  async loginWithInvalidCredentials() {
    console.log('Entering Invalid credentials');

    await this.page.fill(this.txtUser, 'user');
    await this.page.fill(this.txtPass, 'sauce');
  }

  async clickButton() {
    await this.page.click(this.btnLogin);
  }

  async errorCheck() {
    await expect(
      this.page.locator('[data-test="error"]')
    ).toBeVisible();
  }

  async loginWithMultipleUsers(
    username: string,
    password: string
  ) {
    await this.page.fill(this.txtUser, username);
    await this.page.fill(this.txtPass, password);
    await this.page.click(this.btnLogin);
  }
}