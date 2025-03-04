class BrowserHistory:
    def __init__(self, homepage: str):
        self.back_r = []
        self.forward_r = []
        self.current = homepage  

    def visit(self, url: str) -> None:
        self.back_r.append(self.current)  
        self.current = url  
        self.forward_r.clear()  

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.back_r:  
                self.forward_r.append(self.current)  
                self.current = self.back_r.pop()  
            else:
                break  
        return self.current

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.forward_r:  
                self.back_r.append(self.current)  
                self.current = self.forward_r.pop()  
            else:
                break  
        return self.current
