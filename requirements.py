try:
    import sys
    import builtins
    import subprocess

except Exception:
    raise Exception

class DependencyUpdator:
    def __init__(self , *args , **kwargs) -> builtins.str:
        builtins.super(DependencyUpdator , self).__init__(*args , **kwargs)
        self.mainInterpreter = builtins.str("pip")
        self.executable = sys.executable
        
    def InterpreterUpdator(self):
        subprocess.call([
            self.executable , "-m" , self.mainInterpreter ,
            "install" , "--upgrade" , self.mainInterpreter
        ])

    def LibraryInstaller(self , package : builtins.str):
        subprocess.call([
            self.executable , "-m" , self.mainInterpreter ,
            "install" , package
        ])

if __name__ == "__main__":
    DependencyUpdator().InterpreterUpdator()
    DependencyUpdator().LibraryInstaller("requests")
    DependencyUpdator().LibraryInstaller("sockets")
    DependencyUpdator().LibraryInstaller("GPUtil")
    DependencyUpdator().LibraryInstaller("psutil")
    DependencyUpdator().LibraryInstaller("getmac")
    DependencyUpdator().LibraryInstaller("python-cfonts")
    DependencyUpdator().LibraryInstaller("colorama")