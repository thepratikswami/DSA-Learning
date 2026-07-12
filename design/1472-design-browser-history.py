class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        # Truncate any forward history, then append the new page.
        del self.history[self.current + 1:]
        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]


# DEBUG RUNNER START
if __name__ == "__main__":
    browser = BrowserHistory("leetcode.com")
    browser.visit("google.com")
    browser.visit("facebook.com")
    browser.visit("youtube.com")
    print(browser.back(1))     # facebook.com
    print(browser.back(1))     # google.com
    print(browser.forward(1))  # facebook.com
    browser.visit("linkedin.com")
    print(browser.forward(2))  # linkedin.com (no forward history)
    print(browser.back(2))     # google.com
    print(browser.back(7))     # leetcode.com (clamped)
# DEBUG RUNNER END
