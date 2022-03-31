class LengthValidator:
    def getSize(bytes , default = "B"):
        for unit in ["" , "K" , "M" , "G" , "T" , "P"]:
            if (bytes < 1024):
                return f"{bytes:.2f}{unit}{default}"
            bytes /= 1024